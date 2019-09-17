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
from api.login_api import LoginApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_auth_token(self):
        """Test case for retrieve_auth_token

        Retrieve AuthToken for local csp users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()