# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LoginApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_auth_token(self, body, **kwargs):  # noqa: E501
        """Retrieve AuthToken for local csp users  # noqa: E501

        Retrieve AuthToken for local csp users. When accessing other endpoints the `Bearer` authentication scheme and the received `token` must be provided in the `Authorization` request header field as follows: `Authorization: Bearer {token}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_auth_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CspLoginSpecification body: CspLoginSpecification instance (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_auth_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_auth_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def retrieve_auth_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Retrieve AuthToken for local csp users  # noqa: E501

        Retrieve AuthToken for local csp users. When accessing other endpoints the `Bearer` authentication scheme and the received `token` must be provided in the `Authorization` request header field as follows: `Authorization: Bearer {token}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_auth_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CspLoginSpecification body: CspLoginSpecification instance (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about
        :return: AuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_auth_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `retrieve_auth_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
