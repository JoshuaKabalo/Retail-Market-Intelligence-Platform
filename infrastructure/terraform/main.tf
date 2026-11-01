
terraform {
  required_version = ">= 1.17.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }

    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region  = "us-east-2"
  profile = "dev"
}

resource "aws_s3_bucket" "research_data" {
  bucket_prefix = "retail-intelligence-dev-"

  tags = {
    Project     = "RetailMarketIntelligence"
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}

resource "aws_s3_bucket_public_access_block" "research_data" {
  bucket = aws_s3_bucket.research_data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "research_data" {
  bucket = aws_s3_bucket.research_data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "research_data" {
  bucket = aws_s3_bucket.research_data.id

  versioning_configuration {
    status = "Enabled"
  }
}
