# swagger_client.ImageProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_profile**](ImageProfileApi.md#create_image_profile) | **POST** /iaas/api/image-profiles | Create image profile
[**delete_image_profile**](ImageProfileApi.md#delete_image_profile) | **DELETE** /iaas/api/image-profiles/{id} | Delete image profile
[**get_image_profile**](ImageProfileApi.md#get_image_profile) | **GET** /iaas/api/image-profiles/{id} | Get image profile
[**get_image_profiles**](ImageProfileApi.md#get_image_profiles) | **GET** /iaas/api/image-profiles | Get image profile
[**update_image_profile**](ImageProfileApi.md#update_image_profile) | **PATCH** /iaas/api/image-profiles/{id} | Update image profile

# **create_image_profile**
> ImageProfile create_image_profile(body, api_version=api_version)

Create image profile

Create image profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageProfileApi()
body = swagger_client.ImageProfileSpecification() # ImageProfileSpecification | ImageProfile instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create image profile
    api_response = api_instance.create_image_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageProfileApi->create_image_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageProfileSpecification**](ImageProfileSpecification.md)| ImageProfile instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ImageProfile**](ImageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_profile**
> delete_image_profile(id, api_version=api_version)

Delete image profile

Delete image profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageProfileApi()
id = 'id_example' # str | The ID of the image.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete image profile
    api_instance.delete_image_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling ImageProfileApi->delete_image_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the image. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_profile**
> ImageProfile get_image_profile(id, api_version=api_version)

Get image profile

Get image profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageProfileApi()
id = 'id_example' # str | The ID of the image.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get image profile
    api_response = api_instance.get_image_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageProfileApi->get_image_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the image. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ImageProfile**](ImageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_profiles**
> ImageProfileResult get_image_profiles(api_version=api_version)

Get image profile

Get all image profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get image profile
    api_response = api_instance.get_image_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageProfileApi->get_image_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ImageProfileResult**](ImageProfileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image_profile**
> ImageProfile update_image_profile(body, id, api_version=api_version)

Update image profile

Update image profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageProfileApi()
body = swagger_client.ImageProfileSpecification() # ImageProfileSpecification | ImageProfile instance
id = 'id_example' # str | The ID of the image.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update image profile
    api_response = api_instance.update_image_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageProfileApi->update_image_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageProfileSpecification**](ImageProfileSpecification.md)| ImageProfile instance | 
 **id** | **str**| The ID of the image. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ImageProfile**](ImageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

