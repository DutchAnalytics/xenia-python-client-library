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


class OrganizationUserInviteList(object):
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
        'admin': 'bool',
        'invitation_creation_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'admin': 'admin',
        'invitation_creation_time': 'invitation_creation_time'
    }

    def __init__(self, id=None, email=None, admin=None, invitation_creation_time=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationUserInviteList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._admin = None
        self._invitation_creation_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.email = email
        if admin is not None:
            self.admin = admin
        self.invitation_creation_time = invitation_creation_time

    @property
    def id(self):
        """Gets the id of this OrganizationUserInviteList.  # noqa: E501


        :return: The id of this OrganizationUserInviteList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationUserInviteList.


        :param id: The id of this OrganizationUserInviteList.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this OrganizationUserInviteList.  # noqa: E501


        :return: The email of this OrganizationUserInviteList.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrganizationUserInviteList.


        :param email: The email of this OrganizationUserInviteList.  # noqa: E501
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
    def admin(self):
        """Gets the admin of this OrganizationUserInviteList.  # noqa: E501


        :return: The admin of this OrganizationUserInviteList.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this OrganizationUserInviteList.


        :param admin: The admin of this OrganizationUserInviteList.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def invitation_creation_time(self):
        """Gets the invitation_creation_time of this OrganizationUserInviteList.  # noqa: E501


        :return: The invitation_creation_time of this OrganizationUserInviteList.  # noqa: E501
        :rtype: datetime
        """
        return self._invitation_creation_time

    @invitation_creation_time.setter
    def invitation_creation_time(self, invitation_creation_time):
        """Sets the invitation_creation_time of this OrganizationUserInviteList.


        :param invitation_creation_time: The invitation_creation_time of this OrganizationUserInviteList.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and invitation_creation_time is None:  # noqa: E501
            raise ValueError("Invalid value for `invitation_creation_time`, must not be `None`")  # noqa: E501

        self._invitation_creation_time = invitation_creation_time

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
        if not isinstance(other, OrganizationUserInviteList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationUserInviteList):
            return True

        return self.to_dict() != other.to_dict()
