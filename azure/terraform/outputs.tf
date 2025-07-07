output "resource_group_name" {
  value = azurerm_resource_group.security.name
}

output "log_analytics_workspace_id" {
  value = azurerm_log_analytics_workspace.main.id
} 