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


class ModelRequestResultList(object):
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
        'time_created': 'datetime',
        'time_last_updated': 'datetime',
        'status': 'str',
        'request_id': 'str',
        'result': 'object',
        'error_message': 'str',
        'prediction_duration': 'float'
    }

    attribute_map = {
        'time_created': 'time_created',
        'time_last_updated': 'time_last_updated',
        'status': 'status',
        'request_id': 'request_id',
        'result': 'result',
        'error_message': 'error_message',
        'prediction_duration': 'prediction_duration'
    }

    def __init__(self, time_created=None, time_last_updated=None, status=None, request_id=None, result=None, error_message=None, prediction_duration=None, local_vars_configuration=None):  # noqa: E501
        """ModelRequestResultList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time_created = None
        self._time_last_updated = None
        self._status = None
        self._request_id = None
        self._result = None
        self._error_message = None
        self._prediction_duration = None
        self.discriminator = None

        self.time_created = time_created
        self.time_last_updated = time_last_updated
        self.status = status
        self.request_id = request_id
        self.result = result
        self.error_message = error_message
        self.prediction_duration = prediction_duration

    @property
    def time_created(self):
        """Gets the time_created of this ModelRequestResultList.  # noqa: E501


        :return: The time_created of this ModelRequestResultList.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this ModelRequestResultList.


        :param time_created: The time_created of this ModelRequestResultList.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and time_created is None:  # noqa: E501
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created

    @property
    def time_last_updated(self):
        """Gets the time_last_updated of this ModelRequestResultList.  # noqa: E501


        :return: The time_last_updated of this ModelRequestResultList.  # noqa: E501
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """Sets the time_last_updated of this ModelRequestResultList.


        :param time_last_updated: The time_last_updated of this ModelRequestResultList.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and time_last_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `time_last_updated`, must not be `None`")  # noqa: E501

        self._time_last_updated = time_last_updated

    @property
    def status(self):
        """Gets the status of this ModelRequestResultList.  # noqa: E501


        :return: The status of this ModelRequestResultList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelRequestResultList.


        :param status: The status of this ModelRequestResultList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["pending", "success", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def request_id(self):
        """Gets the request_id of this ModelRequestResultList.  # noqa: E501


        :return: The request_id of this ModelRequestResultList.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ModelRequestResultList.


        :param request_id: The request_id of this ModelRequestResultList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def result(self):
        """Gets the result of this ModelRequestResultList.  # noqa: E501


        :return: The result of this ModelRequestResultList.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ModelRequestResultList.


        :param result: The result of this ModelRequestResultList.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def error_message(self):
        """Gets the error_message of this ModelRequestResultList.  # noqa: E501


        :return: The error_message of this ModelRequestResultList.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ModelRequestResultList.


        :param error_message: The error_message of this ModelRequestResultList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                error_message is not None and len(error_message) < 1):
            raise ValueError("Invalid value for `error_message`, length must be greater than or equal to `1`")  # noqa: E501

        self._error_message = error_message

    @property
    def prediction_duration(self):
        """Gets the prediction_duration of this ModelRequestResultList.  # noqa: E501


        :return: The prediction_duration of this ModelRequestResultList.  # noqa: E501
        :rtype: float
        """
        return self._prediction_duration

    @prediction_duration.setter
    def prediction_duration(self, prediction_duration):
        """Sets the prediction_duration of this ModelRequestResultList.


        :param prediction_duration: The prediction_duration of this ModelRequestResultList.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and prediction_duration is None:  # noqa: E501
            raise ValueError("Invalid value for `prediction_duration`, must not be `None`")  # noqa: E501

        self._prediction_duration = prediction_duration

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
        if not isinstance(other, ModelRequestResultList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelRequestResultList):
            return True

        return self.to_dict() != other.to_dict()
