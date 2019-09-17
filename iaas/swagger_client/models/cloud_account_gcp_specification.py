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


class CloudAccountGcpSpecification(object):
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
        'project_id': 'str',
        'private_key_id': 'str',
        'private_key': 'str',
        'client_email': 'str',
        'region_ids': 'list[str]',
        'create_default_zones': 'bool',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'project_id': 'projectId',
        'private_key_id': 'privateKeyId',
        'private_key': 'privateKey',
        'client_email': 'clientEmail',
        'region_ids': 'regionIds',
        'create_default_zones': 'createDefaultZones',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, project_id=None, private_key_id=None, private_key=None, client_email=None, region_ids=None, create_default_zones=None, tags=None):  # noqa: E501
        """CloudAccountGcpSpecification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._project_id = None
        self._private_key_id = None
        self._private_key = None
        self._client_email = None
        self._region_ids = None
        self._create_default_zones = None
        self._tags = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.project_id = project_id
        self.private_key_id = private_key_id
        self.private_key = private_key
        self.client_email = client_email
        self.region_ids = region_ids
        if create_default_zones is not None:
            self.create_default_zones = create_default_zones
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CloudAccountGcpSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountGcpSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CloudAccountGcpSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudAccountGcpSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this CloudAccountGcpSpecification.  # noqa: E501

        GCP Project ID  # noqa: E501

        :return: The project_id of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CloudAccountGcpSpecification.

        GCP Project ID  # noqa: E501

        :param project_id: The project_id of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def private_key_id(self):
        """Gets the private_key_id of this CloudAccountGcpSpecification.  # noqa: E501

        GCP Private key ID  # noqa: E501

        :return: The private_key_id of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._private_key_id

    @private_key_id.setter
    def private_key_id(self, private_key_id):
        """Sets the private_key_id of this CloudAccountGcpSpecification.

        GCP Private key ID  # noqa: E501

        :param private_key_id: The private_key_id of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """
        if private_key_id is None:
            raise ValueError("Invalid value for `private_key_id`, must not be `None`")  # noqa: E501

        self._private_key_id = private_key_id

    @property
    def private_key(self):
        """Gets the private_key of this CloudAccountGcpSpecification.  # noqa: E501

        GCP Private key  # noqa: E501

        :return: The private_key of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CloudAccountGcpSpecification.

        GCP Private key  # noqa: E501

        :param private_key: The private_key of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """
        if private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")  # noqa: E501

        self._private_key = private_key

    @property
    def client_email(self):
        """Gets the client_email of this CloudAccountGcpSpecification.  # noqa: E501

        GCP Client email  # noqa: E501

        :return: The client_email of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: str
        """
        return self._client_email

    @client_email.setter
    def client_email(self, client_email):
        """Sets the client_email of this CloudAccountGcpSpecification.

        GCP Client email  # noqa: E501

        :param client_email: The client_email of this CloudAccountGcpSpecification.  # noqa: E501
        :type: str
        """
        if client_email is None:
            raise ValueError("Invalid value for `client_email`, must not be `None`")  # noqa: E501

        self._client_email = client_email

    @property
    def region_ids(self):
        """Gets the region_ids of this CloudAccountGcpSpecification.  # noqa: E501

        A set of Region names to enable provisioning on. Refer to /iaas/cloud-accounts-gcp/region-enumeration.  # noqa: E501

        :return: The region_ids of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        """Sets the region_ids of this CloudAccountGcpSpecification.

        A set of Region names to enable provisioning on. Refer to /iaas/cloud-accounts-gcp/region-enumeration.  # noqa: E501

        :param region_ids: The region_ids of this CloudAccountGcpSpecification.  # noqa: E501
        :type: list[str]
        """
        if region_ids is None:
            raise ValueError("Invalid value for `region_ids`, must not be `None`")  # noqa: E501

        self._region_ids = region_ids

    @property
    def create_default_zones(self):
        """Gets the create_default_zones of this CloudAccountGcpSpecification.  # noqa: E501

        Create default cloud zones for the enabled regions.  # noqa: E501

        :return: The create_default_zones of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._create_default_zones

    @create_default_zones.setter
    def create_default_zones(self, create_default_zones):
        """Sets the create_default_zones of this CloudAccountGcpSpecification.

        Create default cloud zones for the enabled regions.  # noqa: E501

        :param create_default_zones: The create_default_zones of this CloudAccountGcpSpecification.  # noqa: E501
        :type: bool
        """

        self._create_default_zones = create_default_zones

    @property
    def tags(self):
        """Gets the tags of this CloudAccountGcpSpecification.  # noqa: E501

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :return: The tags of this CloudAccountGcpSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudAccountGcpSpecification.

        A set of tag keys and optional values to set on the Cloud Account  # noqa: E501

        :param tags: The tags of this CloudAccountGcpSpecification.  # noqa: E501
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
        if issubclass(CloudAccountGcpSpecification, dict):
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
        if not isinstance(other, CloudAccountGcpSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
