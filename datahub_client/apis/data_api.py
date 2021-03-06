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


class DataApi(object):
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

    def get_csv_data(self, api_key, owner, dataset, release, element, **kwargs):
        """
        
        Returns a block of CSV data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_csv_data(api_key, owner, dataset, release, element, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param bool with_header: Whether to include headers (row 0)
        :param int skip: which page to show
        :param int limit: How many records to return
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_csv_data_with_http_info(api_key, owner, dataset, release, element, **kwargs)
        else:
            (data) = self.get_csv_data_with_http_info(api_key, owner, dataset, release, element, **kwargs)
            return data

    def get_csv_data_with_http_info(self, api_key, owner, dataset, release, element, **kwargs):
        """
        
        Returns a block of CSV data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_csv_data_with_http_info(api_key, owner, dataset, release, element, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param bool with_header: Whether to include headers (row 0)
        :param int skip: which page to show
        :param int limit: How many records to return
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset', 'release', 'element', 'with_header', 'skip', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_csv_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_csv_data`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_csv_data`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_csv_data`")
        # verify the required parameter 'release' is set
        if ('release' not in params) or (params['release'] is None):
            raise ValueError("Missing the required parameter `release` when calling `get_csv_data`")
        # verify the required parameter 'element' is set
        if ('element' not in params) or (params['element'] is None):
            raise ValueError("Missing the required parameter `element` when calling `get_csv_data`")

        resource_path = '/data/{owner}/{dataset}/{release}/{element}/getCSVBlock'.replace('{format}', 'json')
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
        if 'with_header' in params:
            query_params['withHeader'] = params['with_header']
        if 'skip' in params:
            query_params['skip'] = params['skip']
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
            select_header_accept(['text/plain'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

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

    def put_csv_data(self, api_key, owner, dataset, release, element, data, **kwargs):
        """
        
        Writes a block of CSV data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_csv_data(api_key, owner, dataset, release, element, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param str data: The CSV data to write (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_csv_data_with_http_info(api_key, owner, dataset, release, element, data, **kwargs)
        else:
            (data) = self.put_csv_data_with_http_info(api_key, owner, dataset, release, element, data, **kwargs)
            return data

    def put_csv_data_with_http_info(self, api_key, owner, dataset, release, element, data, **kwargs):
        """
        
        Writes a block of CSV data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_csv_data_with_http_info(api_key, owner, dataset, release, element, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param str data: The CSV data to write (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset', 'release', 'element', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_csv_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `put_csv_data`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `put_csv_data`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `put_csv_data`")
        # verify the required parameter 'release' is set
        if ('release' not in params) or (params['release'] is None):
            raise ValueError("Missing the required parameter `release` when calling `put_csv_data`")
        # verify the required parameter 'element' is set
        if ('element' not in params) or (params['element'] is None):
            raise ValueError("Missing the required parameter `element` when calling `put_csv_data`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `put_csv_data`")

        resource_path = '/data/{owner}/{dataset}/{release}/{element}/csv'.replace('{format}', 'json')
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

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GeneralStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def put_kv_data(self, api_key, owner, dataset, release, element, fields, **kwargs):
        """
        
        Writes a block of key/value style data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_kv_data(api_key, owner, dataset, release, element, fields, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param KVBody fields:  (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_kv_data_with_http_info(api_key, owner, dataset, release, element, fields, **kwargs)
        else:
            (data) = self.put_kv_data_with_http_info(api_key, owner, dataset, release, element, fields, **kwargs)
            return data

    def put_kv_data_with_http_info(self, api_key, owner, dataset, release, element, fields, **kwargs):
        """
        
        Writes a block of key/value style data

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_kv_data_with_http_info(api_key, owner, dataset, release, element, fields, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :param str release: The name of the release (required)
        :param str element: The element name (required)
        :param KVBody fields:  (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset', 'release', 'element', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_kv_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `put_kv_data`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `put_kv_data`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `put_kv_data`")
        # verify the required parameter 'release' is set
        if ('release' not in params) or (params['release'] is None):
            raise ValueError("Missing the required parameter `release` when calling `put_kv_data`")
        # verify the required parameter 'element' is set
        if ('element' not in params) or (params['element'] is None):
            raise ValueError("Missing the required parameter `element` when calling `put_kv_data`")
        # verify the required parameter 'fields' is set
        if ('fields' not in params) or (params['fields'] is None):
            raise ValueError("Missing the required parameter `fields` when calling `put_kv_data`")

        resource_path = '/data/{owner}/{dataset}/{release}/{element}/kv'.replace('{format}', 'json')
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

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fields' in params:
            body_params = params['fields']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GeneralStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
