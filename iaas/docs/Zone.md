# Zone

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
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that were set on this placement. | [optional] 
**tags_to_match** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values for compute resource filtering. | [optional] 
**placement_policy** | **str** | The placement policy for the zone. | [optional] 
**custom_properties** | **dict(str, str)** | A list of key value pair of properties that will  be used | [optional] 
**folder** | **str** | The folder relative path to the datacenter where resources are deployed to. (only applicable for vSphere cloud zones) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

