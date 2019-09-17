# CloudAccountAwsSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**access_key_id** | **str** | Aws Access key ID | 
**secret_access_key** | **str** | Aws Secret Access Key | 
**region_ids** | **list[str]** | A set of Region names to enable provisioning on. Refer to /iaas/cloud-accounts-aws/region-enumeration.. | 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

