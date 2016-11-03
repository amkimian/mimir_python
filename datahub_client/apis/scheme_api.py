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


class SchemeApi(object):
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

    def create_scheme(self, admin_key, id, body, **kwargs):
        """
        
        Create a scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_scheme(admin_key, id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin api key (required)
        :param str id: The id of the scheme (required)
        :param Scheme body: DataSet object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_scheme_with_http_info(admin_key, id, body, **kwargs)
        else:
            (data) = self.create_scheme_with_http_info(admin_key, id, body, **kwargs)
            return data

    def create_scheme_with_http_info(self, admin_key, id, body, **kwargs):
        """
        
        Create a scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_scheme_with_http_info(admin_key, id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin api key (required)
        :param str id: The id of the scheme (required)
        :param Scheme body: DataSet object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['admin_key', 'id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'admin_key' is set
        if ('admin_key' not in params) or (params['admin_key'] is None):
            raise ValueError("Missing the required parameter `admin_key` when calling `create_scheme`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_scheme`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_scheme`")

        resource_path = '/scheme/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}
        if 'admin_key' in params:
            header_params['admin_key'] = params['admin_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

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

    def delete_scheme(self, admin_key, id, **kwargs):
        """
        Remove a scheme
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_scheme(admin_key, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin key (required)
        :param str id: The id of the scheme (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_scheme_with_http_info(admin_key, id, **kwargs)
        else:
            (data) = self.delete_scheme_with_http_info(admin_key, id, **kwargs)
            return data

    def delete_scheme_with_http_info(self, admin_key, id, **kwargs):
        """
        Remove a scheme
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_scheme_with_http_info(admin_key, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin key (required)
        :param str id: The id of the scheme (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['admin_key', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'admin_key' is set
        if ('admin_key' not in params) or (params['admin_key'] is None):
            raise ValueError("Missing the required parameter `admin_key` when calling `delete_scheme`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_scheme`")

        resource_path = '/scheme/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}
        if 'admin_key' in params:
            header_params['admin_key'] = params['admin_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
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

    def get_scheme(self, api_key, id, **kwargs):
        """
        
        retrieve a scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scheme(api_key, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: user api key (required)
        :param str id: The id of the scheme (required)
        :return: Scheme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_scheme_with_http_info(api_key, id, **kwargs)
        else:
            (data) = self.get_scheme_with_http_info(api_key, id, **kwargs)
            return data

    def get_scheme_with_http_info(self, api_key, id, **kwargs):
        """
        
        retrieve a scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scheme_with_http_info(api_key, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: user api key (required)
        :param str id: The id of the scheme (required)
        :return: Scheme
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_scheme`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_scheme`")

        resource_path = '/scheme/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Scheme',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_schemes(self, admin_key, **kwargs):
        """
        
        Retrieve schemes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_schemes(admin_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin api key (required)
        :param int page: The page of schemes to return
        :param int limit: The limit of schemes to return (the page size)
        :return: list[Scheme]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_schemes_with_http_info(admin_key, **kwargs)
        else:
            (data) = self.get_schemes_with_http_info(admin_key, **kwargs)
            return data

    def get_schemes_with_http_info(self, admin_key, **kwargs):
        """
        
        Retrieve schemes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_schemes_with_http_info(admin_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str admin_key: The admin api key (required)
        :param int page: The page of schemes to return
        :param int limit: The limit of schemes to return (the page size)
        :return: list[Scheme]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['admin_key', 'page', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schemes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'admin_key' is set
        if ('admin_key' not in params) or (params['admin_key'] is None):
            raise ValueError("Missing the required parameter `admin_key` when calling `get_schemes`")

        resource_path = '/schemes/get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}
        if 'admin_key' in params:
            header_params['admin_key'] = params['admin_key']

        form_params = []
        local_var_files = {}

        body_params = None

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Scheme]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_scheme(self, api_key, id, body, **kwargs):
        """
        Update an existing scheme.
        Update scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_scheme(api_key, id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str id: The id of the scheme (required)
        :param Scheme body: Scheme object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_scheme_with_http_info(api_key, id, body, **kwargs)
        else:
            (data) = self.update_scheme_with_http_info(api_key, id, body, **kwargs)
            return data

    def update_scheme_with_http_info(self, api_key, id, body, **kwargs):
        """
        Update an existing scheme.
        Update scheme

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_scheme_with_http_info(api_key, id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str id: The id of the scheme (required)
        :param Scheme body: Scheme object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_scheme`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_scheme`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_scheme`")

        resource_path = '/scheme/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
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
