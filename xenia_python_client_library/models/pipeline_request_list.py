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


class PipelineRequestList(object):
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
        'project': 'str',
        'pipeline': 'str',
        'pipeline_request_id': 'str',
        'model_requests': 'list[PipelineRequestModelRequest]'
    }

    attribute_map = {
        'project': 'project',
        'pipeline': 'pipeline',
        'pipeline_request_id': 'pipeline_request_id',
        'model_requests': 'model_requests'
    }

    def __init__(self, project=None, pipeline=None, pipeline_request_id=None, model_requests=None, local_vars_configuration=None):  # noqa: E501
        """PipelineRequestList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project = None
        self._pipeline = None
        self._pipeline_request_id = None
        self._model_requests = None
        self.discriminator = None

        self.project = project
        self.pipeline = pipeline
        self.pipeline_request_id = pipeline_request_id
        self.model_requests = model_requests

    @property
    def project(self):
        """Gets the project of this PipelineRequestList.  # noqa: E501


        :return: The project of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this PipelineRequestList.


        :param project: The project of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project is not None and len(project) < 1):
            raise ValueError("Invalid value for `project`, length must be greater than or equal to `1`")  # noqa: E501

        self._project = project

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelineRequestList.  # noqa: E501


        :return: The pipeline of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelineRequestList.


        :param pipeline: The pipeline of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipeline is None:  # noqa: E501
            raise ValueError("Invalid value for `pipeline`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pipeline is not None and len(pipeline) < 1):
            raise ValueError("Invalid value for `pipeline`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline = pipeline

    @property
    def pipeline_request_id(self):
        """Gets the pipeline_request_id of this PipelineRequestList.  # noqa: E501


        :return: The pipeline_request_id of this PipelineRequestList.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_request_id

    @pipeline_request_id.setter
    def pipeline_request_id(self, pipeline_request_id):
        """Sets the pipeline_request_id of this PipelineRequestList.


        :param pipeline_request_id: The pipeline_request_id of this PipelineRequestList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipeline_request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pipeline_request_id`, must not be `None`")  # noqa: E501

        self._pipeline_request_id = pipeline_request_id

    @property
    def model_requests(self):
        """Gets the model_requests of this PipelineRequestList.  # noqa: E501


        :return: The model_requests of this PipelineRequestList.  # noqa: E501
        :rtype: list[PipelineRequestModelRequest]
        """
        return self._model_requests

    @model_requests.setter
    def model_requests(self, model_requests):
        """Sets the model_requests of this PipelineRequestList.


        :param model_requests: The model_requests of this PipelineRequestList.  # noqa: E501
        :type: list[PipelineRequestModelRequest]
        """
        if self.local_vars_configuration.client_side_validation and model_requests is None:  # noqa: E501
            raise ValueError("Invalid value for `model_requests`, must not be `None`")  # noqa: E501

        self._model_requests = model_requests

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
        if not isinstance(other, PipelineRequestList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineRequestList):
            return True

        return self.to_dict() != other.to_dict()