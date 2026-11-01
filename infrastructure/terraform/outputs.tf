output "research_bucket_name" {
  description = "Name of the development S3 bucket"
  value       = aws_s3_bucket.research_data.id
}

output "research_bucket_arn" {
  description = "ARN of the development S3 bucket"
  value       = aws_s3_bucket.research_data.arn
}

output "aws_region" {
  description = "AWS region for the project"
  value       = aws_s3_bucket.research_data.region
}
