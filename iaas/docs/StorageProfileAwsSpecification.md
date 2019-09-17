# StorageProfileAwsSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**default_item** | **bool** | Indicates if a storage profile is default or not. | [optional] 
**supports_encryption** | **bool** | Indicates whether this storage profile supports encryption or not. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A list of tags that represent the capabilities of this storage profile | [optional] 
**device_type** | **str** | Indicates the type of storage. | 
**volume_type** | **str** | Indicates the type of volume associated with type of storage. | [optional] 
**iops** | **str** | Indicates maximum I/O operations per second in range(1-20,000). | [optional] 
**region_id** | **str** | A link to the region that is associated with the storage profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

