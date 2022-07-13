# coding: utf-8


"""
IGNORE:
    Nutanix Prism Versioned APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
import pprint
import json
import ast
import re  # noqa: F401

import six
from prism_client.Ntnx.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""

class TaskReferenceInternal(ApiLink):
    """TaskReferenceInternal - a model defined in Swagger"""
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
        'ext_id': 'str',
        'href': 'str',
        'rel': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'ext_id': 'extId',
        'href': 'href',
        'rel': 'rel',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, ext_id=None, href=None, rel=None, *args, **kwargs):  # noqa: E501
        """TaskReferenceInternal - a model defined in Swagger
            \nReference to task associated with current task.
        """
        ApiLink.__init__(self, href, rel, *args, **kwargs)
        self._ext_id = None
        self.discriminator = None
        if ext_id is not None:
            self._ext_id = ext_id

    def _initialize_object_type(self):
        return 'prism.v4.config.TaskReferenceInternal'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.TaskReferenceInternal'


    @property
    def ext_id(self):
        """`{ str }`
            \nGlocally unique identifier of the task.
        """ # noqa: E501
        return self._ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        if ext_id is not None and not re.search(r'^[a-zA-Z0-9\/+]*={0,2}:[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', ext_id):  # noqa: E501
            raise ValueError(r"Invalid value for `ext_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\/+]*={0,2}:[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/`")  # noqa: E501

        self._ext_id = ext_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, attr_type in six.iteritems(self.swagger_types):
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
        if issubclass(TaskReferenceInternal, dict):
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
        if not isinstance(other, TaskReferenceInternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

