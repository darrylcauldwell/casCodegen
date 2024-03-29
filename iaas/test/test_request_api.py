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
from api.request_api import RequestApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRequestApi(unittest.TestCase):
    """RequestApi unit test stubs"""

    def setUp(self):
        self.api = api.request_api.RequestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_request(self):
        """Test case for delete_request

        Delete Request  # noqa: E501
        """
        pass

    def test_get_request_tracker(self):
        """Test case for get_request_tracker

        Get request tracker  # noqa: E501
        """
        pass

    def test_get_request_trackers(self):
        """Test case for get_request_trackers

        Get request tracker  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
