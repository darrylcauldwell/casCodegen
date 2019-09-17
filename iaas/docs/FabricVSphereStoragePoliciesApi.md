# swagger_client.FabricVSphereStoragePoliciesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_v_sphere_storage_policies**](FabricVSphereStoragePoliciesApi.md#get_fabric_v_sphere_storage_policies) | **GET** /iaas/api/fabric-vsphere-storage-policies | Get fabric vSphere storage polices
[**get_fabric_v_sphere_storage_policy**](FabricVSphereStoragePoliciesApi.md#get_fabric_v_sphere_storage_policy) | **GET** /iaas/api/fabric-vsphere-storage-policies/{id} | Get fabric vSphere storage policy

# **get_fabric_v_sphere_storage_policies**
> FabricVsphereStoragePolicyResult get_fabric_v_sphere_storage_policies(api_version=api_version)

Get fabric vSphere storage polices

Get all fabric vSphere storage polices.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricVSphereStoragePoliciesApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric vSphere storage polices
    api_response = api_instance.get_fabric_v_sphere_storage_policies(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricVSphereStoragePoliciesApi->get_fabric_v_sphere_storage_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricVsphereStoragePolicyResult**](FabricVsphereStoragePolicyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_v_sphere_storage_policy**
> FabricVsphereStoragePolicy get_fabric_v_sphere_storage_policy(id, api_version=api_version)

Get fabric vSphere storage policy

Get fabric vSphere storage policy with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricVSphereStoragePoliciesApi()
id = 'id_example' # str | The ID of the Fabric vSphere Storage Policy.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric vSphere storage policy
    api_response = api_instance.get_fabric_v_sphere_storage_policy(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricVSphereStoragePoliciesApi->get_fabric_v_sphere_storage_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Fabric vSphere Storage Policy. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**FabricVsphereStoragePolicy**](FabricVsphereStoragePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

