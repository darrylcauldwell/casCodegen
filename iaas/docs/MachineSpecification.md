# MachineSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name used as an identifier in APIs that support this option. | 
**project_id** | **str** | The id of the project the current user belongs to. | 
**description** | **str** | Describes machine within the scope of your organization and is not propagated to the cloud | [optional] 
**flavor** | **str** | Flavor of machine instance. | 
**image** | **str** | Type of image used for this machine. | 
**image_ref** | **str** | Direct image reference used for this machine (name, path, location, uri, etc.). Valid if no image property is provided | 
**nics** | [**list[NetworkInterfaceSpecification]**](NetworkInterfaceSpecification.md) | A set of network interface controller specifications for this machine. If not specified, then a default network connection will be created. | [optional] 
**disks** | [**list[DiskAttachmentSpecification]**](DiskAttachmentSpecification.md) | A set of disk specifications for this machine. | [optional] 
**boot_config** | [**MachineBootConfig**](MachineBootConfig.md) |  | [optional] 
**machine_count** | **int** | Number of machines to provision - default 1. | [optional] 
**constraints** | [**list[Constraint]**](Constraint.md) | Constraints that are used to drive placement policies for the virtual machine that is produced from this specification. Constraint expressions are matched against tags on existing placement targets. | [optional] 
**image_disk_constraints** | [**list[Constraint]**](Constraint.md) | Constraints that are used to drive placement policies for the image disk. Constraint expressions are matched against tags on existing placement targets. | [optional] 
**tags** | [**list[Tag]**](Tag.md) | A set of tag keys and optional values that should be set on any resource that is produced from this specification. | [optional] 
**custom_properties** | **dict(str, str)** | Additional custom properties that may be used to extend the machine. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

