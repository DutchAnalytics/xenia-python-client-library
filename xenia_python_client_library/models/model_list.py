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


class ModelList(object):
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
        'name': 'str',
        'project': 'str',
        'description': 'str',
        'input_type': 'str',
        'output_type': 'str',
        'input_fields': 'list[ModelInputFieldList]',
        'output_fields': 'list[ModelOutputFieldList]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project': 'project',
        'description': 'description',
        'input_type': 'input_type',
        'output_type': 'output_type',
        'input_fields': 'input_fields',
        'output_fields': 'output_fields'
    }

    def __init__(self, id=None, name=None, project=None, description=None, input_type=None, output_type=None, input_fields=None, output_fields=None, local_vars_configuration=None):  # noqa: E501
        """ModelList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._project = None
        self._description = None
        self._input_type = None
        self._output_type = None
        self._input_fields = None
        self._output_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.project = project
        if description is not None:
            self.description = description
        self.input_type = input_type
        self.output_type = output_type
        if input_fields is not None:
            self.input_fields = input_fields
        if output_fields is not None:
            self.output_fields = output_fields

    @property
    def id(self):
        """Gets the id of this ModelList.  # noqa: E501


        :return: The id of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelList.


        :param id: The id of this ModelList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelList.  # noqa: E501


        :return: The name of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelList.


        :param name: The name of this ModelList.  # noqa: E501
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
    def project(self):
        """Gets the project of this ModelList.  # noqa: E501


        :return: The project of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ModelList.


        :param project: The project of this ModelList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project is not None and len(project) < 1):
            raise ValueError("Invalid value for `project`, length must be greater than or equal to `1`")  # noqa: E501

        self._project = project

    @property
    def description(self):
        """Gets the description of this ModelList.  # noqa: E501


        :return: The description of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelList.


        :param description: The description of this ModelList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 200):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def input_type(self):
        """Gets the input_type of this ModelList.  # noqa: E501


        :return: The input_type of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this ModelList.


        :param input_type: The input_type of this ModelList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and input_type is None:  # noqa: E501
            raise ValueError("Invalid value for `input_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                input_type is not None and len(input_type) < 1):
            raise ValueError("Invalid value for `input_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._input_type = input_type

    @property
    def output_type(self):
        """Gets the output_type of this ModelList.  # noqa: E501


        :return: The output_type of this ModelList.  # noqa: E501
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """Sets the output_type of this ModelList.


        :param output_type: The output_type of this ModelList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and output_type is None:  # noqa: E501
            raise ValueError("Invalid value for `output_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                output_type is not None and len(output_type) < 1):
            raise ValueError("Invalid value for `output_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._output_type = output_type

    @property
    def input_fields(self):
        """Gets the input_fields of this ModelList.  # noqa: E501


        :return: The input_fields of this ModelList.  # noqa: E501
        :rtype: list[ModelInputFieldList]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this ModelList.


        :param input_fields: The input_fields of this ModelList.  # noqa: E501
        :type: list[ModelInputFieldList]
        """

        self._input_fields = input_fields

    @property
    def output_fields(self):
        """Gets the output_fields of this ModelList.  # noqa: E501


        :return: The output_fields of this ModelList.  # noqa: E501
        :rtype: list[ModelOutputFieldList]
        """
        return self._output_fields

    @output_fields.setter
    def output_fields(self, output_fields):
        """Sets the output_fields of this ModelList.


        :param output_fields: The output_fields of this ModelList.  # noqa: E501
        :type: list[ModelOutputFieldList]
        """

        self._output_fields = output_fields

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
        if not isinstance(other, ModelList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelList):
            return True

        return self.to_dict() != other.to_dict()
