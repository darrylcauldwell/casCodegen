# StorageProfileAzureSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**default_item** | **bool** | Indicates if a storage policy contains default storage properties. | [optional] 
**supports_encryption** | **bool** | Indicates whether this storage policy should support encryption or not. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values for a storage policy which define set of specifications for creating a disk. | [optional] 
**disk_type** | **str** | Indicates the performance tier for the storage type. Premium disks are SSD backed and Standard disks are HDD backed. | [optional] 
**os_disk_caching** | **str** | Indicates the caching mechanism for OS disk. Default policy for OS disks is Read/Write. | [optional] 
**data_disk_caching** | **str** | Indicates the caching mechanism for additional disk.  | [optional] 
**storage_account_id** | **str** | Id of a storage account where in the disk is placed. | [optional] 
**region_id** | **str** | The If of the region that is associated with the storage profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

