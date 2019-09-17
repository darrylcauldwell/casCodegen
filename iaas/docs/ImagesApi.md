# swagger_client.ImagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images**](ImagesApi.md#get_images) | **GET** /iaas/api/images | Get images

# **get_images**
> ImageResult get_images(api_version=api_version)

Get images

Get all images defined in ImageProfile.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get images
    api_response = api_instance.get_images(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ImageResult**](ImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

