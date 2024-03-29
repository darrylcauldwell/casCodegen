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


class DataCollector(object):
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
        'dc_id': 'str',
        'ip_address': 'str',
        'name': 'str',
        'host_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'dc_id': 'dcId',
        'ip_address': 'ipAddress',
        'name': 'name',
        'host_name': 'hostName',
        'status': 'status'
    }

    def __init__(self, dc_id=None, ip_address=None, name=None, host_name=None, status=None):  # noqa: E501
        """DataCollector - a model defined in Swagger"""  # noqa: E501
        self._dc_id = None
        self._ip_address = None
        self._name = None
        self._host_name = None
        self._status = None
        self.discriminator = None
        self.dc_id = dc_id
        self.ip_address = ip_address
        self.name = name
        self.host_name = host_name
        self.status = status

    @property
    def dc_id(self):
        """Gets the dc_id of this DataCollector.  # noqa: E501

        Data collector identifier  # noqa: E501

        :return: The dc_id of this DataCollector.  # noqa: E501
        :rtype: str
        """
        return self._dc_id

    @dc_id.setter
    def dc_id(self, dc_id):
        """Sets the dc_id of this DataCollector.

        Data collector identifier  # noqa: E501

        :param dc_id: The dc_id of this DataCollector.  # noqa: E501
        :type: str
        """
        if dc_id is None:
            raise ValueError("Invalid value for `dc_id`, must not be `None`")  # noqa: E501

        self._dc_id = dc_id

    @property
    def ip_address(self):
        """Gets the ip_address of this DataCollector.  # noqa: E501

        Ip Address of the data collector VM  # noqa: E501

        :return: The ip_address of this DataCollector.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DataCollector.

        Ip Address of the data collector VM  # noqa: E501

        :param ip_address: The ip_address of this DataCollector.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def name(self):
        """Gets the name of this DataCollector.  # noqa: E501

        Data collector name  # noqa: E501

        :return: The name of this DataCollector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataCollector.

        Data collector name  # noqa: E501

        :param name: The name of this DataCollector.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def host_name(self):
        """Gets the host_name of this DataCollector.  # noqa: E501

        Data collector host name  # noqa: E501

        :return: The host_name of this DataCollector.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DataCollector.

        Data collector host name  # noqa: E501

        :param host_name: The host_name of this DataCollector.  # noqa: E501
        :type: str
        """
        if host_name is None:
            raise ValueError("Invalid value for `host_name`, must not be `None`")  # noqa: E501

        self._host_name = host_name

    @property
    def status(self):
        """Gets the status of this DataCollector.  # noqa: E501

        Current status of the data collector  # noqa: E501

        :return: The status of this DataCollector.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataCollector.

        Current status of the data collector  # noqa: E501

        :param status: The status of this DataCollector.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(DataCollector, dict):
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
        if not isinstance(other, DataCollector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
