# swagger_client.CloudAccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_cloud_account**](CloudAccountApi.md#create_aws_cloud_account) | **POST** /iaas/api/cloud-accounts-aws | Create an AWS cloud account
[**create_azure_cloud_account**](CloudAccountApi.md#create_azure_cloud_account) | **POST** /iaas/api/cloud-accounts-azure | Create an Azure cloud account
[**create_cloud_account**](CloudAccountApi.md#create_cloud_account) | **POST** /iaas/api/cloud-accounts | Create a cloud account
[**create_gcp_cloud_account**](CloudAccountApi.md#create_gcp_cloud_account) | **POST** /iaas/api/cloud-accounts-gcp | Create an GCP cloud account
[**create_nsx_t_cloud_account**](CloudAccountApi.md#create_nsx_t_cloud_account) | **POST** /iaas/api/cloud-accounts-nsx-t | Create a NSX-T cloud account
[**create_nsx_v_cloud_account**](CloudAccountApi.md#create_nsx_v_cloud_account) | **POST** /iaas/api/cloud-accounts-nsx-v | Create a NSX-V cloud account
[**create_v_sphere_cloud_account**](CloudAccountApi.md#create_v_sphere_cloud_account) | **POST** /iaas/api/cloud-accounts-vsphere | Create a vSphere cloud account
[**delete_aws_cloud_account**](CloudAccountApi.md#delete_aws_cloud_account) | **DELETE** /iaas/api/cloud-accounts-aws/{id} | Delete an AWS cloud account
[**delete_azure_cloud_account**](CloudAccountApi.md#delete_azure_cloud_account) | **DELETE** /iaas/api/cloud-accounts-azure/{id} | Delete an Azure Cloud Account
[**delete_cloud_account**](CloudAccountApi.md#delete_cloud_account) | **DELETE** /iaas/api/cloud-accounts/{id} | Delete a cloud account
[**delete_cloud_account_nsx_t**](CloudAccountApi.md#delete_cloud_account_nsx_t) | **DELETE** /iaas/api/cloud-accounts-nsx-t/{id} | Delete a NSX-T cloud account
[**delete_cloud_account_nsx_v**](CloudAccountApi.md#delete_cloud_account_nsx_v) | **DELETE** /iaas/api/cloud-accounts-nsx-v/{id} | Delete a NSV-V cloud account
[**delete_gcp_cloud_account**](CloudAccountApi.md#delete_gcp_cloud_account) | **DELETE** /iaas/api/cloud-accounts-gcp/{id} | Delete an GCP cloud account
[**delete_v_sphere_cloud_account**](CloudAccountApi.md#delete_v_sphere_cloud_account) | **DELETE** /iaas/api/cloud-accounts-vsphere/{id} | Delete a vSphere cloud account
[**enumerate_aws_regions**](CloudAccountApi.md#enumerate_aws_regions) | **POST** /iaas/api/cloud-accounts-aws/region-enumeration | Get the available regions for specified AWS cloud account
[**enumerate_azure_regions**](CloudAccountApi.md#enumerate_azure_regions) | **POST** /iaas/api/cloud-accounts-azure/region-enumeration | Get the available regions for specified Azure cloud account
[**enumerate_gcp_regions**](CloudAccountApi.md#enumerate_gcp_regions) | **POST** /iaas/api/cloud-accounts-gcp/region-enumeration | Get the available regions for specified GCP cloud account
[**enumerate_regions**](CloudAccountApi.md#enumerate_regions) | **POST** /iaas/api/cloud-accounts/region-enumeration | Get the available regions for specified cloud account
[**enumerate_v_sphere_regions**](CloudAccountApi.md#enumerate_v_sphere_regions) | **POST** /iaas/api/cloud-accounts-vsphere/region-enumeration | Get the available regions for specified vSphere cloud account
[**get_aws_cloud_account**](CloudAccountApi.md#get_aws_cloud_account) | **GET** /iaas/api/cloud-accounts-aws/{id} | Get an AWS cloud account
[**get_aws_cloud_accounts**](CloudAccountApi.md#get_aws_cloud_accounts) | **GET** /iaas/api/cloud-accounts-aws | Get AWS cloud accounts
[**get_azure_cloud_account**](CloudAccountApi.md#get_azure_cloud_account) | **GET** /iaas/api/cloud-accounts-azure/{id} | Get an Azure Cloud Account
[**get_azure_cloud_accounts**](CloudAccountApi.md#get_azure_cloud_accounts) | **GET** /iaas/api/cloud-accounts-azure | Get Azure cloud accounts
[**get_cloud_account**](CloudAccountApi.md#get_cloud_account) | **GET** /iaas/api/cloud-accounts/{id} | Get cloud account
[**get_cloud_accounts**](CloudAccountApi.md#get_cloud_accounts) | **GET** /iaas/api/cloud-accounts | Get cloud accounts
[**get_gcp_cloud_account**](CloudAccountApi.md#get_gcp_cloud_account) | **GET** /iaas/api/cloud-accounts-gcp/{id} | Get an GCP cloud account
[**get_gcp_cloud_accounts**](CloudAccountApi.md#get_gcp_cloud_accounts) | **GET** /iaas/api/cloud-accounts-gcp | Get GCP cloud accounts
[**get_nsx_t_cloud_account**](CloudAccountApi.md#get_nsx_t_cloud_account) | **GET** /iaas/api/cloud-accounts-nsx-t/{id} | Get an NSX-T cloud account
[**get_nsx_t_cloud_accounts**](CloudAccountApi.md#get_nsx_t_cloud_accounts) | **GET** /iaas/api/cloud-accounts-nsx-t | Get NSX-T cloud accounts
[**get_nsx_v_cloud_account**](CloudAccountApi.md#get_nsx_v_cloud_account) | **GET** /iaas/api/cloud-accounts-nsx-v/{id} | Get an NSX-V cloud account
[**get_nsx_v_cloud_accounts**](CloudAccountApi.md#get_nsx_v_cloud_accounts) | **GET** /iaas/api/cloud-accounts-nsx-v | Get NSX-V cloud accounts
[**get_v_sphere_cloud_account**](CloudAccountApi.md#get_v_sphere_cloud_account) | **GET** /iaas/api/cloud-accounts-vsphere/{id} | Get an vSphere cloud account
[**get_v_sphere_cloud_accounts**](CloudAccountApi.md#get_v_sphere_cloud_accounts) | **GET** /iaas/api/cloud-accounts-vsphere | Get vSphere cloud accounts
[**update_aws_cloud_account**](CloudAccountApi.md#update_aws_cloud_account) | **PATCH** /iaas/api/cloud-accounts-aws/{id} | Update AWS cloud account
[**update_azure_cloud_account**](CloudAccountApi.md#update_azure_cloud_account) | **PATCH** /iaas/api/cloud-accounts-azure/{id} | Update Azure cloud account
[**update_cloud_account**](CloudAccountApi.md#update_cloud_account) | **PATCH** /iaas/api/cloud-accounts/{id} | Update CloudAccount
[**update_gcp_cloud_account**](CloudAccountApi.md#update_gcp_cloud_account) | **PATCH** /iaas/api/cloud-accounts-gcp/{id} | Update GCP cloud account
[**update_nsx_t_cloud_account**](CloudAccountApi.md#update_nsx_t_cloud_account) | **PATCH** /iaas/api/cloud-accounts-nsx-t/{id} | Update NSX-T cloud account
[**update_nsx_v_cloud_account**](CloudAccountApi.md#update_nsx_v_cloud_account) | **PATCH** /iaas/api/cloud-accounts-nsx-v/{id} | Update NSX-V cloud account
[**update_v_sphere_cloud_account**](CloudAccountApi.md#update_v_sphere_cloud_account) | **PATCH** /iaas/api/cloud-accounts-vsphere/{id} | Update vSphere cloud account

# **create_aws_cloud_account**
> CloudAccountAws create_aws_cloud_account(body, api_version=api_version)

Create an AWS cloud account

Create an AWS cloud account in the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountAwsSpecification() # CloudAccountAwsSpecification | CloudAccountAws specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create an AWS cloud account
    api_response = api_instance.create_aws_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_aws_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountAwsSpecification**](CloudAccountAwsSpecification.md)| CloudAccountAws specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAws**](CloudAccountAws.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_cloud_account**
> CloudAccountAzure create_azure_cloud_account(body, api_version=api_version)

Create an Azure cloud account

Create an Azure cloud account in the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountAzureSpecification() # CloudAccountAzureSpecification | CloudAccountAzure specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create an Azure cloud account
    api_response = api_instance.create_azure_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_azure_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountAzureSpecification**](CloudAccountAzureSpecification.md)| CloudAccountAzure specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAzure**](CloudAccountAzure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_account**
> CloudAccount create_cloud_account(body, api_version=api_version)

Create a cloud account

Create a cloud account in the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountSpecification() # CloudAccountSpecification | CloudAccount instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create a cloud account
    api_response = api_instance.create_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountSpecification**](CloudAccountSpecification.md)| CloudAccount instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccount**](CloudAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_cloud_account**
> CloudAccountGcp create_gcp_cloud_account(body, api_version=api_version)

Create an GCP cloud account

Create an GCP cloud account in the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountGcpSpecification() # CloudAccountGcpSpecification | CloudAccountGcp specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create an GCP cloud account
    api_response = api_instance.create_gcp_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_gcp_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountGcpSpecification**](CloudAccountGcpSpecification.md)| CloudAccountGcp specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountGcp**](CloudAccountGcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_t_cloud_account**
> CloudAccountNsxT create_nsx_t_cloud_account(body, api_version=api_version)

Create a NSX-T cloud account

Create a NSX-T cloud account in the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountNsxTSpecification() # CloudAccountNsxTSpecification | CloudAccountNsxT specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create a NSX-T cloud account
    api_response = api_instance.create_nsx_t_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_nsx_t_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountNsxTSpecification**](CloudAccountNsxTSpecification.md)| CloudAccountNsxT specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxT**](CloudAccountNsxT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_v_cloud_account**
> CloudAccountNsxV create_nsx_v_cloud_account(body, api_version=api_version)

Create a NSX-V cloud account

Create a NSX-V cloud account within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountNsxVSpecification() # CloudAccountNsxVSpecification | CloudAccountNsxV specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create a NSX-V cloud account
    api_response = api_instance.create_nsx_v_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_nsx_v_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountNsxVSpecification**](CloudAccountNsxVSpecification.md)| CloudAccountNsxV specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxV**](CloudAccountNsxV.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_v_sphere_cloud_account**
> CloudAccountVsphere create_v_sphere_cloud_account(body, api_version=api_version)

Create a vSphere cloud account

Create a vSphere cloud account within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountVsphereSpecification() # CloudAccountVsphereSpecification | CloudAccountVsphere specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create a vSphere cloud account
    api_response = api_instance.create_v_sphere_cloud_account(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->create_v_sphere_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountVsphereSpecification**](CloudAccountVsphereSpecification.md)| CloudAccountVsphere specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountVsphere**](CloudAccountVsphere.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_cloud_account**
> delete_aws_cloud_account(id, api_version=api_version)

Delete an AWS cloud account

Delete an AWS cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete an AWS cloud account
    api_instance.delete_aws_cloud_account(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_aws_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_cloud_account**
> delete_azure_cloud_account(id, api_version=api_version)

Delete an Azure Cloud Account

Delete an Azure Cloud Account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete an Azure Cloud Account
    api_instance.delete_azure_cloud_account(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_azure_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account**
> delete_cloud_account(id, api_version=api_version)

Delete a cloud account

Delete a cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a cloud account
    api_instance.delete_cloud_account(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account_nsx_t**
> delete_cloud_account_nsx_t(id, api_version=api_version)

Delete a NSX-T cloud account

Delete a NSX-T cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a NSX-T cloud account
    api_instance.delete_cloud_account_nsx_t(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_cloud_account_nsx_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account_nsx_v**
> delete_cloud_account_nsx_v(id, api_version=api_version)

Delete a NSV-V cloud account

Delete a NSV-V cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a NSV-V cloud account
    api_instance.delete_cloud_account_nsx_v(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_cloud_account_nsx_v: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gcp_cloud_account**
> delete_gcp_cloud_account(id, api_version=api_version)

Delete an GCP cloud account

Delete an GCP cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete an GCP cloud account
    api_instance.delete_gcp_cloud_account(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_gcp_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v_sphere_cloud_account**
> delete_v_sphere_cloud_account(id, api_version=api_version)

Delete a vSphere cloud account

Delete a vSphere Cloud Account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a vSphere cloud account
    api_instance.delete_v_sphere_cloud_account(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling CloudAccountApi->delete_v_sphere_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_aws_regions**
> CloudAccountRegions enumerate_aws_regions(body, api_version=api_version)

Get the available regions for specified AWS cloud account

Get the available regions for specified AWS cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountAwsSpecification() # CloudAccountAwsSpecification | CloudAccount specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get the available regions for specified AWS cloud account
    api_response = api_instance.enumerate_aws_regions(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->enumerate_aws_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountAwsSpecification**](CloudAccountAwsSpecification.md)| CloudAccount specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountRegions**](CloudAccountRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_azure_regions**
> CloudAccountRegions enumerate_azure_regions(body, api_version=api_version)

Get the available regions for specified Azure cloud account

Get the available regions for specified Azure cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountAzureSpecification() # CloudAccountAzureSpecification | CloudAccountAzure specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get the available regions for specified Azure cloud account
    api_response = api_instance.enumerate_azure_regions(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->enumerate_azure_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountAzureSpecification**](CloudAccountAzureSpecification.md)| CloudAccountAzure specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountRegions**](CloudAccountRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_gcp_regions**
> CloudAccountRegions enumerate_gcp_regions(body, api_version=api_version)

Get the available regions for specified GCP cloud account

Get the available regions for specified GCP cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountGcpSpecification() # CloudAccountGcpSpecification | CloudAccount specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get the available regions for specified GCP cloud account
    api_response = api_instance.enumerate_gcp_regions(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->enumerate_gcp_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountGcpSpecification**](CloudAccountGcpSpecification.md)| CloudAccount specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountRegions**](CloudAccountRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_regions**
> CloudAccountRegions enumerate_regions(body, api_version=api_version)

Get the available regions for specified cloud account

Get the available regions for specified cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountSpecification() # CloudAccountSpecification | CloudAccount instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get the available regions for specified cloud account
    api_response = api_instance.enumerate_regions(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->enumerate_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountSpecification**](CloudAccountSpecification.md)| CloudAccount instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountRegions**](CloudAccountRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enumerate_v_sphere_regions**
> CloudAccountRegions enumerate_v_sphere_regions(body, api_version=api_version)

Get the available regions for specified vSphere cloud account

Get the available regions for specified vSphere cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.CloudAccountVsphereSpecification() # CloudAccountVsphereSpecification | CloudAccountVsphere specification
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get the available regions for specified vSphere cloud account
    api_response = api_instance.enumerate_v_sphere_regions(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->enumerate_v_sphere_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudAccountVsphereSpecification**](CloudAccountVsphereSpecification.md)| CloudAccountVsphere specification | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountRegions**](CloudAccountRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_cloud_account**
> CloudAccountAws get_aws_cloud_account(id, api_version=api_version)

Get an AWS cloud account

Get an AWS cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an AWS cloud account
    api_response = api_instance.get_aws_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_aws_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAws**](CloudAccountAws.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_cloud_accounts**
> CloudAccountAwsResult get_aws_cloud_accounts(api_version=api_version)

Get AWS cloud accounts

Get all AWS cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get AWS cloud accounts
    api_response = api_instance.get_aws_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_aws_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAwsResult**](CloudAccountAwsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_cloud_account**
> CloudAccountAzure get_azure_cloud_account(id, api_version=api_version)

Get an Azure Cloud Account

Get an Azure Cloud Account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an Azure Cloud Account
    api_response = api_instance.get_azure_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_azure_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAzure**](CloudAccountAzure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_cloud_accounts**
> CloudAccountAzureResult get_azure_cloud_accounts(api_version=api_version)

Get Azure cloud accounts

Get all Azure cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get Azure cloud accounts
    api_response = api_instance.get_azure_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_azure_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAzureResult**](CloudAccountAzureResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_account**
> CloudAccount get_cloud_account(id, api_version=api_version)

Get cloud account

Get cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get cloud account
    api_response = api_instance.get_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccount**](CloudAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_accounts**
> CloudAccountResult get_cloud_accounts(api_version=api_version)

Get cloud accounts

Get all cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get cloud accounts
    api_response = api_instance.get_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountResult**](CloudAccountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_cloud_account**
> CloudAccountGcp get_gcp_cloud_account(id, api_version=api_version)

Get an GCP cloud account

Get an GCP cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an GCP cloud account
    api_response = api_instance.get_gcp_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_gcp_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountGcp**](CloudAccountGcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_cloud_accounts**
> CloudAccountGcpResult get_gcp_cloud_accounts(api_version=api_version)

Get GCP cloud accounts

Get all GCP cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get GCP cloud accounts
    api_response = api_instance.get_gcp_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_gcp_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountGcpResult**](CloudAccountGcpResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsx_t_cloud_account**
> CloudAccountNsxT get_nsx_t_cloud_account(id, api_version=api_version)

Get an NSX-T cloud account

Get an NSX-T cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an NSX-T cloud account
    api_response = api_instance.get_nsx_t_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_nsx_t_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxT**](CloudAccountNsxT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsx_t_cloud_accounts**
> CloudAccountNsxTResult get_nsx_t_cloud_accounts(api_version=api_version)

Get NSX-T cloud accounts

Get all NSX-T cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get NSX-T cloud accounts
    api_response = api_instance.get_nsx_t_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_nsx_t_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxTResult**](CloudAccountNsxTResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsx_v_cloud_account**
> CloudAccountNsxV get_nsx_v_cloud_account(id, api_version=api_version)

Get an NSX-V cloud account

Get an NSX-V cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an NSX-V cloud account
    api_response = api_instance.get_nsx_v_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_nsx_v_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxV**](CloudAccountNsxV.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nsx_v_cloud_accounts**
> CloudAccountNsxVResult get_nsx_v_cloud_accounts(api_version=api_version)

Get NSX-V cloud accounts

Get all NSX-V cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get NSX-V cloud accounts
    api_response = api_instance.get_nsx_v_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_nsx_v_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxVResult**](CloudAccountNsxVResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v_sphere_cloud_account**
> CloudAccountVsphere get_v_sphere_cloud_account(id, api_version=api_version)

Get an vSphere cloud account

Get an vSphere cloud account with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
id = 'id_example' # str | The ID of the Cloud Account
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get an vSphere cloud account
    api_response = api_instance.get_v_sphere_cloud_account(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_v_sphere_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud Account | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountVsphere**](CloudAccountVsphere.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v_sphere_cloud_accounts**
> CloudAccountVsphereResult get_v_sphere_cloud_accounts(api_version=api_version)

Get vSphere cloud accounts

Get all vSphere cloud accounts within the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get vSphere cloud accounts
    api_response = api_instance.get_v_sphere_cloud_accounts(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->get_v_sphere_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountVsphereResult**](CloudAccountVsphereResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_cloud_account**
> CloudAccountAws update_aws_cloud_account(body, id, api_version=api_version)

Update AWS cloud account

Update AWS cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountAwsSpecification() # UpdateCloudAccountAwsSpecification | AWS cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update AWS cloud account
    api_response = api_instance.update_aws_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_aws_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountAwsSpecification**](UpdateCloudAccountAwsSpecification.md)| AWS cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAws**](CloudAccountAws.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_cloud_account**
> CloudAccountAzure update_azure_cloud_account(body, id, api_version=api_version)

Update Azure cloud account

Update Azure cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountAzureSpecification() # UpdateCloudAccountAzureSpecification | Azure cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update Azure cloud account
    api_response = api_instance.update_azure_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_azure_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountAzureSpecification**](UpdateCloudAccountAzureSpecification.md)| Azure cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountAzure**](CloudAccountAzure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_account**
> CloudAccount update_cloud_account(body, id, api_version=api_version)

Update CloudAccount

Update a single CloudAccount

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountSpecification() # UpdateCloudAccountSpecification | Cloud account details to be updated
id = 'id_example' # str | The ID of the cloudAccount
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update CloudAccount
    api_response = api_instance.update_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountSpecification**](UpdateCloudAccountSpecification.md)| Cloud account details to be updated | 
 **id** | **str**| The ID of the cloudAccount | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccount**](CloudAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_cloud_account**
> CloudAccountGcp update_gcp_cloud_account(body, id, api_version=api_version)

Update GCP cloud account

Update GCP cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountGcpSpecification() # UpdateCloudAccountGcpSpecification | GCP cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update GCP cloud account
    api_response = api_instance.update_gcp_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_gcp_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountGcpSpecification**](UpdateCloudAccountGcpSpecification.md)| GCP cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountGcp**](CloudAccountGcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nsx_t_cloud_account**
> CloudAccountNsxT update_nsx_t_cloud_account(body, id, api_version=api_version)

Update NSX-T cloud account

Update NSX-T cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountSpecificationBase() # UpdateCloudAccountSpecificationBase | NSX-T cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update NSX-T cloud account
    api_response = api_instance.update_nsx_t_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_nsx_t_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountSpecificationBase**](UpdateCloudAccountSpecificationBase.md)| NSX-T cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxT**](CloudAccountNsxT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nsx_v_cloud_account**
> CloudAccountNsxV update_nsx_v_cloud_account(body, id, api_version=api_version)

Update NSX-V cloud account

Update NSX-V cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountSpecificationBase() # UpdateCloudAccountSpecificationBase | NSX-V cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update NSX-V cloud account
    api_response = api_instance.update_nsx_v_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_nsx_v_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountSpecificationBase**](UpdateCloudAccountSpecificationBase.md)| NSX-V cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountNsxV**](CloudAccountNsxV.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_v_sphere_cloud_account**
> CloudAccountVsphere update_v_sphere_cloud_account(body, id, api_version=api_version)

Update vSphere cloud account

Update vSphere cloud account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudAccountApi()
body = swagger_client.UpdateCloudAccountVsphereSpecification() # UpdateCloudAccountVsphereSpecification | VSphere cloud account details to be updated
id = 'id_example' # str | Cloud account id
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update vSphere cloud account
    api_response = api_instance.update_v_sphere_cloud_account(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudAccountApi->update_v_sphere_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCloudAccountVsphereSpecification**](UpdateCloudAccountVsphereSpecification.md)| VSphere cloud account details to be updated | 
 **id** | **str**| Cloud account id | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**CloudAccountVsphere**](CloudAccountVsphere.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

