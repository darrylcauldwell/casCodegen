# StorageProfileVsphereSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**default_item** | **bool** | Indicates if a storage profile acts as a default storage profile for a disk. | 
**supports_encryption** | **bool** | Indicates whether this storage profile supports encryption or not. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A list of tags that represent the capabilities of this storage profile. | [optional] 
**datastore_id** | **str** | Id of the vSphere Datastore for placing disk and VM. | [optional] 
**storage_policy_id** | **str** | Id of the vSphere Storage Policy to be applied. | [optional] 
**provisioning_type** | **str** | Type of provisioning policy for the disk. | [optional] 
**shares_level** | **str** | Shares are specified as High, Normal, Low or Custom and these values specify share values with a 4:2:1 ratio, respectively.  | [optional] 
**shares** | **str** | A specific number of shares assigned to each virtual machine. | [optional] 
**limit_iops** | **str** | The upper bound for the I/O operations per second allocated for each virtual disk. | [optional] 
**disk_mode** | **str** | Type of mode for the disk | [optional] 
**region_id** | **str** | The Id of the region that is associated with the storage profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

