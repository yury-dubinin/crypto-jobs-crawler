resource "azurerm_resource_group" "rg" {
  location = "northeurope"
  name     = "web-page-rg"
}

resource "azurerm_storage_account" "example" {
  name                     = "mywebstorageaccount01"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = "northeurope"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  enable_https_traffic_only = true

  static_website {
    index_document = "index.html"
  }
}

resource "azurerm_storage_container" "example" {
  name                  = "mywebcontainer01"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "blob"
}

resource "azurerm_storage_blob" "index-file" {
  name                   = "index.html"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = azurerm_storage_container.example.name
  type                   = "Block"
  source                 = "index.html"
}

resource "azurerm_storage_blob" "error-file" {
  name                   = "404.html"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = azurerm_storage_container.example.name
  type                   = "Block"
  source                 = "404.html"
}
