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


class VolumeTypeList(object):
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
        'volume_types': 'list[str]'
    }

    attribute_map = {
        'volume_types': 'volumeTypes'
    }

    def __init__(self, volume_types=None):  # noqa: E501
        """VolumeTypeList - a model defined in Swagger"""  # noqa: E501
        self._volume_types = None
        self.discriminator = None
        if volume_types is not None:
            self.volume_types = volume_types

    @property
    def volume_types(self):
        """Gets the volume_types of this VolumeTypeList.  # noqa: E501


        :return: The volume_types of this VolumeTypeList.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_types

    @volume_types.setter
    def volume_types(self, volume_types):
        """Sets the volume_types of this VolumeTypeList.


        :param volume_types: The volume_types of this VolumeTypeList.  # noqa: E501
        :type: list[str]
        """

        self._volume_types = volume_types

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
        if issubclass(VolumeTypeList, dict):
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
        if not isinstance(other, VolumeTypeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
