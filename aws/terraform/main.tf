provider "aws" {
  region = var.region
}

resource "aws_securityhub_account" "main" {}
resource "aws_guardduty_detector" "main" {
  enable = true
}
resource "aws_cloudtrail" "main" {
  name                          = "multi-cloud-security-trail"
  s3_bucket_name                = aws_s3_bucket.trail_bucket.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
}
resource "aws_s3_bucket" "trail_bucket" {
  bucket = "multi-cloud-security-trail-bucket-${random_id.suffix.hex}"
  force_destroy = true
}
resource "random_id" "suffix" {
  byte_length = 4
} 