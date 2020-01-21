provider "azurerm" {
  version = "=1.38.0"
}

resource "azurerm_resource_group" "test-group" {
  name = "test-luis"
  location = "South Central US"
}

resource "azurerm_virtual_network" "test-network" {
  name = "test-luis-network"
  resource_group_name = azurerm_resource_group.test-group.name
  location = azurerm_resource_group.test-group.location
  address_space = [
    "10.0.0.0/16"
  ]
}

resource "azurerm_app_service_plan" "test-appservice" {
  name = "test-luis-appserviceplan"
  location = azurerm_resource_group.test-group.location
  resource_group_name = azurerm_resource_group.test-group.name
  kind = "Linux"
  reserved = true

  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "sahn-appservice" {
  name = "test-luis-app-service"
  location = azurerm_resource_group.test-group.location
  resource_group_name = azurerm_resource_group.test-group.name
  app_service_plan_id = azurerm_app_service_plan.test-appservice.id

  site_config {
    python_version = "3.4"
    use_32_bit_worker_process = true
  }
}

# User: eduardoGarza
# Password: n0gpJMZqNvZ5bQyloMo73equX8BThy0q3mfiNb