# coding: utf-8

"""
    DataHub API

    DataHub API

    OpenAPI spec version: 0.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class QueryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def query_data(self, api_key, owner, dataset, release, element, query, **kwargs):
        """
        
        Querys data in a KV element

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_data(api_key, owner, dataset, release, element, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner:  (required)
        :param str dataset:  (required)
        :param str release:  (required)
        :param str element:  (required)
        :param str query: The query, currently a string rep of a JSON mongo query (required)
        :param int page: The page of data to return
        :param int limit: The maximum rows to return
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_data_with_http_info(api_key, owner, dataset, release, element, query, **kwargs)
        else:
            (data) = self.query_data_with_http_info(api_key, owner, dataset, release, element, query, **kwargs)
            return data

    def query_data_with_http_info(self, api_key, owner, dataset, release, element, query, **kwargs):
        """
        
        Querys data in a KV element

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_data_with_http_info(api_key, owner, dataset, release, element, query, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner:  (required)
        :param str dataset:  (required)
        :param str release:  (required)
        :param str element:  (required)
        :param str query: The query, currently a string rep of a JSON mongo query (required)
        :param int page: The page of data to return
        :param int limit: The maximum rows to return
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset', 'release', 'element', 'query', 'page', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `query_data`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `query_data`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `query_data`")
        # verify the required parameter 'release' is set
        if ('release' not in params) or (params['release'] is None):
            raise ValueError("Missing the required parameter `release` when calling `query_data`")
        # verify the required parameter 'element' is set
        if ('element' not in params) or (params['element'] is None):
            raise ValueError("Missing the required parameter `element` when calling `query_data`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `query_data`")

        resource_path = '/query/{owner}/{dataset}/{release}/{element}'.replace('{format}', 'json')
        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']
        if 'release' in params:
            path_params['release'] = params['release']
        if 'element' in params:
            path_params['element'] = params['element']

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/plain'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
