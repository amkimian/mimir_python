# coding: utf-8

"""
    Mimir DataHub API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.9
    
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

from pprint import pformat
from six import iteritems
import re


class UserTokens(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, access_token=None, token_secret=None):
        """
        UserTokens - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'access_token': 'str',
            'token_secret': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'access_token': 'accessToken',
            'token_secret': 'tokenSecret'
        }

        self._kind = kind
        self._access_token = access_token
        self._token_secret = token_secret

    @property
    def kind(self):
        """
        Gets the kind of this UserTokens.


        :return: The kind of this UserTokens.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UserTokens.


        :param kind: The kind of this UserTokens.
        :type: str
        """

        self._kind = kind

    @property
    def access_token(self):
        """
        Gets the access_token of this UserTokens.


        :return: The access_token of this UserTokens.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this UserTokens.


        :param access_token: The access_token of this UserTokens.
        :type: str
        """

        self._access_token = access_token

    @property
    def token_secret(self):
        """
        Gets the token_secret of this UserTokens.


        :return: The token_secret of this UserTokens.
        :rtype: str
        """
        return self._token_secret

    @token_secret.setter
    def token_secret(self, token_secret):
        """
        Sets the token_secret of this UserTokens.


        :param token_secret: The token_secret of this UserTokens.
        :type: str
        """

        self._token_secret = token_secret

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other