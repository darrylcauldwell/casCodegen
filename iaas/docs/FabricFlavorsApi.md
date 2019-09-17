# swagger_client.FabricFlavorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_flavors**](FabricFlavorsApi.md#get_fabric_flavors) | **GET** /iaas/api/fabric-flavors | Get fabric flavors

# **get_fabric_flavors**
> FabricFlavorResult get_fabric_flavors(api_version=api_version)

Get fabric flavors

Get all fabric flavors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricFlavorsApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric flavors
    api_response = api_instance.get_fabric_flavors(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricFlavorsApi->get_fabric_flavors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricFlavorResult**](FabricFlavorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

