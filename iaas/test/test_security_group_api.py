# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.security_group_api import SecurityGroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSecurityGroupApi(unittest.TestCase):
    """SecurityGroupApi unit test stubs"""

    def setUp(self):
        self.api = api.security_group_api.SecurityGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_security_group(self):
        """Test case for get_security_group

        Get security group  # noqa: E501
        """
        pass

    def test_get_security_groups(self):
        """Test case for get_security_groups

        Get security groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()