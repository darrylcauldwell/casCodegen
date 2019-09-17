# swagger_client.StorageProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_storage_profile**](StorageProfileApi.md#create_aws_storage_profile) | **POST** /iaas/api/storage-profiles-aws | Create AWS storage profile
[**create_azure_storage_profile**](StorageProfileApi.md#create_azure_storage_profile) | **POST** /iaas/api/storage-profiles-azure | Create Azure storage profile
[**create_storage_profile**](StorageProfileApi.md#create_storage_profile) | **POST** /iaas/api/storage-profiles | Create storage profile
[**create_v_sphere_storage_profile**](StorageProfileApi.md#create_v_sphere_storage_profile) | **POST** /iaas/api/storage-profiles-vsphere | Create vSphere storage profile
[**delete_aws_storage_profile**](StorageProfileApi.md#delete_aws_storage_profile) | **DELETE** /iaas/api/storage-profiles-aws/{id} | Delete AWS storage profile
[**delete_azure_storage_profile**](StorageProfileApi.md#delete_azure_storage_profile) | **DELETE** /iaas/api/storage-profiles-azure/{id} | Delete Azure storage profile
[**delete_storage_profile**](StorageProfileApi.md#delete_storage_profile) | **DELETE** /iaas/api/storage-profiles/{id} | Delete storage profile
[**delete_v_sphere_storage_profile**](StorageProfileApi.md#delete_v_sphere_storage_profile) | **DELETE** /iaas/api/storage-profiles-vsphere/{id} | Delete vSphere storage profile
[**get_aws_storage_profile**](StorageProfileApi.md#get_aws_storage_profile) | **GET** /iaas/api/storage-profiles-aws/{id} | Get AWS storage profile
[**get_aws_storage_profiles**](StorageProfileApi.md#get_aws_storage_profiles) | **GET** /iaas/api/storage-profiles-aws | Get AWS storage profiles
[**get_azure_storage_profile**](StorageProfileApi.md#get_azure_storage_profile) | **GET** /iaas/api/storage-profiles-azure/{id} | Get Azure storage profile
[**get_azure_storage_profiles**](StorageProfileApi.md#get_azure_storage_profiles) | **GET** /iaas/api/storage-profiles-azure | Get Azure storage profiles
[**get_storage_profile**](StorageProfileApi.md#get_storage_profile) | **GET** /iaas/api/storage-profiles/{id} | Get storage profile
[**get_storage_profiles**](StorageProfileApi.md#get_storage_profiles) | **GET** /iaas/api/storage-profiles | Get storage profiles
[**get_v_sphere_storage_profile**](StorageProfileApi.md#get_v_sphere_storage_profile) | **GET** /iaas/api/storage-profiles-vsphere/{id} | Get vSphere storage profile
[**get_v_sphere_storage_profiles**](StorageProfileApi.md#get_v_sphere_storage_profiles) | **GET** /iaas/api/storage-profiles-vsphere | Get vSphere storage profiles
[**replace_storage_profile**](StorageProfileApi.md#replace_storage_profile) | **PUT** /iaas/api/storage-profiles/{id} | Replace storage profile
[**update_aws_storage_profile**](StorageProfileApi.md#update_aws_storage_profile) | **PATCH** /iaas/api/storage-profiles-aws/{id} | Update AWS storage profile
[**update_azure_storage_profile**](StorageProfileApi.md#update_azure_storage_profile) | **PATCH** /iaas/api/storage-profiles-azure/{id} | Update Azure storage profile
[**update_v_sphere_storage_profile**](StorageProfileApi.md#update_v_sphere_storage_profile) | **PATCH** /iaas/api/storage-profiles-vsphere/{id} | Update vSphere storage profile

# **create_aws_storage_profile**
> AwsStorageProfile create_aws_storage_profile(body, api_version=api_version)

Create AWS storage profile

Create AWS storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileAwsSpecification() # StorageProfileAwsSpecification | StorageProfileAwsSpecification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create AWS storage profile
    api_response = api_instance.create_aws_storage_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->create_aws_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileAwsSpecification**](StorageProfileAwsSpecification.md)| StorageProfileAwsSpecification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AwsStorageProfile**](AwsStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_storage_profile**
> AzureStorageProfile create_azure_storage_profile(body, api_version=api_version)

Create Azure storage profile

Create Azure storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileAzureSpecification() # StorageProfileAzureSpecification | StorageProfileAzureSpecification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create Azure storage profile
    api_response = api_instance.create_azure_storage_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->create_azure_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileAzureSpecification**](StorageProfileAzureSpecification.md)| StorageProfileAzureSpecification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AzureStorageProfile**](AzureStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storage_profile**
> StorageProfile create_storage_profile(body, api_version=api_version)

Create storage profile

Create storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileSpecification() # StorageProfileSpecification | StorageProfileSpecification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create storage profile
    api_response = api_instance.create_storage_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->create_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileSpecification**](StorageProfileSpecification.md)| StorageProfileSpecification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfile**](StorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_v_sphere_storage_profile**
> VsphereStorageProfile create_v_sphere_storage_profile(body, api_version=api_version)

Create vSphere storage profile

Create vSphere storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileVsphereSpecification() # StorageProfileVsphereSpecification | StorageProfileVsphereSpecification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create vSphere storage profile
    api_response = api_instance.create_v_sphere_storage_profile(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->create_v_sphere_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileVsphereSpecification**](StorageProfileVsphereSpecification.md)| StorageProfileVsphereSpecification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**VsphereStorageProfile**](VsphereStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_storage_profile**
> delete_aws_storage_profile(id, api_version=api_version)

Delete AWS storage profile

Delete AWS storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete AWS storage profile
    api_instance.delete_aws_storage_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling StorageProfileApi->delete_aws_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_storage_profile**
> delete_azure_storage_profile(id, api_version=api_version)

Delete Azure storage profile

Delete Azure storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete Azure storage profile
    api_instance.delete_azure_storage_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling StorageProfileApi->delete_azure_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_profile**
> delete_storage_profile(id, api_version=api_version)

Delete storage profile

Delete storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete storage profile
    api_instance.delete_storage_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling StorageProfileApi->delete_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v_sphere_storage_profile**
> delete_v_sphere_storage_profile(id, api_version=api_version)

Delete vSphere storage profile

Delete vSphere storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete vSphere storage profile
    api_instance.delete_v_sphere_storage_profile(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling StorageProfileApi->delete_v_sphere_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_storage_profile**
> AwsStorageProfile get_aws_storage_profile(id, api_version=api_version)

Get AWS storage profile

Get AWS storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get AWS storage profile
    api_response = api_instance.get_aws_storage_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_aws_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AwsStorageProfile**](AwsStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_storage_profiles**
> StorageProfileAwsResult get_aws_storage_profiles(api_version=api_version)

Get AWS storage profiles

Get all AWS storage profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get AWS storage profiles
    api_response = api_instance.get_aws_storage_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_aws_storage_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfileAwsResult**](StorageProfileAwsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_storage_profile**
> AzureStorageProfile get_azure_storage_profile(id, api_version=api_version)

Get Azure storage profile

Get Azure storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get Azure storage profile
    api_response = api_instance.get_azure_storage_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_azure_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AzureStorageProfile**](AzureStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_storage_profiles**
> StorageProfileAzureResult get_azure_storage_profiles(api_version=api_version)

Get Azure storage profiles

Get all Azure storage profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get Azure storage profiles
    api_response = api_instance.get_azure_storage_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_azure_storage_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfileAzureResult**](StorageProfileAzureResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_profile**
> StorageProfile get_storage_profile(id, api_version=api_version)

Get storage profile

Get storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get storage profile
    api_response = api_instance.get_storage_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfile**](StorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_profiles**
> StorageProfileResult get_storage_profiles(api_version=api_version)

Get storage profiles

Get all storage profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get storage profiles
    api_response = api_instance.get_storage_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_storage_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfileResult**](StorageProfileResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v_sphere_storage_profile**
> VsphereStorageProfile get_v_sphere_storage_profile(id, api_version=api_version)

Get vSphere storage profile

Get vSphere storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
id = 'id_example' # str | The ID of storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get vSphere storage profile
    api_response = api_instance.get_v_sphere_storage_profile(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_v_sphere_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**VsphereStorageProfile**](VsphereStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v_sphere_storage_profiles**
> StorageProfileVsphereResult get_v_sphere_storage_profiles(api_version=api_version)

Get vSphere storage profiles

Get all vSphere storage profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get vSphere storage profiles
    api_response = api_instance.get_v_sphere_storage_profiles(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->get_v_sphere_storage_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfileVsphereResult**](StorageProfileVsphereResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_storage_profile**
> StorageProfile replace_storage_profile(body, id, api_version=api_version)

Replace storage profile

Replace storage profile with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileSpecification() # StorageProfileSpecification | StorageProfileSpecification
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Replace storage profile
    api_response = api_instance.replace_storage_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->replace_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileSpecification**](StorageProfileSpecification.md)| StorageProfileSpecification | 
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**StorageProfile**](StorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_storage_profile**
> AwsStorageProfile update_aws_storage_profile(body, id, api_version=api_version)

Update AWS storage profile

Update AWS storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileAwsSpecification() # StorageProfileAwsSpecification | StorageProfileAwsSpecification
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update AWS storage profile
    api_response = api_instance.update_aws_storage_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->update_aws_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileAwsSpecification**](StorageProfileAwsSpecification.md)| StorageProfileAwsSpecification | 
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AwsStorageProfile**](AwsStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_storage_profile**
> AzureStorageProfile update_azure_storage_profile(body, id, api_version=api_version)

Update Azure storage profile

Update Azure storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileAzureSpecification() # StorageProfileAzureSpecification | StorageProfileAzureSpecification instance
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update Azure storage profile
    api_response = api_instance.update_azure_storage_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->update_azure_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileAzureSpecification**](StorageProfileAzureSpecification.md)| StorageProfileAzureSpecification instance | 
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AzureStorageProfile**](AzureStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_v_sphere_storage_profile**
> VsphereStorageProfile update_v_sphere_storage_profile(body, id, api_version=api_version)

Update vSphere storage profile

Update vSphere storage profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageProfileApi()
body = swagger_client.StorageProfileVsphereSpecification() # StorageProfileVsphereSpecification | StorageProfileVsphereSpecification instance
id = 'id_example' # str | The ID of the storage profile.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update vSphere storage profile
    api_response = api_instance.update_v_sphere_storage_profile(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageProfileApi->update_v_sphere_storage_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageProfileVsphereSpecification**](StorageProfileVsphereSpecification.md)| StorageProfileVsphereSpecification instance | 
 **id** | **str**| The ID of the storage profile. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**VsphereStorageProfile**](VsphereStorageProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

