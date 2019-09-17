# FabricNetwork

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
**is_public** | **bool** | Indicates whether the sub-network supports public IP assignment. | [optional] 
**is_default** | **bool** | Indicates whether this is the default subnet for the zone. | [optional] 
**cidr** | **str** | Network CIDR to be used. | [optional] 
**ipv6_cidr** | **str** | Network IPv6 CIDR to be used. | [optional] 
**external_region_id** | **str** | The id of the region for which this network is defined | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that were set on this resource instance. | [optional] 
**cloud_account_ids** | **list[str]** | Set of ids of the cloud accounts this entity belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

