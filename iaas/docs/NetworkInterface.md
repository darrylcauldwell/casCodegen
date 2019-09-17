# NetworkInterface

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
**external_id** | **str** | External entity Id on the provider side. | [optional] 
**device_index** | **int** | The device index of this network interface. | [optional] 
**addresses** | **list[str]** | A list of IP addresses allocated or in use by this network interface. | [optional] 
**external_region_id** | **str** | The external regionId of the network interface. | 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that were set on this network interface. | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the base type. | [optional] 
**cloud_account_ids** | **list[str]** | Set of ids of the cloud accounts this entity belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

