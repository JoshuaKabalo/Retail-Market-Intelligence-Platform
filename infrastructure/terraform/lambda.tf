
data "archive_file" "lambda_package" {
  type        = "zip"
  output_path = "${path.module}/lambda_package.zip"

  source {
    content  = file("${path.module}/../../src/pipeline.py")
    filename = "pipeline.py"
  }

  source {
    content  = file("${path.module}/../../src/scoring.py")
    filename = "scoring.py"
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "retail-intelligence-dev-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "lambda_s3_policy" {
  name = "retail-intelligence-s3-access"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["s3:GetObject"]
        Resource = [
          "${aws_s3_bucket.research_data.arn}/input/sample_products.json"
        ]
      },
      {
        Effect = "Allow"
        Action = ["s3:PutObject"]
        Resource = [
          "${aws_s3_bucket.research_data.arn}/reports/*"
        ]
      }
    ]
  })
}

resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/retail-intelligence-dev"
  retention_in_days = 7
}

resource "aws_iam_role_policy_attachment" "lambda_logging" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "research_pipeline" {
  function_name    = "retail-intelligence-dev"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.13"
  handler          = "pipeline.lambda_handler"
  filename         = data.archive_file.lambda_package.output_path
  source_code_hash = data.archive_file.lambda_package.output_base64sha256

  timeout     = 30
  memory_size = 128

  environment {
    variables = {
      RESEARCH_BUCKET = aws_s3_bucket.research_data.id
    }
  }

  depends_on = [
    aws_iam_role_policy.lambda_s3_policy,
    aws_iam_role_policy_attachment.lambda_logging,
    aws_cloudwatch_log_group.lambda_logs
  ]

  tags = {
    Project     = "RetailMarketIntelligence"
    Environment = "dev"
  }
}
