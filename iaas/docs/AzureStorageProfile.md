# AzureStorageProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of this resource instance | 
**created_at** | **str** | Date when the entity was created. The date is in ISO 6801 and UTC. | [optional] 
**updated_at** | **str** | Date when the entity was last updated. The date is ISO 8601 and UTC. | [optional] 
**owner** | **str** | Email of the user that owns the entity. | [optional] 
**organization_id** | **str** | This field is deprecated. Use orgId instead. The id of the organization this entity belongs to. | [optional] 
**org_id** | **str** | The id of the organization this entity belongs to. | [optional] 
**links** | [**dict(str, Href)**](Href.md) | HATEOAS of the entity | 
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | [optional] 
**description** | **str** | A human-friendly description. | [optional] 
**default_item** | **bool** | Indicates if a storage profile contains default storage properties. | 
**supports_encryption** | **bool** | Indicates whether this storage profile should support encryption or not. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A list of tags that represent the capabilities of this storage profile | [optional] 
**disk_type** | **str** | Indicates the performance tier for the storage type. Premium disks are SSD backed and Standard disks are HDD backed. | [optional] 
**os_disk_caching** | **str** | Indicates the caching mechanism for OS disk. Default policy for OS disks is Read/Write. | [optional] 
**data_disk_caching** | **str** | Indicates the caching mechanism for additional disk.  | [optional] 
**external_region_id** | **str** | The id of the region for which this profile is defined | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

