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


class CloudAccountNsxVSpecification(object):
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
        'host_name': 'str',
        'dcid': 'str',
        'username': 'str',
        'password': 'str',
        'accept_self_signed_certificate': 'bool',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'host_name': 'hostName',
        'dcid': 'dcid',
        'username': 'username',
        'password': 'password',
        'accept_self_signed_certificate': 'acceptSelfSignedCertificate',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, host_name=None, dcid=None, username=None, password=None, accept_self_signed_certificate=None, tags=None):  # noqa: E501
        """CloudAccountNsxVSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._host_name = None
        self._dcid = None
        self._username = None
        self._password = None
        self._accept_self_signed_certificate = None
        self._tags = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.host_name = host_name
        self.dcid = dcid
        self.username = username
        self.password = password
        if accept_self_signed_certificate is not None:
            self.accept_self_signed_certificate = accept_self_signed_certificate
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CloudAccountNsxVSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountNsxVSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CloudAccountNsxVSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudAccountNsxVSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def host_name(self):
        """Gets the host_name of this CloudAccountNsxVSpecification.  # noqa: E501

        Host name for the Nsx-T endpoint  # noqa: E501

        :return: The host_name of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this CloudAccountNsxVSpecification.

        Host name for the Nsx-T endpoint  # noqa: E501

        :param host_name: The host_name of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """
        if host_name is None:
            raise ValueError("Invalid value for `host_name`, must not be `None`")  # noqa: E501

        self._host_name = host_name

    @property
    def dcid(self):
        """Gets the dcid of this CloudAccountNsxVSpecification.  # noqa: E501

        Identifier of a data collector vm deployed in the on premise infrastructure. Refer to the data-collector API to create or list data collectors  # noqa: E501

        :return: The dcid of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._dcid

    @dcid.setter
    def dcid(self, dcid):
        """Sets the dcid of this CloudAccountNsxVSpecification.

        Identifier of a data collector vm deployed in the on premise infrastructure. Refer to the data-collector API to create or list data collectors  # noqa: E501

        :param dcid: The dcid of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """
        if dcid is None:
            raise ValueError("Invalid value for `dcid`, must not be `None`")  # noqa: E501

        self._dcid = dcid

    @property
    def username(self):
        """Gets the username of this CloudAccountNsxVSpecification.  # noqa: E501

        Username to authenticate with the cloud account  # noqa: E501

        :return: The username of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CloudAccountNsxVSpecification.

        Username to authenticate with the cloud account  # noqa: E501

        :param username: The username of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this CloudAccountNsxVSpecification.  # noqa: E501

        Password for the user used to authenticate with the cloud Account  # noqa: E501

        :return: The password of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CloudAccountNsxVSpecification.

        Password for the user used to authenticate with the cloud Account  # noqa: E501

        :param password: The password of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def accept_self_signed_certificate(self):
        """Gets the accept_self_signed_certificate of this CloudAccountNsxVSpecification.  # noqa: E501

        Accept self signed certificate when connecting.  # noqa: E501

        :return: The accept_self_signed_certificate of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._accept_self_signed_certificate

    @accept_self_signed_certificate.setter
    def accept_self_signed_certificate(self, accept_self_signed_certificate):
        """Sets the accept_self_signed_certificate of this CloudAccountNsxVSpecification.

        Accept self signed certificate when connecting.  # noqa: E501

        :param accept_self_signed_certificate: The accept_self_signed_certificate of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: bool
        """

        self._accept_self_signed_certificate = accept_self_signed_certificate

    @property
    def tags(self):
        """Gets the tags of this CloudAccountNsxVSpecification.  # noqa: E501

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :return: The tags of this CloudAccountNsxVSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudAccountNsxVSpecification.

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :param tags: The tags of this CloudAccountNsxVSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

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
        if issubclass(CloudAccountNsxVSpecification, dict):
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
        if not isinstance(other, CloudAccountNsxVSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
