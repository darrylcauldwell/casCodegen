# swagger_client.FlavorProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flavor_profile**](FlavorProfileApi.md#create_flavor_profile) | **POST** /iaas/api/flavor-profiles | Create flavor profile
[**delete_flavor_profile**](FlavorProfileApi.md#delete_flavor_profile) | **DELETE** /iaas/api/flavor-profiles/{id} | Delete flavor profile
[**get_flavor_profile**](FlavorProfileApi.md#get_flavor_profile) | **GET** /iaas/api/flavor-profiles/{id} | Get flavor profile
[**get_flavor_profiles**](FlavorProfileApi.md#get_flavor_profiles) | **GET** /iaas/api/flavor-profiles | Get flavor profile
[**update_flavor_profile**](FlavorProfileApi.md#update_flavor_profile) | **PATCH** /iaas/api/flavor-profiles/{id} | Update flavor profile

# **create_flavor_profile**
> FlavorProfile create_flavor_profile(body, api_version=api_version)

Create flavor profile

Create flavor profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorProfileApi()
body = swagger_client.FlavorProfileSpecification() # FlavorProfileSpecification | FlavorProfile instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create flavor profile
    api_response = api_instance.create_flavor_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlavorProfileApi->create_flavor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlavorProfileSpecification**](FlavorProfileSpecification.md)| FlavorProfile instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FlavorProfile**](FlavorProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flavor_profile**
> delete_flavor_profile(id, api_version=api_version)

Delete flavor profile

Delete flavor profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorProfileApi()
id = 'id_example' # str | The ID of the flavor.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete flavor profile
    api_instance.delete_flavor_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling FlavorProfileApi->delete_flavor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the flavor. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flavor_profile**
> FlavorProfile get_flavor_profile(id, api_version=api_version)

Get flavor profile

Get flavor profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorProfileApi()
id = 'id_example' # str | The ID of the flavor.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get flavor profile
    api_response = api_instance.get_flavor_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlavorProfileApi->get_flavor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the flavor. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FlavorProfile**](FlavorProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flavor_profiles**
> FlavorProfileResult get_flavor_profiles(api_version=api_version)

Get flavor profile

Get all flavor profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get flavor profile
    api_response = api_instance.get_flavor_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlavorProfileApi->get_flavor_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FlavorProfileResult**](FlavorProfileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flavor_profile**
> FlavorProfile update_flavor_profile(body, id, api_version=api_version)

Update flavor profile

Update flavor profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlavorProfileApi()
body = swagger_client.FlavorProfileSpecification() # FlavorProfileSpecification | FlavorProfile instance
id = 'id_example' # str | The ID of the flavor.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update flavor profile
    api_response = api_instance.update_flavor_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlavorProfileApi->update_flavor_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlavorProfileSpecification**](FlavorProfileSpecification.md)| FlavorProfile instance | 
 **id** | **str**| The ID of the flavor. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FlavorProfile**](FlavorProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

