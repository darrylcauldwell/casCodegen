# NetworkSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**project_id** | **str** | The id of the project the current user belongs to. | 
**description** | **str** | A human-friendly description. | [optional] 
**constraints** | [**list[Constraint]**](Constraint.md) | Constraints that are used to drive placement policies for the network that is produced from this specification, related with the network profile. Constraint expressions are matched against tags on existing placement targets. | [optional] 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the network. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that should be set on any resource that is produced from this specification. | [optional] 
**outbound_access** | **bool** | Flag to indicate if the network needs to have outbound access or not. Default is true. This field will be ignored if there is proper input for networkType customProperty | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

