# coding: utf-8


"""
IGNORE:
    Tasks Versioned APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 16.7.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import pprint
import json
import ast
import re  # noqa: F401

import six
import tasks_client.Ntnx
from tasks_client.Ntnx.OneOfprism.v4.config.TaskCancelResponsedata import TaskCancelResponsedata  # noqa: F401,E501
from tasks_client.Ntnx.common.v1.response.ApiResponseMetadata import ApiResponseMetadata  # noqa: F401,E501

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""


class TaskCancelResponse(object):
    """TaskCancelResponse - a model defined in Swagger"""
    """
    IGNORE:
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    IGNORE
    """ # noqa: E501
    swagger_types = {
        'metadata': 'common.v1.response.ApiResponseMetadata',
        'data': 'OneOfprism.v4.config.TaskCancelResponsedata',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'metadata': 'metadata',
        'data': 'data',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, metadata=None, data=None, *args, **kwargs):  # noqa: E501
        """TaskCancelResponse - a model defined in Swagger
            \nREST Response for all response codes in api path /prism/v4.0.a1/config/tasks/{taskExtId}/$actions/cancel Post operation
        """
        self.__metadata = None
        self.__data = None
        self.discriminator = None
        if metadata is not None:
            self.__metadata = metadata
        if data is not None:
            self.__data = data
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'prism.v4.config.TaskCancelResponse'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.TaskCancelResponse'

    def _populate_hidden_vars(self, kwargs):
        if "_reserved" in kwargs and kwargs["_reserved"] is not None:
            self.__dollar_reserved = kwargs["_reserved"]
        elif "_reserved" in self.attribute_map and self.attribute_map["_reserved"] in kwargs and kwargs[self.attribute_map["_reserved"]] is not None:
            self.__dollar_reserved = kwargs[self.attribute_map["_reserved"]]
        else :
            self.__dollar_reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        if "_unknown_fields" in kwargs and kwargs["_unknown_fields"] is not None:
            self.__dollar_unknown_fields = kwargs["_unknown_fields"]
        elif "_unknown_fields" in self.attribute_map and self.attribute_map["_unknown_fields"] in kwargs and kwargs[self.attribute_map["_unknown_fields"]] is not None:
            self.__dollar_unknown_fields = kwargs[self.attribute_map["_unknown_fields"]]
        else :
            self.__dollar_unknown_fields = {}
        if "_object_type" in kwargs and kwargs["_object_type"] is not None:
            self.__dollar_object_type = kwargs["_object_type"]
        elif "_object_type" in self.attribute_map and self.attribute_map["_object_type"] in kwargs and kwargs[self.attribute_map["_object_type"]] is not None:
            self.__dollar_object_type = kwargs[self.attribute_map["_object_type"]]
        else:
            self.__dollar_object_type = self._initialize_object_type()

    def get_object_type(self):
        return self.__dollar_object_type

    def get_reserved(self):
        return self.__dollar_reserved

    def get_unknown_fields(self):
        return self.__dollar_unknown_fields

    @property
    def metadata(self):
        """`{ common.v1.response.ApiResponseMetadata }`
            
        """ # noqa: E501
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata):

        self.__metadata = metadata

    @property
    def data(self):
        """`{ prism.v4.error.ErrorResponse }`
            
        """ # noqa: E501
        return self.__data

    @data.setter
    def data(self, data):

        self.__data = data

    @property
    def _reserved(self):
        """`{ dict(str, object) }`
            
        """ # noqa: E501
        return self.__dollar_reserved

    @property
    def _object_type(self):
        """`{ str }`
            
        """ # noqa: E501
        return self.__dollar_object_type

    @property
    def _unknown_fields(self):
        """`{ dict(str, object) }`
            
        """ # noqa: E501
        return self.__dollar_unknown_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, attr_type in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if attr_type.startswith('OneOf'):
                type = getattr(tasks_client.Ntnx, attr_type.split('.')[-1])
                if hasattr(type, 'get_discriminator_from_object'):
                    result[type.ONE_OF_ITEM_DISCRIMINATOR_NAME] = type.get_discriminator_from_object(value)
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
        if issubclass(TaskCancelResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskCancelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

