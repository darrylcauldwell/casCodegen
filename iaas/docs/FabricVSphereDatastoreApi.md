# swagger_client.FabricVSphereDatastoreApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_v_sphere_datastore**](FabricVSphereDatastoreApi.md#get_fabric_v_sphere_datastore) | **GET** /iaas/api/fabric-vsphere-datastores/{id} | Get fabric vSphere datastore
[**get_fabric_v_sphere_datastores**](FabricVSphereDatastoreApi.md#get_fabric_v_sphere_datastores) | **GET** /iaas/api/fabric-vsphere-datastores | Get fabric vSphere datastores

# **get_fabric_v_sphere_datastore**
> FabricVsphereDatastore get_fabric_v_sphere_datastore(id, api_version=api_version)

Get fabric vSphere datastore

Get fabric vSphere datastore with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricVSphereDatastoreApi()
id = 'id_example' # str | The ID of the Fabric vSphere Datastore.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric vSphere datastore
    api_response = api_instance.get_fabric_v_sphere_datastore(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricVSphereDatastoreApi->get_fabric_v_sphere_datastore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Fabric vSphere Datastore. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricVsphereDatastore**](FabricVsphereDatastore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_v_sphere_datastores**
> FabricVsphereDatastoreResult get_fabric_v_sphere_datastores(api_version=api_version)

Get fabric vSphere datastores

Get all fabric vSphere datastores.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricVSphereDatastoreApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric vSphere datastores
    api_response = api_instance.get_fabric_v_sphere_datastores(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricVSphereDatastoreApi->get_fabric_v_sphere_datastores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricVsphereDatastoreResult**](FabricVsphereDatastoreResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

