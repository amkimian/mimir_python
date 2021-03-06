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


class InvoiceApi(object):
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

    def add_subscription_to_invoice(self, api_key, owner, dataset, **kwargs):
        """
        
        Adds the subscription to the current users current invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_subscription_to_invoice(api_key, owner, dataset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_subscription_to_invoice_with_http_info(api_key, owner, dataset, **kwargs)
        else:
            (data) = self.add_subscription_to_invoice_with_http_info(api_key, owner, dataset, **kwargs)
            return data

    def add_subscription_to_invoice_with_http_info(self, api_key, owner, dataset, **kwargs):
        """
        
        Adds the subscription to the current users current invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_subscription_to_invoice_with_http_info(api_key, owner, dataset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param str owner: The owner of the data element (required)
        :param str dataset: The name of the data set (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'owner', 'dataset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_subscription_to_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `add_subscription_to_invoice`")
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `add_subscription_to_invoice`")
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params) or (params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `add_subscription_to_invoice`")

        resource_path = '/invoice/addSubscription/{owner}/{dataset}'.replace('{format}', 'json')
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
                                            response_type='Invoice',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_cart(self, api_key, **kwargs):
        """
        
        retrieve the current open oneoff invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_cart_with_http_info(api_key, **kwargs)
        else:
            (data) = self.get_cart_with_http_info(api_key, **kwargs)
            return data

    def get_cart_with_http_info(self, api_key, **kwargs):
        """
        
        retrieve the current open oneoff invoice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cart_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_cart`")

        resource_path = '/invoice/retrieveCurrent'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='Invoice',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_invoices(self, api_key, **kwargs):
        """
        
        retrieve a page of invoices

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invoices(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param int page: The page to show
        :return: list[Invoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_invoices_with_http_info(api_key, **kwargs)
        else:
            (data) = self.get_invoices_with_http_info(api_key, **kwargs)
            return data

    def get_invoices_with_http_info(self, api_key, **kwargs):
        """
        
        retrieve a page of invoices

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invoices_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :param int page: The page to show
        :return: list[Invoice]
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
                    " to method get_invoices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_invoices`")

        resource_path = '/invoice/retrieve'.replace('{format}', 'json')
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
                                            response_type='list[Invoice]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def process_cart(self, api_key, **kwargs):
        """
        
        Process a successful payment

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.process_cart(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.process_cart_with_http_info(api_key, **kwargs)
        else:
            (data) = self.process_cart_with_http_info(api_key, **kwargs)
            return data

    def process_cart_with_http_info(self, api_key, **kwargs):
        """
        
        Process a successful payment

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.process_cart_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key: The user api key (required)
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_cart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `process_cart`")

        resource_path = '/invoice/processCurrent'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='Invoice',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
