# CloudAccountSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**cloud_account_type** | **str** | Cloud account type | 
**private_key_id** | **str** | Access key id or username to be used to authenticate with the cloud account | 
**private_key** | **str** | Secret access key or password to be used to authenticate with the cloud account | 
**associated_cloud_account_ids** | **list[str]** | Cloud account to link with this cloud account | [optional] 
**cloud_account_properties** | **dict(str, str)** | Cloud Account specific properties supplied in as name value pairs | 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the Cloud Account. | [optional] 
**region_ids** | **list[str]** | A set of Region names to enable provisioning on.Refer to /iaas/cloud-accounts/region-enumeration. | 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

