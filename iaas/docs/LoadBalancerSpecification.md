# LoadBalancerSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**project_id** | **str** | The id of the project the current user belongs to. | 
**description** | **str** | A human-friendly description. | [optional] 
**routes** | [**list[RouteConfiguration]**](RouteConfiguration.md) | The load balancer route configuration regarding ports and protocols. | 
**nics** | [**list[NetworkInterfaceSpecification]**](NetworkInterfaceSpecification.md) | A set of network interface specifications for this load balancer. | 
**target_links** | **list[str]** | A list of links to target load balancer pool members. Links can be to either a machine or a machine&#x27;s network interface. | [optional] 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the load balancer. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that should be set on any resource that is produced from this specification. | [optional] 
**internet_facing** | **bool** | An Internet-facing load balancer has a publicly resolvable DNS name, so it can route requests from clients over the Internet to the instances that are registered with the load balancer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

