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


class PipelineInsertList(object):
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
        'success': 'str',
        'trace_id': 'str'
    }

    attribute_map = {
        'success': 'success',
        'trace_id': 'trace_id'
    }

    def __init__(self, success=None, trace_id=None, local_vars_configuration=None):  # noqa: E501
        """PipelineInsertList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._trace_id = None
        self.discriminator = None

        self.success = success
        self.trace_id = trace_id

    @property
    def success(self):
        """Gets the success of this PipelineInsertList.  # noqa: E501


        :return: The success of this PipelineInsertList.  # noqa: E501
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PipelineInsertList.


        :param success: The success of this PipelineInsertList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                success is not None and len(success) < 1):
            raise ValueError("Invalid value for `success`, length must be greater than or equal to `1`")  # noqa: E501

        self._success = success

    @property
    def trace_id(self):
        """Gets the trace_id of this PipelineInsertList.  # noqa: E501


        :return: The trace_id of this PipelineInsertList.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this PipelineInsertList.


        :param trace_id: The trace_id of this PipelineInsertList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and trace_id is None:  # noqa: E501
            raise ValueError("Invalid value for `trace_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trace_id is not None and len(trace_id) < 1):
            raise ValueError("Invalid value for `trace_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._trace_id = trace_id

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
        if not isinstance(other, PipelineInsertList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineInsertList):
            return True

        return self.to_dict() != other.to_dict()
