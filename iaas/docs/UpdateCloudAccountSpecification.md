# UpdateCloudAccountSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A human-friendly description. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the Cloud Account. | [optional] 
**region_ids** | **list[str]** | A set of Region names to enable provisioning on. | [optional] 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**associated_cloud_account_ids** | **list[str]** | Cloud accounts to link with this cloud account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

