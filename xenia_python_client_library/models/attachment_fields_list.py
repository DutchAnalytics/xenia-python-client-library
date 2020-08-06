# coding: utf-8

"""
    Xenia Python Client Library

    Python Client Library to interact with the Xenia API.  # noqa: E501

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from xenia_python_client_library.configuration import Configuration


class AttachmentFieldsList(object):
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
        'source_field_name': 'str',
        'destination_field_name': 'str'
    }

    attribute_map = {
        'source_field_name': 'source_field_name',
        'destination_field_name': 'destination_field_name'
    }

    def __init__(self, source_field_name=None, destination_field_name=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentFieldsList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_field_name = None
        self._destination_field_name = None
        self.discriminator = None

        if source_field_name is not None:
            self.source_field_name = source_field_name
        if destination_field_name is not None:
            self.destination_field_name = destination_field_name

    @property
    def source_field_name(self):
        """Gets the source_field_name of this AttachmentFieldsList.  # noqa: E501


        :return: The source_field_name of this AttachmentFieldsList.  # noqa: E501
        :rtype: str
        """
        return self._source_field_name

    @source_field_name.setter
    def source_field_name(self, source_field_name):
        """Sets the source_field_name of this AttachmentFieldsList.


        :param source_field_name: The source_field_name of this AttachmentFieldsList.  # noqa: E501
        :type: str
        """

        self._source_field_name = source_field_name

    @property
    def destination_field_name(self):
        """Gets the destination_field_name of this AttachmentFieldsList.  # noqa: E501


        :return: The destination_field_name of this AttachmentFieldsList.  # noqa: E501
        :rtype: str
        """
        return self._destination_field_name

    @destination_field_name.setter
    def destination_field_name(self, destination_field_name):
        """Sets the destination_field_name of this AttachmentFieldsList.


        :param destination_field_name: The destination_field_name of this AttachmentFieldsList.  # noqa: E501
        :type: str
        """

        self._destination_field_name = destination_field_name

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
        if not isinstance(other, AttachmentFieldsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentFieldsList):
            return True

        return self.to_dict() != other.to_dict()
