# swagger_client.DataCollectorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_collector**](DataCollectorApi.md#create_data_collector) | **POST** /iaas/api/data-collectors | Create Data collector
[**delete_data_collector**](DataCollectorApi.md#delete_data_collector) | **DELETE** /iaas/api/data-collectors/{id} | Delete Data Collector
[**get_data_collector**](DataCollectorApi.md#get_data_collector) | **GET** /iaas/api/data-collectors/{id} | Get Data Collector
[**get_data_collectors**](DataCollectorApi.md#get_data_collectors) | **GET** /iaas/api/data-collectors | Get Data Collectors

# **create_data_collector**
> DataCollectorRegistration create_data_collector(api_version=api_version)

Create Data collector

Create a new Data Collector.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCollectorApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create Data collector
    api_response = api_instance.create_data_collector(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCollectorApi->create_data_collector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**DataCollectorRegistration**](DataCollectorRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_collector**
> delete_data_collector(id, api_version=api_version)

Delete Data Collector

Delete Data Collector with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCollectorApi()
id = 'id_example' # str | The ID of the Data Collector.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete Data Collector
    api_instance.delete_data_collector(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling DataCollectorApi->delete_data_collector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Data Collector. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_collector**
> DataCollector get_data_collector(id, api_version=api_version)

Get Data Collector

Get Data Collector with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCollectorApi()
id = 'id_example' # str | The ID of the Data Collector.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get Data Collector
    api_response = api_instance.get_data_collector(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCollectorApi->get_data_collector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Data Collector. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**DataCollector**](DataCollector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_collectors**
> DataCollectorResult get_data_collectors(api_version=api_version, disabled=disabled)

Get Data Collectors

Get all Data Collectors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCollectorApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)
disabled = true # bool | If query param is provided with value equals to true, only disabled data collectors will be retrieved.  (optional)

try:
    # Get Data Collectors
    api_response = api_instance.get_data_collectors(api_version=api_version, disabled=disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCollectorApi->get_data_collectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 
 **disabled** | **bool**| If query param is provided with value equals to true, only disabled data collectors will be retrieved.  | [optional] 

### Return type

[**DataCollectorResult**](DataCollectorResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

