# CloudAccountGcp

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
**project_id** | **str** | GCP Project ID | 
**private_key_id** | **str** | GCP Private key ID | 
**client_email** | **str** | GCP Client email | 
**enabled_region_ids** | **list[str]** | A set of region names that are enabled for this  | [optional] 
**custom_properties** | **dict(str, str)** | Additional properties that may be used to extend the base type. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that were set on on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

