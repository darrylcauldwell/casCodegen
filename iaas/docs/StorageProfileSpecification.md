# StorageProfileSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**default_item** | **bool** | Indicates if a storage profile is a default profile. | 
**supports_encryption** | **bool** | Indicates whether this storage profile supports encryption or not. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A list of tags that represent the capabilities of this storage profile | [optional] 
**disk_properties** | **dict(str, str)** | Map of storage properties that are to be applied on disk while provisioning. | [optional] 
**disk_target_properties** | **dict(str, str)** | Map of storage placements to know where the disk is provisioned. | [optional] 
**region_id** | **str** | The Id of the region that is associated with the storage profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

