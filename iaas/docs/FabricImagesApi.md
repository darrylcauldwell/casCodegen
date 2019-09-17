# swagger_client.FabricImagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_image**](FabricImagesApi.md#get_fabric_image) | **GET** /iaas/api/fabric-images/{id} | Get fabric image
[**get_fabric_images**](FabricImagesApi.md#get_fabric_images) | **GET** /iaas/api/fabric-images | Get fabric images

# **get_fabric_image**
> FabricImage get_fabric_image(id, api_version=api_version)

Get fabric image

Get fabric image with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricImagesApi()
id = 'id_example' # str | The ID of the image.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric image
    api_response = api_instance.get_fabric_image(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricImagesApi->get_fabric_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the image. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricImage**](FabricImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_images**
> FabricImageResult get_fabric_images(api_version=api_version)

Get fabric images

Get all fabric images

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricImagesApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric images
    api_response = api_instance.get_fabric_images(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricImagesApi->get_fabric_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricImageResult**](FabricImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

