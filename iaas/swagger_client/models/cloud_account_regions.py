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


class CloudAccountRegions(object):
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
        'external_region_ids': 'list[str]'
    }

    attribute_map = {
        'external_region_ids': 'externalRegionIds'
    }

    def __init__(self, external_region_ids=None):  # noqa: E501
        """CloudAccountRegions - a model defined in Swagger"""  # noqa: E501
        self._external_region_ids = None
        self.discriminator = None
        self.external_region_ids = external_region_ids

    @property
    def external_region_ids(self):
        """Gets the external_region_ids of this CloudAccountRegions.  # noqa: E501

        A set of region ids for the cloud account.  # noqa: E501

        :return: The external_region_ids of this CloudAccountRegions.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_region_ids

    @external_region_ids.setter
    def external_region_ids(self, external_region_ids):
        """Sets the external_region_ids of this CloudAccountRegions.

        A set of region ids for the cloud account.  # noqa: E501

        :param external_region_ids: The external_region_ids of this CloudAccountRegions.  # noqa: E501
        :type: list[str]
        """
        if external_region_ids is None:
            raise ValueError("Invalid value for `external_region_ids`, must not be `None`")  # noqa: E501

        self._external_region_ids = external_region_ids

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
        if issubclass(CloudAccountRegions, dict):
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
        if not isinstance(other, CloudAccountRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
