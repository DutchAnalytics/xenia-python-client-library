# coding: utf-8

"""
    Xenia Python Client Library

    Python Client Library to interact with the Xenia API.  # noqa: E501

    The version of the OpenAPI document: v1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from xenia_python_client_library.configuration import Configuration


class ConnectorCreate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'type': 'str',
        'credentials': 'str',
        'configuration': 'dict(str, str)',
        'input_fields': 'list[ConnectorFieldCreate]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'credentials': 'credentials',
        'configuration': 'configuration',
        'input_fields': 'input_fields'
    }

    def __init__(self, name=None, type=None, credentials=None, configuration=None, input_fields=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._credentials = None
        self._configuration = None
        self._input_fields = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.credentials = credentials
        self.configuration = configuration
        if input_fields is not None:
            self.input_fields = input_fields

    @property
    def name(self):
        """Gets the name of this ConnectorCreate.  # noqa: E501


        :return: The name of this ConnectorCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorCreate.


        :param name: The name of this ConnectorCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this ConnectorCreate.  # noqa: E501


        :return: The type of this ConnectorCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectorCreate.


        :param type: The type of this ConnectorCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 64):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def credentials(self):
        """Gets the credentials of this ConnectorCreate.  # noqa: E501


        :return: The credentials of this ConnectorCreate.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ConnectorCreate.


        :param credentials: The credentials of this ConnectorCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and credentials is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                credentials is not None and len(credentials) < 1):
            raise ValueError("Invalid value for `credentials`, length must be greater than or equal to `1`")  # noqa: E501

        self._credentials = credentials

    @property
    def configuration(self):
        """Gets the configuration of this ConnectorCreate.  # noqa: E501


        :return: The configuration of this ConnectorCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ConnectorCreate.


        :param configuration: The configuration of this ConnectorCreate.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and configuration is None:  # noqa: E501
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def input_fields(self):
        """Gets the input_fields of this ConnectorCreate.  # noqa: E501


        :return: The input_fields of this ConnectorCreate.  # noqa: E501
        :rtype: list[ConnectorFieldCreate]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this ConnectorCreate.


        :param input_fields: The input_fields of this ConnectorCreate.  # noqa: E501
        :type: list[ConnectorFieldCreate]
        """

        self._input_fields = input_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectorCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorCreate):
            return True

        return self.to_dict() != other.to_dict()
