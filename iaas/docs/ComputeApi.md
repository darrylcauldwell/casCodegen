# swagger_client.ComputeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_machine_disk**](ComputeApi.md#attach_machine_disk) | **POST** /iaas/api/machines/{id}/disks | Attach machine disk
[**create_machine**](ComputeApi.md#create_machine) | **POST** /iaas/api/machines | Create machine
[**create_machine_snapshot**](ComputeApi.md#create_machine_snapshot) | **POST** /iaas/api/machines/{id}/operations/snapshots | Create snapshot operation for machine
[**delete_machine**](ComputeApi.md#delete_machine) | **DELETE** /iaas/api/machines/{id} | Delete Machine
[**delete_machine_disk**](ComputeApi.md#delete_machine_disk) | **DELETE** /iaas/api/machines/{id}/disks/{id1} | Delete machine disk
[**delete_machine_snapshot**](ComputeApi.md#delete_machine_snapshot) | **DELETE** /iaas/api/machines/{id}/snapshots/{id1} | Delete snapshot operation for machine
[**get_machine**](ComputeApi.md#get_machine) | **GET** /iaas/api/machines/{id} | Get machine
[**get_machine_disk**](ComputeApi.md#get_machine_disk) | **GET** /iaas/api/machines/{id}/disks/{id1} | Get a machine disk
[**get_machine_disks**](ComputeApi.md#get_machine_disks) | **GET** /iaas/api/machines/{id}/disks | Get machine disks
[**get_machine_network_interface**](ComputeApi.md#get_machine_network_interface) | **GET** /iaas/api/machines/{id}/network-interfaces/{id1} | Get machine network interface
[**get_machine_snapshots**](ComputeApi.md#get_machine_snapshots) | **GET** /iaas/api/machines/{id}/snapshots | Get machine snapshots information
[**get_machines**](ComputeApi.md#get_machines) | **GET** /iaas/api/machines | Get machines
[**power_off_machine**](ComputeApi.md#power_off_machine) | **POST** /iaas/api/machines/{id}/operations/power-off | Power-off operation for machine
[**power_on_machine**](ComputeApi.md#power_on_machine) | **POST** /iaas/api/machines/{id}/operations/power-on | Power-on operation for machine
[**reboot_machine**](ComputeApi.md#reboot_machine) | **POST** /iaas/api/machines/{id}/operations/reboot | Reboot operation for machine
[**reset_machine**](ComputeApi.md#reset_machine) | **POST** /iaas/api/machines/{id}/operations/reset | Reset operation for machine
[**resize_machine**](ComputeApi.md#resize_machine) | **POST** /iaas/api/machines/{id}/operations/resize | Resize operation for machine
[**restart_machine**](ComputeApi.md#restart_machine) | **POST** /iaas/api/machines/{id}/operations/restart | Restart operation for machine
[**revert_machine_snapshot**](ComputeApi.md#revert_machine_snapshot) | **POST** /iaas/api/machines/{id}/operations/revert | Revert snapshot operation for machine
[**shutdown_machine**](ComputeApi.md#shutdown_machine) | **POST** /iaas/api/machines/{id}/operations/shutdown | Shut down operation for machine
[**suspend_machine**](ComputeApi.md#suspend_machine) | **POST** /iaas/api/machines/{id}/operations/suspend | Suspend operation for machine
[**update_machine**](ComputeApi.md#update_machine) | **PATCH** /iaas/api/machines/{id} | Update machine.

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
api_instance = swagger_client.ComputeApi()
body = swagger_client.DiskAttachmentSpecification() # DiskAttachmentSpecification | Disk Specification instance
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Attach machine disk
    api_response = api_instance.attach_machine_disk(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->attach_machine_disk: %s\n" % e)
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

# **create_machine**
> RequestTracker create_machine(body, api_version=api_version)

Create machine

Create machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
body = swagger_client.MachineSpecification() # MachineSpecification | Machine Specification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create machine
    api_response = api_instance.create_machine(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->create_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MachineSpecification**](MachineSpecification.md)| Machine Specification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_machine_snapshot**
> RequestTracker create_machine_snapshot(body, id, api_version=api_version)

Create snapshot operation for machine

Second day create snapshot operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
body = swagger_client.SnapshotSpecification() # SnapshotSpecification | Snapshot Specification details
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create snapshot operation for machine
    api_response = api_instance.create_machine_snapshot(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->create_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotSpecification**](SnapshotSpecification.md)| Snapshot Specification details | 
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_machine**
> RequestTracker delete_machine(id, api_version=api_version)

Delete Machine

Delete Machine with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete Machine
    api_response = api_instance.delete_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->delete_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
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
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the disk.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete machine disk
    api_response = api_instance.delete_machine_disk(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->delete_machine_disk: %s\n" % e)
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

# **delete_machine_snapshot**
> RequestTracker delete_machine_snapshot(id, id1, api_version=api_version)

Delete snapshot operation for machine

Second day delete snapshot operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
id1 = 'id1_example' # str | Snapshot id to delete.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete snapshot operation for machine
    api_response = api_instance.delete_machine_snapshot(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->delete_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **id1** | **str**| Snapshot id to delete. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine**
> Machine get_machine(id, api_version=api_version)

Get machine

Get machine with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine
    api_response = api_instance.get_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Machine**](Machine.md)

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
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the disk.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get a machine disk
    api_response = api_instance.get_machine_disk(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machine_disk: %s\n" % e)
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
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine disks
    api_response = api_instance.get_machine_disks(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machine_disks: %s\n" % e)
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
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
id1 = 'id1_example' # str | The ID of the network interface.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine network interface
    api_response = api_instance.get_machine_network_interface(id, id1, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machine_network_interface: %s\n" % e)
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

# **get_machine_snapshots**
> list[Snapshot] get_machine_snapshots(id, api_version=api_version)

Get machine snapshots information

Get machine snapshots information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The ID of the machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machine snapshots information
    api_response = api_instance.get_machine_snapshots(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machine_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**list[Snapshot]**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machines**
> MachineResult get_machines(api_version=api_version)

Get machines

Get all machines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get machines
    api_response = api_instance.get_machines(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->get_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**MachineResult**](MachineResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **power_off_machine**
> RequestTracker power_off_machine(id, api_version=api_version)

Power-off operation for machine

Second day power-off operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Power-off operation for machine
    api_response = api_instance.power_off_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->power_off_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **power_on_machine**
> RequestTracker power_on_machine(id, api_version=api_version)

Power-on operation for machine

Second day power-on operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Power-on operation for machine
    api_response = api_instance.power_on_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->power_on_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_machine**
> RequestTracker reboot_machine(id, api_version=api_version)

Reboot operation for machine

Second day reboot operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Reboot operation for machine
    api_response = api_instance.reboot_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->reboot_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_machine**
> RequestTracker reset_machine(id, api_version=api_version)

Reset operation for machine

Second day reset operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Reset operation for machine
    api_response = api_instance.reset_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->reset_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_machine**
> RequestTracker resize_machine(id, name=name, cpu_count=cpu_count, memory_in_mb=memory_in_mb, api_version=api_version)

Resize operation for machine

Second day resize operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
name = 'name_example' # str | The desired flavor to resize the Machine. (optional)
cpu_count = 'cpu_count_example' # str | The desired number of CPUs to resize the Machine (optional)
memory_in_mb = 'memory_in_mb_example' # str | The desired memory in MBs to resize the Machine (optional)
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Resize operation for machine
    api_response = api_instance.resize_machine(id, name=name, cpu_count=cpu_count, memory_in_mb=memory_in_mb, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->resize_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **name** | **str**| The desired flavor to resize the Machine. | [optional] 
 **cpu_count** | **str**| The desired number of CPUs to resize the Machine | [optional] 
 **memory_in_mb** | **str**| The desired memory in MBs to resize the Machine | [optional] 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_machine**
> RequestTracker restart_machine(id, api_version=api_version)

Restart operation for machine

Second day restart operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Restart operation for machine
    api_response = api_instance.restart_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->restart_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_machine_snapshot**
> RequestTracker revert_machine_snapshot(id, id2, api_version=api_version)

Revert snapshot operation for machine

Second day revert snapshot operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
id2 = 'id_example' # str | Snapshot id to revert.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Revert snapshot operation for machine
    api_response = api_instance.revert_machine_snapshot(id, id2, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->revert_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **id2** | **str**| Snapshot id to revert. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_machine**
> RequestTracker shutdown_machine(id, api_version=api_version)

Shut down operation for machine

Second day shut down operation machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Shut down operation for machine
    api_response = api_instance.shutdown_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->shutdown_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_machine**
> RequestTracker suspend_machine(id, api_version=api_version)

Suspend operation for machine

Second day suspend operation for machine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
id = 'id_example' # str | The id of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Suspend operation for machine
    api_response = api_instance.suspend_machine(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->suspend_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**RequestTracker**](RequestTracker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_machine**
> Machine update_machine(body, id, api_version=api_version)

Update machine.

Update machine. Only tag updates are supported. All other properties in the MachineSpecification body are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComputeApi()
body = swagger_client.UpdateMachineSpecification() # UpdateMachineSpecification | Machine Specification
id = 'id_example' # str | The ID of the Machine.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update machine.
    api_response = api_instance.update_machine(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->update_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMachineSpecification**](UpdateMachineSpecification.md)| Machine Specification | 
 **id** | **str**| The ID of the Machine. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Machine**](Machine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

