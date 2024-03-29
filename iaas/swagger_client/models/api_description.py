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
from swagger_client.models.deprecation_policy import DeprecationPolicy  # noqa: F401,E501


class ApiDescription(object):
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
        'api_version': 'str',
        'documentation_link': 'str',
        'deprecation_policy': 'DeprecationPolicy'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'documentation_link': 'documentationLink',
        'deprecation_policy': 'deprecationPolicy'
    }

    def __init__(self, api_version=None, documentation_link=None, deprecation_policy=None):  # noqa: E501
        """ApiDescription - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._documentation_link = None
        self._deprecation_policy = None
        self.discriminator = None
        self.api_version = api_version
        self.documentation_link = documentation_link
        if deprecation_policy is not None:
            self.deprecation_policy = deprecation_policy

    @property
    def api_version(self):
        """Gets the api_version of this ApiDescription.  # noqa: E501

        The version of the API in yyyy-MM-dd format (UTC).  # noqa: E501

        :return: The api_version of this ApiDescription.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ApiDescription.

        The version of the API in yyyy-MM-dd format (UTC).  # noqa: E501

        :param api_version: The api_version of this ApiDescription.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def documentation_link(self):
        """Gets the documentation_link of this ApiDescription.  # noqa: E501

        The link to the documentation of this api version  # noqa: E501

        :return: The documentation_link of this ApiDescription.  # noqa: E501
        :rtype: str
        """
        return self._documentation_link

    @documentation_link.setter
    def documentation_link(self, documentation_link):
        """Sets the documentation_link of this ApiDescription.

        The link to the documentation of this api version  # noqa: E501

        :param documentation_link: The documentation_link of this ApiDescription.  # noqa: E501
        :type: str
        """
        if documentation_link is None:
            raise ValueError("Invalid value for `documentation_link`, must not be `None`")  # noqa: E501

        self._documentation_link = documentation_link

    @property
    def deprecation_policy(self):
        """Gets the deprecation_policy of this ApiDescription.  # noqa: E501


        :return: The deprecation_policy of this ApiDescription.  # noqa: E501
        :rtype: DeprecationPolicy
        """
        return self._deprecation_policy

    @deprecation_policy.setter
    def deprecation_policy(self, deprecation_policy):
        """Sets the deprecation_policy of this ApiDescription.


        :param deprecation_policy: The deprecation_policy of this ApiDescription.  # noqa: E501
        :type: DeprecationPolicy
        """

        self._deprecation_policy = deprecation_policy

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
        if issubclass(ApiDescription, dict):
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
        if not isinstance(other, ApiDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
