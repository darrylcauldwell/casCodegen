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


class UpdateCloudAccountAzureSpecification(object):
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
        'description': 'str',
        'tags': 'list[Tag]',
        'region_ids': 'list[str]',
        'create_default_zones': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'tags': 'tags',
        'region_ids': 'regionIds',
        'create_default_zones': 'createDefaultZones'
    }

    def __init__(self, description=None, tags=None, region_ids=None, create_default_zones=None):  # noqa: E501
        """UpdateCloudAccountAzureSpecification - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._tags = None
        self._region_ids = None
        self._create_default_zones = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if region_ids is not None:
            self.region_ids = region_ids
        if create_default_zones is not None:
            self.create_default_zones = create_default_zones

    @property
    def description(self):
        """Gets the description of this UpdateCloudAccountAzureSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCloudAccountAzureSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateCloudAccountAzureSpecification.  # noqa: E501

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :return: The tags of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateCloudAccountAzureSpecification.

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :param tags: The tags of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def region_ids(self):
        """Gets the region_ids of this UpdateCloudAccountAzureSpecification.  # noqa: E501

        A set of Region names to enable provisioning on.  # noqa: E501

        :return: The region_ids of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        """Sets the region_ids of this UpdateCloudAccountAzureSpecification.

        A set of Region names to enable provisioning on.  # noqa: E501

        :param region_ids: The region_ids of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :type: list[str]
        """

        self._region_ids = region_ids

    @property
    def create_default_zones(self):
        """Gets the create_default_zones of this UpdateCloudAccountAzureSpecification.  # noqa: E501

        Create default cloud zones for the enabled regions.  # noqa: E501

        :return: The create_default_zones of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._create_default_zones

    @create_default_zones.setter
    def create_default_zones(self, create_default_zones):
        """Sets the create_default_zones of this UpdateCloudAccountAzureSpecification.

        Create default cloud zones for the enabled regions.  # noqa: E501

        :param create_default_zones: The create_default_zones of this UpdateCloudAccountAzureSpecification.  # noqa: E501
        :type: bool
        """

        self._create_default_zones = create_default_zones

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
        if issubclass(UpdateCloudAccountAzureSpecification, dict):
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
        if not isinstance(other, UpdateCloudAccountAzureSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other