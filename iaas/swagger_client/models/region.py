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


class Region(object):
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
        'external_region_id': 'str',
        'cloud_account_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'owner': 'owner',
        'organization_id': 'organizationId',
        'org_id': 'orgId',
        'links': '_links',
        'external_region_id': 'externalRegionId',
        'cloud_account_id': 'cloudAccountId'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, owner=None, organization_id=None, org_id=None, links=None, external_region_id=None, cloud_account_id=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._owner = None
        self._organization_id = None
        self._org_id = None
        self._links = None
        self._external_region_id = None
        self._cloud_account_id = None
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
        self.external_region_id = external_region_id
        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id

    @property
    def id(self):
        """Gets the id of this Region.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.

        The id of this resource instance  # noqa: E501

        :param id: The id of this Region.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Region.  # noqa: E501

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :return: The created_at of this Region.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Region.

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :param created_at: The created_at of this Region.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Region.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this Region.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Region.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this Region.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this Region.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this Region.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Region.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this Region.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def organization_id(self):
        """Gets the organization_id of this Region.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Region.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this Region.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def org_id(self):
        """Gets the org_id of this Region.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Region.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this Region.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def links(self):
        """Gets the links of this Region.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this Region.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Region.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this Region.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def external_region_id(self):
        """Gets the external_region_id of this Region.  # noqa: E501

        Unique identifier of region on the provider side.  # noqa: E501

        :return: The external_region_id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._external_region_id

    @external_region_id.setter
    def external_region_id(self, external_region_id):
        """Sets the external_region_id of this Region.

        Unique identifier of region on the provider side.  # noqa: E501

        :param external_region_id: The external_region_id of this Region.  # noqa: E501
        :type: str
        """
        if external_region_id is None:
            raise ValueError("Invalid value for `external_region_id`, must not be `None`")  # noqa: E501

        self._external_region_id = external_region_id

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this Region.  # noqa: E501

        The id of the cloud account this region belongs to.  # noqa: E501

        :return: The cloud_account_id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this Region.

        The id of the cloud account this region belongs to.  # noqa: E501

        :param cloud_account_id: The cloud_account_id of this Region.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

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
        if issubclass(Region, dict):
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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
