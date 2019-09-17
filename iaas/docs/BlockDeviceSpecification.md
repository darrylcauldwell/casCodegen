# BlockDeviceSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**project_id** | **str** | The id of the project the current user belongs to. | 
**description** | **str** | A human-friendly description. | [optional] 
**capacity_in_gb** | **int** | Capacity of the block device in GB. | 
**encrypted** | **bool** | Indicates whether the block device should be encrypted or not. | [optional] 
**source_reference** | **str** | Reference to URI using which the block device has to be created. | [optional] 
**disk_content_base64** | **str** | Content of a disk, base64 encoded. | [optional] 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the block device. | [optional] 
**constraints** | [**list[Constraint]**](Constraint.md) | Constraints that are used to drive placement policies for the block device that is produced from this specification. Constraint expressions are matched against tags on existing placement targets. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that should be set on any resource that is produced from this specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

