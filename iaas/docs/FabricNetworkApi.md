# swagger_client.FabricNetworkApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_network**](FabricNetworkApi.md#get_fabric_network) | **GET** /iaas/api/fabric-networks/{id} | Get fabric network
[**get_fabric_networks**](FabricNetworkApi.md#get_fabric_networks) | **GET** /iaas/api/fabric-networks | Get fabric networks
[**update_fabric_network**](FabricNetworkApi.md#update_fabric_network) | **PATCH** /iaas/api/fabric-networks/{id} | Update fabric network.

# **get_fabric_network**
> FabricNetwork get_fabric_network(id, api_version=api_version)

Get fabric network

Get fabric network with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricNetworkApi()
id = 'id_example' # str | The ID of the fabric network.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric network
    api_response = api_instance.get_fabric_network(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricNetworkApi->get_fabric_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the fabric network. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricNetwork**](FabricNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_networks**
> FabricNetworkResult get_fabric_networks(api_version=api_version)

Get fabric networks

Get all fabric networks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricNetworkApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric networks
    api_response = api_instance.get_fabric_networks(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricNetworkApi->get_fabric_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricNetworkResult**](FabricNetworkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fabric_network**
> FabricNetwork update_fabric_network(body, id, api_version=api_version)

Update fabric network.

Update fabric network. Only tag updates are supported.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricNetworkApi()
body = swagger_client.FabricNetworkSpecification() # FabricNetworkSpecification | Fabric Network Specification
id = 'id_example' # str | The ID of the Fabric Network.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update fabric network.
    api_response = api_instance.update_fabric_network(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricNetworkApi->update_fabric_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FabricNetworkSpecification**](FabricNetworkSpecification.md)| Fabric Network Specification | 
 **id** | **str**| The ID of the Fabric Network. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricNetwork**](FabricNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

