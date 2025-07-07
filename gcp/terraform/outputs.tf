output "securitycenter_service" {
  value = google_project_service.securitycenter.service
}

output "logging_service" {
  value = google_project_service.logging.service
} 