# swagger_client.DiskApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_machine_disk**](DiskApi.md#attach_machine_disk) | **POST** /iaas/api/machines/{id}/disks | Attach machine disk
[**create_block_device**](DiskApi.md#create_block_device) | **POST** /iaas/api/block-devices | Create BlockDevice
[**delete_block_device**](DiskApi.md#delete_block_device) | **DELETE** /iaas/api/block-devices/{id} | Delete a BlockDevice
[**delete_machine_disk**](DiskApi.md#delete_machine_disk) | **DELETE** /iaas/api/machines/{id}/disks/{id1} | Delete machine disk
[**get_block_device**](DiskApi.md#get_block_device) | **GET** /iaas/api/block-devices/{id} | Get BlockDevice
[**get_block_devices**](DiskApi.md#get_block_devices) | **GET** /iaas/api/block-devices | Get BlockDevices
[**get_machine_disk**](DiskApi.md#get_machine_disk) | **GET** /iaas/api/machines/{id}/disks/{id1} | Get a machine disk
[**get_machine_disks**](DiskApi.md#get_machine_disks) | **GET** /iaas/api/machines/{id}/disks | Get machine disks

# **attach_machine_disk**
> BlockDevice attach_machine_disk(body, id, api_version=api_version)

Attach machine disk

Attach a disk to a machine.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
body = swagger_client.DiskAttachmentSpecification() # DiskAttachmentSpecification | Disk Specification instance
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Attach machine disk
    api_response = api_instance.attach_machine_disk(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->attach_machine_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskAttachmentSpecification**](DiskAttachmentSpecification.md)| Disk Specification instance | 
 **id** | **str**| The ID of the machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDevice**](BlockDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_block_device**
> RequestTracker create_block_device(body, api_version=api_version)

Create BlockDevice

Following disk custom properties can be passed while creating a block device:         1. dataStore: Defines name of the datastore in which the disk has to be provisioned.       2. storagePolicy: Defines name of the storage policy in which the disk has to be provisioned. If name of the datastore is specified in the custom properties then, datastore takes precedence.      3. provisioningType: Defines the type of provisioning. For eg. thick/thin. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
body = swagger_client.BlockDeviceSpecification() # BlockDeviceSpecification | Disk Specification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create BlockDevice
    api_response = api_instance.create_block_device(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->create_block_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlockDeviceSpecification**](BlockDeviceSpecification.md)| Disk Specification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_device**
> RequestTracker delete_block_device(id, api_version=api_version)

Delete a BlockDevice

Delete a BlockDevice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
id = 'id_example' # str | The ID of the block device.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete a BlockDevice
    api_response = api_instance.delete_block_device(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->delete_block_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the block device. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_machine_disk**
> BlockDevice delete_machine_disk(id, id1, api_version=api_version)

Delete machine disk

Remove a disk from a given machine.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the disk.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete machine disk
    api_response = api_instance.delete_machine_disk(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->delete_machine_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **id1** | **str**| The ID of the disk. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDevice**](BlockDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_device**
> BlockDevice get_block_device(id, api_version=api_version)

Get BlockDevice

Get a single BlockDevice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
id = 'id_example' # str | The ID of the block device.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get BlockDevice
    api_response = api_instance.get_block_device(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->get_block_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the block device. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDevice**](BlockDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_devices**
> BlockDeviceResult get_block_devices(api_version=api_version)

Get BlockDevices

Get all BlockDevices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get BlockDevices
    api_response = api_instance.get_block_devices(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->get_block_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDeviceResult**](BlockDeviceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_disk**
> BlockDevice get_machine_disk(id, id1, api_version=api_version)

Get a machine disk

Get disk with a given id for specific machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the disk.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get a machine disk
    api_response = api_instance.get_machine_disk(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->get_machine_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **id1** | **str**| The ID of the disk. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDevice**](BlockDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_disks**
> BlockDeviceResult get_machine_disks(id, api_version=api_version)

Get machine disks

Get all machine disks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiskApi()
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine disks
    api_response = api_instance.get_machine_disks(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskApi->get_machine_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**BlockDeviceResult**](BlockDeviceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

