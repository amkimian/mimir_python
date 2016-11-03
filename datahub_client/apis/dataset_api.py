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


class DatasetApi(object):
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

    def add_data_set(self, user_id, body, **kwargs):
        """
        Create a new data set, associated with the given user id
        This creates a new data set that can then be added to 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_data_set(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user that this dataset is associated with (required)
        :param DataSet body: DataSet object that defines the element (required)
        :param str api_key: The user api key
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_data_set_with_http_info(user_id, body, **kwargs)
        else:
            (data) = self.add_data_set_with_http_info(user_id, body, **kwargs)
            return data

    def add_data_set_with_http_info(self, user_id, body, **kwargs):
        """
        Create a new data set, associated with the given user id
        This creates a new data set that can then be added to 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_data_set_with_http_info(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user that this dataset is associated with (required)
        :param DataSet body: DataSet object that defines the element (required)
        :param str api_key: The user api key
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body', 'api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_data_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `add_data_set`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_data_set`")

        resource_path = '/datasets/{userId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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

    def delete_data_set(self, user_id, data_set, **kwargs):
        """
        Remove a data set and all releases and elements
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_data_set(user_id, data_set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user owning this dataset (required)
        :param str data_set: The id of the dataset (required)
        :param str api_key: The user api key
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_data_set_with_http_info(user_id, data_set, **kwargs)
        else:
            (data) = self.delete_data_set_with_http_info(user_id, data_set, **kwargs)
            return data

    def delete_data_set_with_http_info(self, user_id, data_set, **kwargs):
        """
        Remove a data set and all releases and elements
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_data_set_with_http_info(user_id, data_set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user owning this dataset (required)
        :param str data_set: The id of the dataset (required)
        :param str api_key: The user api key
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'data_set', 'api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_data_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_data_set`")
        # verify the required parameter 'data_set' is set
        if ('data_set' not in params) or (params['data_set'] is None):
            raise ValueError("Missing the required parameter `data_set` when calling `delete_data_set`")

        resource_path = '/datasets/{userId}/{dataSet}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'data_set' in params:
            path_params['dataSet'] = params['data_set']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
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

    def find_data_sets_by_tags(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_data_sets_by_tags(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key
        :param list[str] tags: Tags to filter by
        :param int page: Page to return (defaults to zero)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_data_sets_by_tags_with_http_info(**kwargs)
        else:
            (data) = self.find_data_sets_by_tags_with_http_info(**kwargs)
            return data

    def find_data_sets_by_tags_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_data_sets_by_tags_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key
        :param list[str] tags: Tags to filter by
        :param int page: Page to return (defaults to zero)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'tags', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_data_sets_by_tags" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/marketplace/getByTag'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tags' in params:
            query_params['tags'] = params['tags']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DataSet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def find_user_data_sets(self, api_key, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_user_data_sets(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param list[str] tags: Tags to filter by
        :param int page: Page to return (defaults to zero)
        :param bool subscribed: If true, also return subscribed data sets
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_user_data_sets_with_http_info(api_key, **kwargs)
        else:
            (data) = self.find_user_data_sets_with_http_info(api_key, **kwargs)
            return data

    def find_user_data_sets_with_http_info(self, api_key, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_user_data_sets_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param list[str] tags: Tags to filter by
        :param int page: Page to return (defaults to zero)
        :param bool subscribed: If true, also return subscribed data sets
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'tags', 'page', 'subscribed']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_user_data_sets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `find_user_data_sets`")

        resource_path = '/user/getDataSets'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tags' in params:
            query_params['tags'] = params['tags']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'subscribed' in params:
            query_params['subscribed'] = params['subscribed']

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DataSet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_data_set_by_id(self, user_id, data_set, **kwargs):
        """
        Find a dataset for a user and a dataset
        Returns a data set

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_data_set_by_id(user_id, data_set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user owning this dataset (required)
        :param str data_set: The id of the dataset (required)
        :param str api_key: The user api key
        :return: DataSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_data_set_by_id_with_http_info(user_id, data_set, **kwargs)
        else:
            (data) = self.get_data_set_by_id_with_http_info(user_id, data_set, **kwargs)
            return data

    def get_data_set_by_id_with_http_info(self, user_id, data_set, **kwargs):
        """
        Find a dataset for a user and a dataset
        Returns a data set

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_data_set_by_id_with_http_info(user_id, data_set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The id of the user owning this dataset (required)
        :param str data_set: The id of the dataset (required)
        :param str api_key: The user api key
        :return: DataSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'data_set', 'api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_set_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_data_set_by_id`")
        # verify the required parameter 'data_set' is set
        if ('data_set' not in params) or (params['data_set'] is None):
            raise ValueError("Missing the required parameter `data_set` when calling `get_data_set_by_id`")

        resource_path = '/datasets/{userId}/{dataSet}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'data_set' in params:
            path_params['dataSet'] = params['data_set']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DataSet',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_front(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_front(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to return (defaults to zero)
        :param int limit: The maximum amount of records to be returned (the size of the page)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_front_with_http_info(**kwargs)
        else:
            (data) = self.get_front_with_http_info(**kwargs)
            return data

    def get_front_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_front_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to return (defaults to zero)
        :param int limit: The maximum amount of records to be returned (the size of the page)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_front" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/marketplace/getFront'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DataSet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_my_data_sets(self, api_key, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_my_data_sets(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param int page: Page to return (defaults to zero)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_my_data_sets_with_http_info(api_key, **kwargs)
        else:
            (data) = self.get_my_data_sets_with_http_info(api_key, **kwargs)
            return data

    def get_my_data_sets_with_http_info(self, api_key, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_my_data_sets_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param int page: Page to return (defaults to zero)
        :return: list[DataSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_my_data_sets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_my_data_sets`")

        resource_path = '/marketplace/getMyDataSets'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

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

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DataSet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_data_set(self, api_key, owner, dataset, body, **kwargs):
        """
        Update an existing data set.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_data_set(api_key, owner, dataset, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The id of the user that this dataset is associated with (required)
        :param str dataset: The data set id to update (required)
        :param DataSet body: DataSet object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_data_set_with_http_info(api_key, owner, dataset, body, **kwargs)
        else:
            (data) = self.update_data_set_with_http_info(api_key, owner, dataset, body, **kwargs)
            return data

    def update_data_set_with_http_info(self, api_key, owner, dataset, body, **kwargs):
        """
        Update an existing data set.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_data_set_with_http_info(api_key, owner, dataset, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The id of the user that this dataset is associated with (required)
        :param str dataset: The data set id to update (required)
        :param DataSet body: DataSet object that defines the element (required)
        :return: GeneralStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_data_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `update_data_set`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `update_data_set`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `update_data_set`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_data_set`")

        resource_path = '/datasets/{userId}/{dataSet}'.replace('{format}', 'json')
        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']

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
