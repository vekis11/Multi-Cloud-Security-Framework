provider "google" {
  project = var.project
  region  = var.region
}

resource "google_project_service" "securitycenter" {
  service = "securitycenter.googleapis.com"
}

resource "google_project_service" "logging" {
  service = "logging.googleapis.com"
} 