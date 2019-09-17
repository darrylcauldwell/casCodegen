# CloudAccountGcpSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**project_id** | **str** | GCP Project ID | 
**private_key_id** | **str** | GCP Private key ID | 
**private_key** | **str** | GCP Private key | 
**client_email** | **str** | GCP Client email | 
**region_ids** | **list[str]** | A set of Region names to enable provisioning on. Refer to /iaas/cloud-accounts-gcp/region-enumeration. | 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

