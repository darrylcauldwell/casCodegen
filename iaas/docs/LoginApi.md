# swagger_client.LoginApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_auth_token**](LoginApi.md#retrieve_auth_token) | **POST** /iaas/api/login | Retrieve AuthToken for local csp users

# **retrieve_auth_token**
> AuthResponse retrieve_auth_token(body, api_version=api_version)

Retrieve AuthToken for local csp users

Retrieve AuthToken for local csp users. When accessing other endpoints the `Bearer` authentication scheme and the received `token` must be provided in the `Authorization` request header field as follows: `Authorization: Bearer {token}`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
body = swagger_client.CspLoginSpecification() # CspLoginSpecification | CspLoginSpecification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Retrieve AuthToken for local csp users
    api_response = api_instance.retrieve_auth_token(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->retrieve_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CspLoginSpecification**](CspLoginSpecification.md)| CspLoginSpecification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

