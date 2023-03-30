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
    error_404_document = "404.html"
  }
}

resource "azurerm_storage_blob" "index-file" {
  name                   = "index.html"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = "$web"
  type                   = "Block"
  source                 = "index.html"
}

resource "azurerm_storage_blob" "error-file" {
  name                   = "404.html"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = "$web"
  type                   = "Block"
  source                 = "404.html"
}
