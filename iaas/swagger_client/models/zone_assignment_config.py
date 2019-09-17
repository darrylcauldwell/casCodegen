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


class ZoneAssignmentConfig(object):
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
        'zone_id': 'str',
        'priority': 'int',
        'max_number_instances': 'int'
    }

    attribute_map = {
        'zone_id': 'zoneId',
        'priority': 'priority',
        'max_number_instances': 'maxNumberInstances'
    }

    def __init__(self, zone_id=None, priority=None, max_number_instances=None):  # noqa: E501
        """ZoneAssignmentConfig - a model defined in Swagger"""  # noqa: E501
        self._zone_id = None
        self._priority = None
        self._max_number_instances = None
        self.discriminator = None
        if zone_id is not None:
            self.zone_id = zone_id
        if priority is not None:
            self.priority = priority
        if max_number_instances is not None:
            self.max_number_instances = max_number_instances

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneAssignmentConfig.  # noqa: E501

        The Cloud Zone Id  # noqa: E501

        :return: The zone_id of this ZoneAssignmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneAssignmentConfig.

        The Cloud Zone Id  # noqa: E501

        :param zone_id: The zone_id of this ZoneAssignmentConfig.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def priority(self):
        """Gets the priority of this ZoneAssignmentConfig.  # noqa: E501

        The priority of this zone in the current project. Lower numbers mean higher priority. Default is 0 (highest)  # noqa: E501

        :return: The priority of this ZoneAssignmentConfig.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ZoneAssignmentConfig.

        The priority of this zone in the current project. Lower numbers mean higher priority. Default is 0 (highest)  # noqa: E501

        :param priority: The priority of this ZoneAssignmentConfig.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def max_number_instances(self):
        """Gets the max_number_instances of this ZoneAssignmentConfig.  # noqa: E501

        The maximum number of instances that can be provisioned in this cloud zone. Default is 0 (unlimited instances).  # noqa: E501

        :return: The max_number_instances of this ZoneAssignmentConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_number_instances

    @max_number_instances.setter
    def max_number_instances(self, max_number_instances):
        """Sets the max_number_instances of this ZoneAssignmentConfig.

        The maximum number of instances that can be provisioned in this cloud zone. Default is 0 (unlimited instances).  # noqa: E501

        :param max_number_instances: The max_number_instances of this ZoneAssignmentConfig.  # noqa: E501
        :type: int
        """

        self._max_number_instances = max_number_instances

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
        if issubclass(ZoneAssignmentConfig, dict):
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
        if not isinstance(other, ZoneAssignmentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other