provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "security" {
  name     = "multi-cloud-security-rg"
  location = var.location
}

resource "azurerm_log_analytics_workspace" "main" {
  name                = "mcsec-law"
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_security_center_subscription_pricing" "defender" {
  tier          = "Standard"
  resource_type = "VirtualMachines"
} 