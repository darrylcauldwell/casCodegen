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
from swagger_client.models.fabric_image_description import FabricImageDescription  # noqa: F401,E501


class ImageProfileSpecification(object):
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
        'image_mapping': 'dict(str, FabricImageDescription)',
        'region_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'image_mapping': 'imageMapping',
        'region_id': 'regionId'
    }

    def __init__(self, name=None, description=None, image_mapping=None, region_id=None):  # noqa: E501
        """ImageProfileSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._image_mapping = None
        self._region_id = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.image_mapping = image_mapping
        self.region_id = region_id

    @property
    def name(self):
        """Gets the name of this ImageProfileSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this ImageProfileSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageProfileSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this ImageProfileSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ImageProfileSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this ImageProfileSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageProfileSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this ImageProfileSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_mapping(self):
        """Gets the image_mapping of this ImageProfileSpecification.  # noqa: E501

        Image mapping defined for the corresponding region.  # noqa: E501

        :return: The image_mapping of this ImageProfileSpecification.  # noqa: E501
        :rtype: dict(str, FabricImageDescription)
        """
        return self._image_mapping

    @image_mapping.setter
    def image_mapping(self, image_mapping):
        """Sets the image_mapping of this ImageProfileSpecification.

        Image mapping defined for the corresponding region.  # noqa: E501

        :param image_mapping: The image_mapping of this ImageProfileSpecification.  # noqa: E501
        :type: dict(str, FabricImageDescription)
        """
        if image_mapping is None:
            raise ValueError("Invalid value for `image_mapping`, must not be `None`")  # noqa: E501

        self._image_mapping = image_mapping

    @property
    def region_id(self):
        """Gets the region_id of this ImageProfileSpecification.  # noqa: E501

        The id of the region for which this profile is created  # noqa: E501

        :return: The region_id of this ImageProfileSpecification.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ImageProfileSpecification.

        The id of the region for which this profile is created  # noqa: E501

        :param region_id: The region_id of this ImageProfileSpecification.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

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
        if issubclass(ImageProfileSpecification, dict):
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
        if not isinstance(other, ImageProfileSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
