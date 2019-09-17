# NetworkInterfaceSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | [optional] 
**description** | **str** | A human-friendly description. | [optional] 
**device_index** | **int** | The device index of this network interface. | [optional] 
**network_id** | **str** | Id of the network instance that this network interface plugs into. | 
**addresses** | **list[str]** | A list of IP addresses allocated or in use by this network interface. | [optional] 
**security_group_ids** | **list[str]** | A list of security group ids which this network interface will be assigned to. | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the base type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

