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


class ServiceUserList(object):
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
        'email': 'str',
        'name': 'str',
        'creation_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'name': 'name',
        'creation_date': 'creation_date'
    }

    def __init__(self, id=None, email=None, name=None, creation_date=None, local_vars_configuration=None):  # noqa: E501
        """ServiceUserList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._name = None
        self._creation_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.email = email
        self.name = name
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this ServiceUserList.  # noqa: E501


        :return: The id of this ServiceUserList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceUserList.


        :param id: The id of this ServiceUserList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this ServiceUserList.  # noqa: E501


        :return: The email of this ServiceUserList.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ServiceUserList.


        :param email: The email of this ServiceUserList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this ServiceUserList.  # noqa: E501


        :return: The name of this ServiceUserList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceUserList.


        :param name: The name of this ServiceUserList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 30):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def creation_date(self):
        """Gets the creation_date of this ServiceUserList.  # noqa: E501


        :return: The creation_date of this ServiceUserList.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ServiceUserList.


        :param creation_date: The creation_date of this ServiceUserList.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

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
        if not isinstance(other, ServiceUserList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceUserList):
            return True

        return self.to_dict() != other.to_dict()
