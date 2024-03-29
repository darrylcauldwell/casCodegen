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
from swagger_client.models.tag import Tag  # noqa: F401,E501


class ZoneSpecification(object):
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
        'description': 'str',
        'region_id': 'str',
        'placement_policy': 'str',
        'tags': 'list[Tag]',
        'tags_to_match': 'list[Tag]',
        'custom_properties': 'dict(str, str)',
        'folder': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'region_id': 'regionId',
        'placement_policy': 'placementPolicy',
        'tags': 'tags',
        'tags_to_match': 'tagsToMatch',
        'custom_properties': 'customProperties',
        'folder': 'folder'
    }

    def __init__(self, name=None, description=None, region_id=None, placement_policy=None, tags=None, tags_to_match=None, custom_properties=None, folder=None):  # noqa: E501
        """ZoneSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._region_id = None
        self._placement_policy = None
        self._tags = None
        self._tags_to_match = None
        self._custom_properties = None
        self._folder = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.region_id = region_id
        if placement_policy is not None:
            self.placement_policy = placement_policy
        if tags is not None:
            self.tags = tags
        if tags_to_match is not None:
            self.tags_to_match = tags_to_match
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if folder is not None:
            self.folder = folder

    @property
    def name(self):
        """Gets the name of this ZoneSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this ZoneSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ZoneSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this ZoneSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ZoneSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this ZoneSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ZoneSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this ZoneSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def region_id(self):
        """Gets the region_id of this ZoneSpecification.  # noqa: E501

        The id of the region for which this profile is created  # noqa: E501

        :return: The region_id of this ZoneSpecification.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ZoneSpecification.

        The id of the region for which this profile is created  # noqa: E501

        :param region_id: The region_id of this ZoneSpecification.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def placement_policy(self):
        """Gets the placement_policy of this ZoneSpecification.  # noqa: E501

        Placement policy for the zone. One of DEFAULT, SPREAD or BINPACK.  # noqa: E501

        :return: The placement_policy of this ZoneSpecification.  # noqa: E501
        :rtype: str
        """
        return self._placement_policy

    @placement_policy.setter
    def placement_policy(self, placement_policy):
        """Sets the placement_policy of this ZoneSpecification.

        Placement policy for the zone. One of DEFAULT, SPREAD or BINPACK.  # noqa: E501

        :param placement_policy: The placement_policy of this ZoneSpecification.  # noqa: E501
        :type: str
        """

        self._placement_policy = placement_policy

    @property
    def tags(self):
        """Gets the tags of this ZoneSpecification.  # noqa: E501

        A set of tag keys and optional values that are effectively applied to all compute resources in this zone, but only in the context of this zone.  # noqa: E501

        :return: The tags of this ZoneSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ZoneSpecification.

        A set of tag keys and optional values that are effectively applied to all compute resources in this zone, but only in the context of this zone.  # noqa: E501

        :param tags: The tags of this ZoneSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def tags_to_match(self):
        """Gets the tags_to_match of this ZoneSpecification.  # noqa: E501

        A set of tag keys and optional values that will be used   # noqa: E501

        :return: The tags_to_match of this ZoneSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags_to_match

    @tags_to_match.setter
    def tags_to_match(self, tags_to_match):
        """Sets the tags_to_match of this ZoneSpecification.

        A set of tag keys and optional values that will be used   # noqa: E501

        :param tags_to_match: The tags_to_match of this ZoneSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags_to_match = tags_to_match

    @property
    def custom_properties(self):
        """Gets the custom_properties of this ZoneSpecification.  # noqa: E501

        A list of key value pair of properties that will  be used  # noqa: E501

        :return: The custom_properties of this ZoneSpecification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this ZoneSpecification.

        A list of key value pair of properties that will  be used  # noqa: E501

        :param custom_properties: The custom_properties of this ZoneSpecification.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def folder(self):
        """Gets the folder of this ZoneSpecification.  # noqa: E501

        The folder relative path to the datacenter where resources are deployed to. (only applicable for vSphere cloud zones)  # noqa: E501

        :return: The folder of this ZoneSpecification.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this ZoneSpecification.

        The folder relative path to the datacenter where resources are deployed to. (only applicable for vSphere cloud zones)  # noqa: E501

        :param folder: The folder of this ZoneSpecification.  # noqa: E501
        :type: str
        """

        self._folder = folder

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
        if issubclass(ZoneSpecification, dict):
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
        if not isinstance(other, ZoneSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
