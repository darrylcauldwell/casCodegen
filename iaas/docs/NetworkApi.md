# swagger_client.NetworkApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network**](NetworkApi.md#create_network) | **POST** /iaas/api/networks | Create network
[**delete_network**](NetworkApi.md#delete_network) | **DELETE** /iaas/api/networks/{id} | Delete a network
[**get_machine_network_interface**](NetworkApi.md#get_machine_network_interface) | **GET** /iaas/api/machines/{id}/network-interfaces/{id1} | Get machine network interface
[**get_network**](NetworkApi.md#get_network) | **GET** /iaas/api/networks/{id} | Get network
[**get_network_domain**](NetworkApi.md#get_network_domain) | **GET** /iaas/api/network-domains/{id} | Get network domain
[**get_network_domains**](NetworkApi.md#get_network_domains) | **GET** /iaas/api/network-domains | Get network domains
[**get_networks**](NetworkApi.md#get_networks) | **GET** /iaas/api/networks | Get networks

# **create_network**
> RequestTracker create_network(body, api_version=api_version)

Create network

Provision a new network based on the passed in constraints. The network should be destroyed after the machine is destroyed to free up resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
body = swagger_client.NetworkSpecification() # NetworkSpecification | Network Specification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create network
    api_response = api_instance.create_network(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkSpecification**](NetworkSpecification.md)| Network Specification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> RequestTracker delete_network(id, api_version=api_version)

Delete a network

Delete a network with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | The ID of the network.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a network
    api_response = api_instance.delete_network(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the network. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_network_interface**
> NetworkInterface get_machine_network_interface(id, id1, api_version=api_version)

Get machine network interface

Get network interface with a given id for specific machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the network interface.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine network interface
    api_response = api_instance.get_machine_network_interface(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_machine_network_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **id1** | **str**| The ID of the network interface. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> Network get_network(id, api_version=api_version)

Get network

Get network with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | The ID of the network.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get network
    api_response = api_instance.get_network(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the network. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_domain**
> NetworkDomain get_network_domain(id, api_version=api_version)

Get network domain

Get network domain with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | The ID of the network domain.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get network domain
    api_response = api_instance.get_network_domain(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the network domain. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkDomain**](NetworkDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_domains**
> NetworkDomainResult get_network_domains(api_version=api_version)

Get network domains

Get all network domains.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get network domains
    api_response = api_instance.get_network_domains(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkDomainResult**](NetworkDomainResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_networks**
> NetworkResult get_networks(api_version=api_version)

Get networks

Get all networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get networks
    api_response = api_instance.get_networks(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**NetworkResult**](NetworkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

