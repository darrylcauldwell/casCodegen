# Project

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
**administrators** | [**list[User]**](User.md) | List of administrator users associated with the project. Only administrators can manage project&#x27;s configuration. | [optional] 
**members** | [**list[User]**](User.md) | List of member users associated with the project.  | [optional] 
**zones** | [**list[ZoneAssignmentConfig]**](ZoneAssignmentConfig.md) | List of Cloud Zones assigned to this project. You can limit deployment to a single region or allow multi-region placement by adding more than one cloud zone to a project. A cloud zone lists available resources. Use tags on resources to control workload placement. | [optional] 
**constraints** | **dict(str, list[Constraint])** | List of storage, network and extensibility constraints to be applied when provisioning through this project. | [optional] 
**operation_timeout** | **int** | The timeout that should be used for Blueprint operations and Provisioning tasks. The timeout is in seconds | [optional] 
**machine_naming_template** | **str** | The naming template to be used for machines provisioned in this project | [optional] 
**shared_resources** | **bool** | Specifies whether the resources in this projects are shared or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

