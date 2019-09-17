# swagger_client.AboutApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about_page**](AboutApi.md#get_about_page) | **GET** /iaas/api/about | Get about page

# **get_about_page**
> About get_about_page()

Get about page

The page contains information about the supported API versions and the latest API version. The version parameter is optional but highly recommended. If you do not specify explicitly an exact version, you will be calling the latest supported API version. Here is an example of a call which specifies the exact version you are using: `GET /iaas/api/network-profiles?apiVersion=2019-01-15`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AboutApi()

try:
    # Get about page
    api_response = api_instance.get_about_page()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about_page: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**About**](About.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

