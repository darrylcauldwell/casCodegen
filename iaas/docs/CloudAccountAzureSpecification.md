# CloudAccountAzureSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**subscription_id** | **str** | Azure Subscribtion ID | 
**tenant_id** | **str** | Azure Tenant ID | 
**client_application_id** | **str** | Azure Client Application ID | 
**client_application_secret_key** | **str** | Azure Client Application Secret Key | 
**region_ids** | **list[str]** | A set of Region names to enable provisioning on. Refer to /iaas/cloud-accounts-azure/region-enumeration.. | 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

