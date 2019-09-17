# swagger_client.FabricAzureStorageAccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_azure_storage_account**](FabricAzureStorageAccountApi.md#get_fabric_azure_storage_account) | **GET** /iaas/api/fabric-azure-storage-accounts/{id} | Get fabric Azure storage account
[**get_fabric_azure_storage_accounts**](FabricAzureStorageAccountApi.md#get_fabric_azure_storage_accounts) | **GET** /iaas/api/fabric-azure-storage-accounts | Get fabric Azure storage accounts

# **get_fabric_azure_storage_account**
> FabricAzureStorageAccount get_fabric_azure_storage_account(id, api_version=api_version)

Get fabric Azure storage account

Get fabric Azure storage account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricAzureStorageAccountApi()
id = 'id_example' # str | The ID of the Fabric Azure Storage Account.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric Azure storage account
    api_response = api_instance.get_fabric_azure_storage_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricAzureStorageAccountApi->get_fabric_azure_storage_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Fabric Azure Storage Account. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricAzureStorageAccount**](FabricAzureStorageAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_azure_storage_accounts**
> FabricAzureStorageAccountResult get_fabric_azure_storage_accounts(api_version=api_version)

Get fabric Azure storage accounts

Get all fabric Azure storage accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricAzureStorageAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric Azure storage accounts
    api_response = api_instance.get_fabric_azure_storage_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricAzureStorageAccountApi->get_fabric_azure_storage_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricAzureStorageAccountResult**](FabricAzureStorageAccountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

