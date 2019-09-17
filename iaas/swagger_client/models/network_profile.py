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
from swagger_client.models.href import Href  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class NetworkProfile(object):
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
        'id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'owner': 'str',
        'organization_id': 'str',
        'org_id': 'str',
        'links': 'dict(str, Href)',
        'name': 'str',
        'description': 'str',
        'external_region_id': 'str',
        'isolation_type': 'str',
        'isolation_network_domain_cidr': 'str',
        'isolated_network_cidr_prefix': 'int',
        'tags': 'list[Tag]',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'owner': 'owner',
        'organization_id': 'organizationId',
        'org_id': 'orgId',
        'links': '_links',
        'name': 'name',
        'description': 'description',
        'external_region_id': 'externalRegionId',
        'isolation_type': 'isolationType',
        'isolation_network_domain_cidr': 'isolationNetworkDomainCIDR',
        'isolated_network_cidr_prefix': 'isolatedNetworkCIDRPrefix',
        'tags': 'tags',
        'custom_properties': 'customProperties'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, owner=None, organization_id=None, org_id=None, links=None, name=None, description=None, external_region_id=None, isolation_type=None, isolation_network_domain_cidr=None, isolated_network_cidr_prefix=None, tags=None, custom_properties=None):  # noqa: E501
        """NetworkProfile - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._owner = None
        self._organization_id = None
        self._org_id = None
        self._links = None
        self._name = None
        self._description = None
        self._external_region_id = None
        self._isolation_type = None
        self._isolation_network_domain_cidr = None
        self._isolated_network_cidr_prefix = None
        self._tags = None
        self._custom_properties = None
        self.discriminator = None
        self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if owner is not None:
            self.owner = owner
        if organization_id is not None:
            self.organization_id = organization_id
        if org_id is not None:
            self.org_id = org_id
        self.links = links
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if external_region_id is not None:
            self.external_region_id = external_region_id
        if isolation_type is not None:
            self.isolation_type = isolation_type
        if isolation_network_domain_cidr is not None:
            self.isolation_network_domain_cidr = isolation_network_domain_cidr
        if isolated_network_cidr_prefix is not None:
            self.isolated_network_cidr_prefix = isolated_network_cidr_prefix
        if tags is not None:
            self.tags = tags
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def id(self):
        """Gets the id of this NetworkProfile.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkProfile.

        The id of this resource instance  # noqa: E501

        :param id: The id of this NetworkProfile.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this NetworkProfile.  # noqa: E501

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :return: The created_at of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NetworkProfile.

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :param created_at: The created_at of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NetworkProfile.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NetworkProfile.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this NetworkProfile.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this NetworkProfile.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def organization_id(self):
        """Gets the organization_id of this NetworkProfile.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this NetworkProfile.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def org_id(self):
        """Gets the org_id of this NetworkProfile.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this NetworkProfile.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def links(self):
        """Gets the links of this NetworkProfile.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this NetworkProfile.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NetworkProfile.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this NetworkProfile.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def name(self):
        """Gets the name of this NetworkProfile.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkProfile.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this NetworkProfile.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkProfile.

        A human-friendly description.  # noqa: E501

        :param description: The description of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_region_id(self):
        """Gets the external_region_id of this NetworkProfile.  # noqa: E501

        The id of the region for which this profile is defined  # noqa: E501

        :return: The external_region_id of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._external_region_id

    @external_region_id.setter
    def external_region_id(self, external_region_id):
        """Sets the external_region_id of this NetworkProfile.

        The id of the region for which this profile is defined  # noqa: E501

        :param external_region_id: The external_region_id of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._external_region_id = external_region_id

    @property
    def isolation_type(self):
        """Gets the isolation_type of this NetworkProfile.  # noqa: E501

        Specifies the isolation type e.g. none, subnet or security group  # noqa: E501

        :return: The isolation_type of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._isolation_type

    @isolation_type.setter
    def isolation_type(self, isolation_type):
        """Sets the isolation_type of this NetworkProfile.

        Specifies the isolation type e.g. none, subnet or security group  # noqa: E501

        :param isolation_type: The isolation_type of this NetworkProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "SUBNET", "SECURITY_GROUP"]  # noqa: E501
        if isolation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `isolation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(isolation_type, allowed_values)
            )

        self._isolation_type = isolation_type

    @property
    def isolation_network_domain_cidr(self):
        """Gets the isolation_network_domain_cidr of this NetworkProfile.  # noqa: E501

        CIDR of the isolation network domain.  # noqa: E501

        :return: The isolation_network_domain_cidr of this NetworkProfile.  # noqa: E501
        :rtype: str
        """
        return self._isolation_network_domain_cidr

    @isolation_network_domain_cidr.setter
    def isolation_network_domain_cidr(self, isolation_network_domain_cidr):
        """Sets the isolation_network_domain_cidr of this NetworkProfile.

        CIDR of the isolation network domain.  # noqa: E501

        :param isolation_network_domain_cidr: The isolation_network_domain_cidr of this NetworkProfile.  # noqa: E501
        :type: str
        """

        self._isolation_network_domain_cidr = isolation_network_domain_cidr

    @property
    def isolated_network_cidr_prefix(self):
        """Gets the isolated_network_cidr_prefix of this NetworkProfile.  # noqa: E501

        The CIDR prefix length to be used for the isolated networks that are created with the network profile.  # noqa: E501

        :return: The isolated_network_cidr_prefix of this NetworkProfile.  # noqa: E501
        :rtype: int
        """
        return self._isolated_network_cidr_prefix

    @isolated_network_cidr_prefix.setter
    def isolated_network_cidr_prefix(self, isolated_network_cidr_prefix):
        """Sets the isolated_network_cidr_prefix of this NetworkProfile.

        The CIDR prefix length to be used for the isolated networks that are created with the network profile.  # noqa: E501

        :param isolated_network_cidr_prefix: The isolated_network_cidr_prefix of this NetworkProfile.  # noqa: E501
        :type: int
        """

        self._isolated_network_cidr_prefix = isolated_network_cidr_prefix

    @property
    def tags(self):
        """Gets the tags of this NetworkProfile.  # noqa: E501

        A set of tag keys and optional values that were set on this Network Profile.  # noqa: E501

        :return: The tags of this NetworkProfile.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NetworkProfile.

        A set of tag keys and optional values that were set on this Network Profile.  # noqa: E501

        :param tags: The tags of this NetworkProfile.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def custom_properties(self):
        """Gets the custom_properties of this NetworkProfile.  # noqa: E501

        Additional properties that may be used to extend the Network Profile object.  # noqa: E501

        :return: The custom_properties of this NetworkProfile.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this NetworkProfile.

        Additional properties that may be used to extend the Network Profile object.  # noqa: E501

        :param custom_properties: The custom_properties of this NetworkProfile.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

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
        if issubclass(NetworkProfile, dict):
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
        if not isinstance(other, NetworkProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
