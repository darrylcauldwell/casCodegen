# ZoneSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**region_id** | **str** | The id of the region for which this profile is created | 
**placement_policy** | **str** | Placement policy for the zone. One of DEFAULT, SPREAD or BINPACK. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that are effectively applied to all compute resources in this zone, but only in the context of this zone. | [optional] 
**tags_to_match** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that will be used  | [optional] 
**custom_properties** | **dict(str, str)** | A list of key value pair of properties that will  be used | [optional] 
**folder** | **str** | The folder relative path to the datacenter where resources are deployed to. (only applicable for vSphere cloud zones) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

