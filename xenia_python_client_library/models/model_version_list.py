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


class ModelVersionList(object):
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
        'id': 'str',
        'model': 'str',
        'version': 'str',
        'language': 'str',
        'status': 'str',
        'error_message': 'str',
        'memory_allocation': 'int',
        'maximum_deployments': 'int',
        'minimum_deployments': 'int',
        'unused_shutdown_time': 'int',
        'file_last_updated_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'version': 'version',
        'language': 'language',
        'status': 'status',
        'error_message': 'error_message',
        'memory_allocation': 'memory_allocation',
        'maximum_deployments': 'maximum_deployments',
        'minimum_deployments': 'minimum_deployments',
        'unused_shutdown_time': 'unused_shutdown_time',
        'file_last_updated_date': 'file_last_updated_date'
    }

    def __init__(self, id=None, model=None, version=None, language=None, status=None, error_message=None, memory_allocation=None, maximum_deployments=None, minimum_deployments=None, unused_shutdown_time=None, file_last_updated_date=None, local_vars_configuration=None):  # noqa: E501
        """ModelVersionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._model = None
        self._version = None
        self._language = None
        self._status = None
        self._error_message = None
        self._memory_allocation = None
        self._maximum_deployments = None
        self._minimum_deployments = None
        self._unused_shutdown_time = None
        self._file_last_updated_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.model = model
        self.version = version
        self.language = language
        self.status = status
        self.error_message = error_message
        if memory_allocation is not None:
            self.memory_allocation = memory_allocation
        if maximum_deployments is not None:
            self.maximum_deployments = maximum_deployments
        if minimum_deployments is not None:
            self.minimum_deployments = minimum_deployments
        if unused_shutdown_time is not None:
            self.unused_shutdown_time = unused_shutdown_time
        if file_last_updated_date is not None:
            self.file_last_updated_date = file_last_updated_date

    @property
    def id(self):
        """Gets the id of this ModelVersionList.  # noqa: E501


        :return: The id of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelVersionList.


        :param id: The id of this ModelVersionList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this ModelVersionList.  # noqa: E501


        :return: The model of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelVersionList.


        :param model: The model of this ModelVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) < 1):
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def version(self):
        """Gets the version of this ModelVersionList.  # noqa: E501


        :return: The version of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelVersionList.


        :param version: The version of this ModelVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 64):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def language(self):
        """Gets the language of this ModelVersionList.  # noqa: E501


        :return: The language of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ModelVersionList.


        :param language: The language of this ModelVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 1):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def status(self):
        """Gets the status of this ModelVersionList.  # noqa: E501


        :return: The status of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelVersionList.


        :param status: The status of this ModelVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this ModelVersionList.  # noqa: E501


        :return: The error_message of this ModelVersionList.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ModelVersionList.


        :param error_message: The error_message of this ModelVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                error_message is not None and len(error_message) > 500):
            raise ValueError("Invalid value for `error_message`, length must be less than or equal to `500`")  # noqa: E501

        self._error_message = error_message

    @property
    def memory_allocation(self):
        """Gets the memory_allocation of this ModelVersionList.  # noqa: E501


        :return: The memory_allocation of this ModelVersionList.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocation

    @memory_allocation.setter
    def memory_allocation(self, memory_allocation):
        """Sets the memory_allocation of this ModelVersionList.


        :param memory_allocation: The memory_allocation of this ModelVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and memory_allocation > 1048576):  # noqa: E501
            raise ValueError("Invalid value for `memory_allocation`, must be a value less than or equal to `1048576`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and memory_allocation < 256):  # noqa: E501
            raise ValueError("Invalid value for `memory_allocation`, must be a value greater than or equal to `256`")  # noqa: E501

        self._memory_allocation = memory_allocation

    @property
    def maximum_deployments(self):
        """Gets the maximum_deployments of this ModelVersionList.  # noqa: E501


        :return: The maximum_deployments of this ModelVersionList.  # noqa: E501
        :rtype: int
        """
        return self._maximum_deployments

    @maximum_deployments.setter
    def maximum_deployments(self, maximum_deployments):
        """Sets the maximum_deployments of this ModelVersionList.


        :param maximum_deployments: The maximum_deployments of this ModelVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_deployments is not None and maximum_deployments > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `maximum_deployments`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                maximum_deployments is not None and maximum_deployments < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `maximum_deployments`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._maximum_deployments = maximum_deployments

    @property
    def minimum_deployments(self):
        """Gets the minimum_deployments of this ModelVersionList.  # noqa: E501


        :return: The minimum_deployments of this ModelVersionList.  # noqa: E501
        :rtype: int
        """
        return self._minimum_deployments

    @minimum_deployments.setter
    def minimum_deployments(self, minimum_deployments):
        """Sets the minimum_deployments of this ModelVersionList.


        :param minimum_deployments: The minimum_deployments of this ModelVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minimum_deployments is not None and minimum_deployments > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `minimum_deployments`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                minimum_deployments is not None and minimum_deployments < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `minimum_deployments`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._minimum_deployments = minimum_deployments

    @property
    def unused_shutdown_time(self):
        """Gets the unused_shutdown_time of this ModelVersionList.  # noqa: E501


        :return: The unused_shutdown_time of this ModelVersionList.  # noqa: E501
        :rtype: int
        """
        return self._unused_shutdown_time

    @unused_shutdown_time.setter
    def unused_shutdown_time(self, unused_shutdown_time):
        """Sets the unused_shutdown_time of this ModelVersionList.


        :param unused_shutdown_time: The unused_shutdown_time of this ModelVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                unused_shutdown_time is not None and unused_shutdown_time > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `unused_shutdown_time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unused_shutdown_time is not None and unused_shutdown_time < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `unused_shutdown_time`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._unused_shutdown_time = unused_shutdown_time

    @property
    def file_last_updated_date(self):
        """Gets the file_last_updated_date of this ModelVersionList.  # noqa: E501


        :return: The file_last_updated_date of this ModelVersionList.  # noqa: E501
        :rtype: datetime
        """
        return self._file_last_updated_date

    @file_last_updated_date.setter
    def file_last_updated_date(self, file_last_updated_date):
        """Sets the file_last_updated_date of this ModelVersionList.


        :param file_last_updated_date: The file_last_updated_date of this ModelVersionList.  # noqa: E501
        :type: datetime
        """

        self._file_last_updated_date = file_last_updated_date

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
        if not isinstance(other, ModelVersionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelVersionList):
            return True

        return self.to_dict() != other.to_dict()
