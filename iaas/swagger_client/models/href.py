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


class Href(object):
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
        'href': 'str',
        'hrefs': 'list[str]'
    }

    attribute_map = {
        'href': 'href',
        'hrefs': 'hrefs'
    }

    def __init__(self, href=None, hrefs=None):  # noqa: E501
        """Href - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._hrefs = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if hrefs is not None:
            self.hrefs = hrefs

    @property
    def href(self):
        """Gets the href of this Href.  # noqa: E501


        :return: The href of this Href.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Href.


        :param href: The href of this Href.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def hrefs(self):
        """Gets the hrefs of this Href.  # noqa: E501


        :return: The hrefs of this Href.  # noqa: E501
        :rtype: list[str]
        """
        return self._hrefs

    @hrefs.setter
    def hrefs(self, hrefs):
        """Sets the hrefs of this Href.


        :param hrefs: The hrefs of this Href.  # noqa: E501
        :type: list[str]
        """

        self._hrefs = hrefs

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
        if issubclass(Href, dict):
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
        if not isinstance(other, Href):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
