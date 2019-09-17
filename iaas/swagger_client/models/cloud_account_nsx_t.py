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


class CloudAccountNsxT(object):
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
        'host_name': 'str',
        'dcid': 'str',
        'username': 'str',
        'custom_properties': 'dict(str, str)',
        'tags': 'list[Tag]'
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
        'host_name': 'hostName',
        'dcid': 'dcid',
        'username': 'username',
        'custom_properties': 'customProperties',
        'tags': 'tags'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, owner=None, organization_id=None, org_id=None, links=None, name=None, description=None, host_name=None, dcid=None, username=None, custom_properties=None, tags=None):  # noqa: E501
        """CloudAccountNsxT - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._owner = None
        self._organization_id = None
        self._org_id = None
        self._links = None
        self._name = None
        self._description = None
        self._host_name = None
        self._dcid = None
        self._username = None
        self._custom_properties = None
        self._tags = None
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
        self.host_name = host_name
        if dcid is not None:
            self.dcid = dcid
        self.username = username
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this CloudAccountNsxT.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudAccountNsxT.

        The id of this resource instance  # noqa: E501

        :param id: The id of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this CloudAccountNsxT.  # noqa: E501

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :return: The created_at of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CloudAccountNsxT.

        Date when the entity was created. The date is in ISO 6801 and UTC.  # noqa: E501

        :param created_at: The created_at of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CloudAccountNsxT.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CloudAccountNsxT.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this CloudAccountNsxT.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CloudAccountNsxT.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def organization_id(self):
        """Gets the organization_id of this CloudAccountNsxT.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CloudAccountNsxT.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def org_id(self):
        """Gets the org_id of this CloudAccountNsxT.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CloudAccountNsxT.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def links(self):
        """Gets the links of this CloudAccountNsxT.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this CloudAccountNsxT.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CloudAccountNsxT.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this CloudAccountNsxT.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def name(self):
        """Gets the name of this CloudAccountNsxT.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountNsxT.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CloudAccountNsxT.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudAccountNsxT.

        A human-friendly description.  # noqa: E501

        :param description: The description of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def host_name(self):
        """Gets the host_name of this CloudAccountNsxT.  # noqa: E501

        Host name for the Nsx-T cloud account  # noqa: E501

        :return: The host_name of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this CloudAccountNsxT.

        Host name for the Nsx-T cloud account  # noqa: E501

        :param host_name: The host_name of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """
        if host_name is None:
            raise ValueError("Invalid value for `host_name`, must not be `None`")  # noqa: E501

        self._host_name = host_name

    @property
    def dcid(self):
        """Gets the dcid of this CloudAccountNsxT.  # noqa: E501

        Identifier of a data collector vm deployed in the on premise infrastructure.  # noqa: E501

        :return: The dcid of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._dcid

    @dcid.setter
    def dcid(self, dcid):
        """Sets the dcid of this CloudAccountNsxT.

        Identifier of a data collector vm deployed in the on premise infrastructure.  # noqa: E501

        :param dcid: The dcid of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """

        self._dcid = dcid

    @property
    def username(self):
        """Gets the username of this CloudAccountNsxT.  # noqa: E501

        Username to authenticate with the cloud account  # noqa: E501

        :return: The username of this CloudAccountNsxT.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CloudAccountNsxT.

        Username to authenticate with the cloud account  # noqa: E501

        :param username: The username of this CloudAccountNsxT.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def custom_properties(self):
        """Gets the custom_properties of this CloudAccountNsxT.  # noqa: E501

        Additional properties that may be used to extend the base type.  # noqa: E501

        :return: The custom_properties of this CloudAccountNsxT.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this CloudAccountNsxT.

        Additional properties that may be used to extend the base type.  # noqa: E501

        :param custom_properties: The custom_properties of this CloudAccountNsxT.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def tags(self):
        """Gets the tags of this CloudAccountNsxT.  # noqa: E501

        A set of tag keys and optional values that were set on the Cloud Account  # noqa: E501

        :return: The tags of this CloudAccountNsxT.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudAccountNsxT.

        A set of tag keys and optional values that were set on the Cloud Account  # noqa: E501

        :param tags: The tags of this CloudAccountNsxT.  # noqa: E501
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
        if issubclass(CloudAccountNsxT, dict):
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
        if not isinstance(other, CloudAccountNsxT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other