# swagger_client.FabricAWSVolumeTypesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fabric_aws_volume_types**](FabricAWSVolumeTypesApi.md#get_fabric_aws_volume_types) | **GET** /iaas/api/fabric-aws-volume-types | Get fabric AWS volume types

# **get_fabric_aws_volume_types**
> VolumeTypeList get_fabric_aws_volume_types(api_version=api_version)

Get fabric AWS volume types

Get all fabric AWS volume types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricAWSVolumeTypesApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get fabric AWS volume types
    api_response = api_instance.get_fabric_aws_volume_types(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FabricAWSVolumeTypesApi->get_fabric_aws_volume_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**VolumeTypeList**](VolumeTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

