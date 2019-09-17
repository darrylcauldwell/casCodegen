# swagger_client.SecurityGroupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_group**](SecurityGroupApi.md#get_security_group) | **GET** /iaas/api/security-groups/{id} | Get security group
[**get_security_groups**](SecurityGroupApi.md#get_security_groups) | **GET** /iaas/api/security-groups | Get security groups

# **get_security_group**
> SecurityGroup get_security_group(id, api_version=api_version)

Get security group

Get security group with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityGroupApi()
id = 'id_example' # str | The ID of the security group.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get security group
    api_response = api_instance.get_security_group(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityGroupApi->get_security_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the security group. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**SecurityGroup**](SecurityGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_groups**
> SecurityGroupResult get_security_groups(api_version=api_version)

Get security groups

Get all security groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityGroupApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get security groups
    api_response = api_instance.get_security_groups(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityGroupApi->get_security_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**SecurityGroupResult**](SecurityGroupResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

