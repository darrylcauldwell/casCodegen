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
from swagger_client.models.network_interface_specification import NetworkInterfaceSpecification  # noqa: F401,E501
from swagger_client.models.route_configuration import RouteConfiguration  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LoadBalancerSpecification(object):
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
        'project_id': 'str',
        'description': 'str',
        'routes': 'list[RouteConfiguration]',
        'nics': 'list[NetworkInterfaceSpecification]',
        'target_links': 'list[str]',
        'custom_properties': 'dict(str, str)',
        'tags': 'list[Tag]',
        'internet_facing': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'projectId',
        'description': 'description',
        'routes': 'routes',
        'nics': 'nics',
        'target_links': 'targetLinks',
        'custom_properties': 'customProperties',
        'tags': 'tags',
        'internet_facing': 'internetFacing'
    }

    def __init__(self, name=None, project_id=None, description=None, routes=None, nics=None, target_links=None, custom_properties=None, tags=None, internet_facing=None):  # noqa: E501
        """LoadBalancerSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._project_id = None
        self._description = None
        self._routes = None
        self._nics = None
        self._target_links = None
        self._custom_properties = None
        self._tags = None
        self._internet_facing = None
        self.discriminator = None
        self.name = name
        self.project_id = project_id
        if description is not None:
            self.description = description
        self.routes = routes
        self.nics = nics
        if target_links is not None:
            self.target_links = target_links
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if tags is not None:
            self.tags = tags
        if internet_facing is not None:
            self.internet_facing = internet_facing

    @property
    def name(self):
        """Gets the name of this LoadBalancerSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this LoadBalancerSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this LoadBalancerSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this LoadBalancerSpecification.  # noqa: E501

        The id of the project the current user belongs to.  # noqa: E501

        :return: The project_id of this LoadBalancerSpecification.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LoadBalancerSpecification.

        The id of the project the current user belongs to.  # noqa: E501

        :param project_id: The project_id of this LoadBalancerSpecification.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this LoadBalancerSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this LoadBalancerSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoadBalancerSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this LoadBalancerSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def routes(self):
        """Gets the routes of this LoadBalancerSpecification.  # noqa: E501

        The load balancer route configuration regarding ports and protocols.  # noqa: E501

        :return: The routes of this LoadBalancerSpecification.  # noqa: E501
        :rtype: list[RouteConfiguration]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this LoadBalancerSpecification.

        The load balancer route configuration regarding ports and protocols.  # noqa: E501

        :param routes: The routes of this LoadBalancerSpecification.  # noqa: E501
        :type: list[RouteConfiguration]
        """
        if routes is None:
            raise ValueError("Invalid value for `routes`, must not be `None`")  # noqa: E501

        self._routes = routes

    @property
    def nics(self):
        """Gets the nics of this LoadBalancerSpecification.  # noqa: E501

        A set of network interface specifications for this load balancer.  # noqa: E501

        :return: The nics of this LoadBalancerSpecification.  # noqa: E501
        :rtype: list[NetworkInterfaceSpecification]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this LoadBalancerSpecification.

        A set of network interface specifications for this load balancer.  # noqa: E501

        :param nics: The nics of this LoadBalancerSpecification.  # noqa: E501
        :type: list[NetworkInterfaceSpecification]
        """
        if nics is None:
            raise ValueError("Invalid value for `nics`, must not be `None`")  # noqa: E501

        self._nics = nics

    @property
    def target_links(self):
        """Gets the target_links of this LoadBalancerSpecification.  # noqa: E501

        A list of links to target load balancer pool members. Links can be to either a machine or a machine's network interface.  # noqa: E501

        :return: The target_links of this LoadBalancerSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_links

    @target_links.setter
    def target_links(self, target_links):
        """Sets the target_links of this LoadBalancerSpecification.

        A list of links to target load balancer pool members. Links can be to either a machine or a machine's network interface.  # noqa: E501

        :param target_links: The target_links of this LoadBalancerSpecification.  # noqa: E501
        :type: list[str]
        """

        self._target_links = target_links

    @property
    def custom_properties(self):
        """Gets the custom_properties of this LoadBalancerSpecification.  # noqa: E501

        Additional custom properties that may be used to extend the load balancer.  # noqa: E501

        :return: The custom_properties of this LoadBalancerSpecification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this LoadBalancerSpecification.

        Additional custom properties that may be used to extend the load balancer.  # noqa: E501

        :param custom_properties: The custom_properties of this LoadBalancerSpecification.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def tags(self):
        """Gets the tags of this LoadBalancerSpecification.  # noqa: E501

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :return: The tags of this LoadBalancerSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LoadBalancerSpecification.

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :param tags: The tags of this LoadBalancerSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def internet_facing(self):
        """Gets the internet_facing of this LoadBalancerSpecification.  # noqa: E501

        An Internet-facing load balancer has a publicly resolvable DNS name, so it can route requests from clients over the Internet to the instances that are registered with the load balancer.  # noqa: E501

        :return: The internet_facing of this LoadBalancerSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._internet_facing

    @internet_facing.setter
    def internet_facing(self, internet_facing):
        """Sets the internet_facing of this LoadBalancerSpecification.

        An Internet-facing load balancer has a publicly resolvable DNS name, so it can route requests from clients over the Internet to the instances that are registered with the load balancer.  # noqa: E501

        :param internet_facing: The internet_facing of this LoadBalancerSpecification.  # noqa: E501
        :type: bool
        """

        self._internet_facing = internet_facing

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
        if issubclass(LoadBalancerSpecification, dict):
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
        if not isinstance(other, LoadBalancerSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
