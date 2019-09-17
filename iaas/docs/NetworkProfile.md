# NetworkProfile

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
**external_region_id** | **str** | The id of the region for which this profile is defined | [optional] 
**isolation_type** | **str** | Specifies the isolation type e.g. none, subnet or security group | [optional] 
**isolation_network_domain_cidr** | **str** | CIDR of the isolation network domain. | [optional] 
**isolated_network_cidr_prefix** | **int** | The CIDR prefix length to be used for the isolated networks that are created with the network profile. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that were set on this Network Profile. | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the Network Profile object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

