# swagger_client.LoadBalancerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_load_balancer**](LoadBalancerApi.md#create_load_balancer) | **POST** /iaas/api/load-balancers | Create load balancer
[**delete_load_balancer**](LoadBalancerApi.md#delete_load_balancer) | **DELETE** /iaas/api/load-balancers/{id} | Delete load balancer
[**delete_load_balancer_operation**](LoadBalancerApi.md#delete_load_balancer_operation) | **POST** /iaas/api/load-balancers/{id}/operations/delete | Delete operation for load balancer
[**get_load_balancer**](LoadBalancerApi.md#get_load_balancer) | **GET** /iaas/api/load-balancers/{id} | Get load balancer
[**get_load_balancers**](LoadBalancerApi.md#get_load_balancers) | **GET** /iaas/api/load-balancers | Get load balancers
[**scale_load_balancer**](LoadBalancerApi.md#scale_load_balancer) | **POST** /iaas/api/load-balancers/{id}/operations/scale | Scale operation for load balancer

# **create_load_balancer**
> RequestTracker create_load_balancer(body, api_version=api_version)

Create load balancer

Create load balancer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
body = swagger_client.LoadBalancerSpecification() # LoadBalancerSpecification | LoadBalancer Specification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create load balancer
    api_response = api_instance.create_load_balancer(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->create_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadBalancerSpecification**](LoadBalancerSpecification.md)| LoadBalancer Specification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer**
> RequestTracker delete_load_balancer(id, api_version=api_version)

Delete load balancer

Delete load balancer with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
id = 'id_example' # str | The ID of the load balancer.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete load balancer
    api_response = api_instance.delete_load_balancer(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->delete_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the load balancer. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_operation**
> RequestTracker delete_load_balancer_operation(id, api_version=api_version)

Delete operation for load balancer

Second day delete operation for load balancer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
id = 'id_example' # str | The ID of the load balancer.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete operation for load balancer
    api_response = api_instance.delete_load_balancer_operation(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->delete_load_balancer_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the load balancer. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer**
> LoadBalancer get_load_balancer(id, api_version=api_version)

Get load balancer

Get load balancer with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
id = 'id_example' # str | The ID of the load balancer.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get load balancer
    api_response = api_instance.get_load_balancer(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->get_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the load balancer. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancers**
> LoadBalancerResult get_load_balancers(api_version=api_version)

Get load balancers

Get all load balancers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get load balancers
    api_response = api_instance.get_load_balancers(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->get_load_balancers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**LoadBalancerResult**](LoadBalancerResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_load_balancer**
> RequestTracker scale_load_balancer(body, id, api_version=api_version)

Scale operation for load balancer

Second day scale operation for load balancer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadBalancerApi()
body = swagger_client.LoadBalancerSpecification() # LoadBalancerSpecification | LoadBalancer Specification instance
id = 'id_example' # str | The ID of the load balancer.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Scale operation for load balancer
    api_response = api_instance.scale_load_balancer(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadBalancerApi->scale_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadBalancerSpecification**](LoadBalancerSpecification.md)| LoadBalancer Specification instance | 
 **id** | **str**| The ID of the load balancer. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

