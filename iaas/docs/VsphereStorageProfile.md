# VsphereStorageProfile

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
**provisioning_type** | **str** | Type of format for the disk. | [optional] 
**shares_level** | **str** | Shares level are specified as High, Normal, Low or Custom. | [optional] 
**shares** | **str** | A specific number of shares assigned to each virtual machine. | [optional] 
**limit_iops** | **str** | The upper bound for the I/O operations per second allocated for each disk. | [optional] 
**disk_mode** | **str** | Type of mode for the disk | [optional] 
**external_region_id** | **str** | The id of the region for which this profile is defined | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

