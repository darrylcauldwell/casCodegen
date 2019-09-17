# CloudAccountVsphereSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**description** | **str** | A human-friendly description. | [optional] 
**host_name** | **str** | Host name for the vSphere endpoint | 
**accept_self_signed_certificate** | **bool** | Accept self signed certificate when connecting to vSphere | [optional] 
**associated_cloud_account_ids** | **list[str]** | Cloud accounts to associate with this cloud account | [optional] 
**dcid** | **str** | Identifier of a data collector vm deployed in the on premise infrastructure. Refer to the data-collector API to create or list data collectors | [optional] 
**username** | **str** | Username to authenticate with the cloud account | 
**password** | **str** | Password for the user used to authenticate with the cloud Account | 
**region_ids** | **list[str]** | A set of datacenter managed object reference identifiers (MoRef) to enable provisioning on. Refer to /iaas/cloud-accounts-vsphere/region-enumeration. | 
**create_default_zones** | **bool** | Create default cloud zones for the enabled regions. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values to set on the Cloud Account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

