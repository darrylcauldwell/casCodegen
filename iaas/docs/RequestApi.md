# swagger_client.RequestApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_request**](RequestApi.md#delete_request) | **DELETE** /iaas/api/request-tracker/{id} | Delete Request
[**get_request_tracker**](RequestApi.md#get_request_tracker) | **GET** /iaas/api/request-tracker/{id} | Get request tracker
[**get_request_trackers**](RequestApi.md#get_request_trackers) | **GET** /iaas/api/request-tracker | Get request tracker

# **delete_request**
> delete_request(id, api_version=api_version)

Delete Request

Delete a single Request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestApi()
id = 'id_example' # str | The ID of the request.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete Request
    api_instance.delete_request(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling RequestApi->delete_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the request. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_tracker**
> RequestTracker get_request_tracker(id, api_version=api_version)

Get request tracker

Get request tracker with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestApi()
id = 'id_example' # str | The ID of the request.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get request tracker
    api_response = api_instance.get_request_tracker(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->get_request_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the request. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_trackers**
> RequestTrackerResult get_request_trackers(api_version=api_version)

Get request tracker

Get all request trackers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get request tracker
    api_response = api_instance.get_request_trackers(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->get_request_trackers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTrackerResult**](RequestTrackerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

