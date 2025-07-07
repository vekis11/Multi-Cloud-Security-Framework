output "securityhub_account_id" {
  value = aws_securityhub_account.main.id
}

output "guardduty_detector_id" {
  value = aws_guardduty_detector.main.id
}

output "cloudtrail_arn" {
  value = aws_cloudtrail.main.arn
} 