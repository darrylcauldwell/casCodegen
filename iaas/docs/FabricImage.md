# FabricImage

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
**os_family** | **str** | Operating System family of the image. | [optional] 
**external_region_id** | **str** | The regionId of the image | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the base type. | [optional] 
**is_private** | **bool** | Indicates whether this fabric image is private. For vSphere, private images are considered to be templates and snapshots and public are Content Library Items | [optional] 
**cloud_account_ids** | **list[str]** | Set of ids of the cloud accounts this entity belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

