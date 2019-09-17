# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.constraint import Constraint  # noqa: F401,E501
from swagger_client.models.disk_attachment_specification import DiskAttachmentSpecification  # noqa: F401,E501
from swagger_client.models.machine_boot_config import MachineBootConfig  # noqa: F401,E501
from swagger_client.models.network_interface_specification import NetworkInterfaceSpecification  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class MachineSpecification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'project_id': 'str',
        'description': 'str',
        'flavor': 'str',
        'image': 'str',
        'image_ref': 'str',
        'nics': 'list[NetworkInterfaceSpecification]',
        'disks': 'list[DiskAttachmentSpecification]',
        'boot_config': 'MachineBootConfig',
        'machine_count': 'int',
        'constraints': 'list[Constraint]',
        'image_disk_constraints': 'list[Constraint]',
        'tags': 'list[Tag]',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'projectId',
        'description': 'description',
        'flavor': 'flavor',
        'image': 'image',
        'image_ref': 'imageRef',
        'nics': 'nics',
        'disks': 'disks',
        'boot_config': 'bootConfig',
        'machine_count': 'machineCount',
        'constraints': 'constraints',
        'image_disk_constraints': 'imageDiskConstraints',
        'tags': 'tags',
        'custom_properties': 'customProperties'
    }

    def __init__(self, name=None, project_id=None, description=None, flavor=None, image=None, image_ref=None, nics=None, disks=None, boot_config=None, machine_count=None, constraints=None, image_disk_constraints=None, tags=None, custom_properties=None):  # noqa: E501
        """MachineSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._project_id = None
        self._description = None
        self._flavor = None
        self._image = None
        self._image_ref = None
        self._nics = None
        self._disks = None
        self._boot_config = None
        self._machine_count = None
        self._constraints = None
        self._image_disk_constraints = None
        self._tags = None
        self._custom_properties = None
        self.discriminator = None
        self.name = name
        self.project_id = project_id
        if description is not None:
            self.description = description
        self.flavor = flavor
        self.image = image
        self.image_ref = image_ref
        if nics is not None:
            self.nics = nics
        if disks is not None:
            self.disks = disks
        if boot_config is not None:
            self.boot_config = boot_config
        if machine_count is not None:
            self.machine_count = machine_count
        if constraints is not None:
            self.constraints = constraints
        if image_disk_constraints is not None:
            self.image_disk_constraints = image_disk_constraints
        if tags is not None:
            self.tags = tags
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def name(self):
        """Gets the name of this MachineSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MachineSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this MachineSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this MachineSpecification.  # noqa: E501

        The id of the project the current user belongs to.  # noqa: E501

        :return: The project_id of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MachineSpecification.

        The id of the project the current user belongs to.  # noqa: E501

        :param project_id: The project_id of this MachineSpecification.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this MachineSpecification.  # noqa: E501

        Describes machine within the scope of your organization and is not propagated to the cloud  # noqa: E501

        :return: The description of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MachineSpecification.

        Describes machine within the scope of your organization and is not propagated to the cloud  # noqa: E501

        :param description: The description of this MachineSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def flavor(self):
        """Gets the flavor of this MachineSpecification.  # noqa: E501

        Flavor of machine instance.  # noqa: E501

        :return: The flavor of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this MachineSpecification.

        Flavor of machine instance.  # noqa: E501

        :param flavor: The flavor of this MachineSpecification.  # noqa: E501
        :type: str
        """
        if flavor is None:
            raise ValueError("Invalid value for `flavor`, must not be `None`")  # noqa: E501

        self._flavor = flavor

    @property
    def image(self):
        """Gets the image of this MachineSpecification.  # noqa: E501

        Type of image used for this machine.  # noqa: E501

        :return: The image of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MachineSpecification.

        Type of image used for this machine.  # noqa: E501

        :param image: The image of this MachineSpecification.  # noqa: E501
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def image_ref(self):
        """Gets the image_ref of this MachineSpecification.  # noqa: E501

        Direct image reference used for this machine (name, path, location, uri, etc.). Valid if no image property is provided  # noqa: E501

        :return: The image_ref of this MachineSpecification.  # noqa: E501
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this MachineSpecification.

        Direct image reference used for this machine (name, path, location, uri, etc.). Valid if no image property is provided  # noqa: E501

        :param image_ref: The image_ref of this MachineSpecification.  # noqa: E501
        :type: str
        """
        if image_ref is None:
            raise ValueError("Invalid value for `image_ref`, must not be `None`")  # noqa: E501

        self._image_ref = image_ref

    @property
    def nics(self):
        """Gets the nics of this MachineSpecification.  # noqa: E501

        A set of network interface controller specifications for this machine. If not specified, then a default network connection will be created.  # noqa: E501

        :return: The nics of this MachineSpecification.  # noqa: E501
        :rtype: list[NetworkInterfaceSpecification]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this MachineSpecification.

        A set of network interface controller specifications for this machine. If not specified, then a default network connection will be created.  # noqa: E501

        :param nics: The nics of this MachineSpecification.  # noqa: E501
        :type: list[NetworkInterfaceSpecification]
        """

        self._nics = nics

    @property
    def disks(self):
        """Gets the disks of this MachineSpecification.  # noqa: E501

        A set of disk specifications for this machine.  # noqa: E501

        :return: The disks of this MachineSpecification.  # noqa: E501
        :rtype: list[DiskAttachmentSpecification]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this MachineSpecification.

        A set of disk specifications for this machine.  # noqa: E501

        :param disks: The disks of this MachineSpecification.  # noqa: E501
        :type: list[DiskAttachmentSpecification]
        """

        self._disks = disks

    @property
    def boot_config(self):
        """Gets the boot_config of this MachineSpecification.  # noqa: E501


        :return: The boot_config of this MachineSpecification.  # noqa: E501
        :rtype: MachineBootConfig
        """
        return self._boot_config

    @boot_config.setter
    def boot_config(self, boot_config):
        """Sets the boot_config of this MachineSpecification.


        :param boot_config: The boot_config of this MachineSpecification.  # noqa: E501
        :type: MachineBootConfig
        """

        self._boot_config = boot_config

    @property
    def machine_count(self):
        """Gets the machine_count of this MachineSpecification.  # noqa: E501

        Number of machines to provision - default 1.  # noqa: E501

        :return: The machine_count of this MachineSpecification.  # noqa: E501
        :rtype: int
        """
        return self._machine_count

    @machine_count.setter
    def machine_count(self, machine_count):
        """Sets the machine_count of this MachineSpecification.

        Number of machines to provision - default 1.  # noqa: E501

        :param machine_count: The machine_count of this MachineSpecification.  # noqa: E501
        :type: int
        """

        self._machine_count = machine_count

    @property
    def constraints(self):
        """Gets the constraints of this MachineSpecification.  # noqa: E501

        Constraints that are used to drive placement policies for the virtual machine that is produced from this specification. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :return: The constraints of this MachineSpecification.  # noqa: E501
        :rtype: list[Constraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this MachineSpecification.

        Constraints that are used to drive placement policies for the virtual machine that is produced from this specification. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :param constraints: The constraints of this MachineSpecification.  # noqa: E501
        :type: list[Constraint]
        """

        self._constraints = constraints

    @property
    def image_disk_constraints(self):
        """Gets the image_disk_constraints of this MachineSpecification.  # noqa: E501

        Constraints that are used to drive placement policies for the image disk. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :return: The image_disk_constraints of this MachineSpecification.  # noqa: E501
        :rtype: list[Constraint]
        """
        return self._image_disk_constraints

    @image_disk_constraints.setter
    def image_disk_constraints(self, image_disk_constraints):
        """Sets the image_disk_constraints of this MachineSpecification.

        Constraints that are used to drive placement policies for the image disk. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :param image_disk_constraints: The image_disk_constraints of this MachineSpecification.  # noqa: E501
        :type: list[Constraint]
        """

        self._image_disk_constraints = image_disk_constraints

    @property
    def tags(self):
        """Gets the tags of this MachineSpecification.  # noqa: E501

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :return: The tags of this MachineSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MachineSpecification.

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :param tags: The tags of this MachineSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def custom_properties(self):
        """Gets the custom_properties of this MachineSpecification.  # noqa: E501

        Additional custom properties that may be used to extend the machine.  # noqa: E501

        :return: The custom_properties of this MachineSpecification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this MachineSpecification.

        Additional custom properties that may be used to extend the machine.  # noqa: E501

        :param custom_properties: The custom_properties of this MachineSpecification.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MachineSpecification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MachineSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
