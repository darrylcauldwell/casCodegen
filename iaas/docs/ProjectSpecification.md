# ProjectSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**administrators** | [**list[User]**](User.md) | List of administrator users associated with the project. Only administrators can manage project&#x27;s configuration. | [optional] 
**members** | [**list[User]**](User.md) | List of member users associated with the project.  | [optional] 
**zone_assignment_configurations** | [**list[ZoneAssignmentConfig]**](ZoneAssignmentConfig.md) | List of configurations for zone assignment to a project. | [optional] 
**constraints** | **dict(str, list[Constraint])** | List of storage, network and extensibility constraints to be applied when provisioning through this project. | [optional] 
**operation_timeout** | **int** | The timeout that should be used for Blueprint operations and Provisioning tasks. The timeout is in seconds | [optional] 
**machine_naming_template** | **str** | The naming template to be used for machines provisioned in this project | [optional] 
**shared_resources** | **bool** | Specifies whether the resources in this projects are shared or not. If not set default will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

