# NetworkProfileSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**fabric_network_ids** | **list[str]** | A list of fabric network Ids which are assigned to the network profile. | [optional] 
**security_group_ids** | **list[str]** | A list of security group Ids which are assigned to the network profile. | [optional] 
**region_id** | **str** | The Id of the region for which this profile is created | 
**isolation_type** | **str** | Specifies the isolation type e.g. none, subnet or security group | [optional] 
**isolation_network_domain_id** | **str** | The Id of the network domain used for creating isolated networks. | [optional] 
**isolation_network_domain_cidr** | **str** | CIDR of the isolation network domain. | [optional] 
**isolation_external_fabric_network_id** | **str** | The Id of the fabric network used for outbound access. | [optional] 
**isolated_network_cidr_prefix** | **int** | The CIDR prefix length to be used for the isolated networks that are created with the network profile. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that should be set on any resource that is produced from this specification. | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the Network Profile object that is produced from this specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

