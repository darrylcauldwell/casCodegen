# swagger_client.NetworkProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_profile**](NetworkProfileApi.md#create_network_profile) | **POST** /iaas/api/network-profiles | Create network profile
[**delete_network_profile**](NetworkProfileApi.md#delete_network_profile) | **DELETE** /iaas/api/network-profiles/{id} | Delete network profile
[**get_network_profile**](NetworkProfileApi.md#get_network_profile) | **GET** /iaas/api/network-profiles/{id} | Get network profile
[**get_network_profiles**](NetworkProfileApi.md#get_network_profiles) | **GET** /iaas/api/network-profiles | Get network profiles
[**update_network_profile**](NetworkProfileApi.md#update_network_profile) | **PATCH** /iaas/api/network-profiles/{id} | Update network profile

# **create_network_profile**
> NetworkProfile create_network_profile(body, api_version=api_version)

Create network profile

Create network profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkProfileApi()
body = swagger_client.NetworkProfileSpecification() # NetworkProfileSpecification | NetworkProfile instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create network profile
    api_response = api_instance.create_network_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkProfileApi->create_network_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkProfileSpecification**](NetworkProfileSpecification.md)| NetworkProfile instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkProfile**](NetworkProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_profile**
> delete_network_profile(id, api_version=api_version)

Delete network profile

Delete network profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkProfileApi()
id = 'id_example' # str | The ID of the network profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete network profile
    api_instance.delete_network_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling NetworkProfileApi->delete_network_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the network profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profile**
> NetworkProfile get_network_profile(id, api_version=api_version)

Get network profile

Get network profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkProfileApi()
id = 'id_example' # str | The ID of the network profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get network profile
    api_response = api_instance.get_network_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkProfileApi->get_network_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the network profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkProfile**](NetworkProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profiles**
> NetworkProfileResult get_network_profiles(api_version=api_version)

Get network profiles

Get all network profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get network profiles
    api_response = api_instance.get_network_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkProfileApi->get_network_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkProfileResult**](NetworkProfileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_profile**
> NetworkProfile update_network_profile(body, id, api_version=api_version)

Update network profile

Update network profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkProfileApi()
body = swagger_client.NetworkProfileSpecification() # NetworkProfileSpecification | NetworkProfile specification
id = 'id_example' # str | The ID of the network profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update network profile
    api_response = api_instance.update_network_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkProfileApi->update_network_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkProfileSpecification**](NetworkProfileSpecification.md)| NetworkProfile specification | 
 **id** | **str**| The ID of the network profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkProfile**](NetworkProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

