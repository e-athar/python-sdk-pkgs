# coding: utf-8


"""
    Storage APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 16.1.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
import pprint
import re  # noqa: F401

import six


class TargetParam(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'num_virtual_targets': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'num_virtual_targets': 'numVirtualTargets',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }


    def __init__(self, num_virtual_targets=None, *args, **kwargs):  # noqa: E501
        """TargetParam - a model defined in Swagger"""  # noqa: E501
        self._num_virtual_targets = None
        self.discriminator = None
        if num_virtual_targets is not None:
            self._num_virtual_targets = num_virtual_targets
        self.__reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        self.__unknown_fields = {}
        self.__object_type = self._initialize_object_type()

    def _initialize_object_type(self):
        return 'storage.v4.config.TargetParam'

    def _initialize_fq_object_type(self):
        return 'storage.v4.r0.a1.config.TargetParam'

    def get_object_type(self):
        return self.__object_type

    def get_reserved(self):
        return self.__reserved

    def get_unknown_fields(self):
        return self.__unknown_fields

    @property
    def num_virtual_targets(self):
        """Gets the num_virtual_targets of this TargetParam.  # noqa: E501

        Number of virtual targets to generate for the iSCSI target.  # noqa: E501

        :return: The num_virtual_targets of this TargetParam.  # noqa: E501
        :rtype: int
        """
        return self._num_virtual_targets

    @num_virtual_targets.setter
    def num_virtual_targets(self, num_virtual_targets):
        """Sets the num_virtual_targets of this TargetParam.

        Number of virtual targets to generate for the iSCSI target.  # noqa: E501

        :param num_virtual_targets: The num_virtual_targets of this TargetParam.  # noqa: E501
        :type: int
        """
        if num_virtual_targets is not None and num_virtual_targets > 32:  # noqa: E501
            raise ValueError("Invalid value for `num_virtual_targets`, must be a value less than or equal to `32`")  # noqa: E501
        if num_virtual_targets is not None and num_virtual_targets < 1:  # noqa: E501
            raise ValueError("Invalid value for `num_virtual_targets`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_virtual_targets = num_virtual_targets

    @property
    def _reserved(self):
        """Gets the _reserved of this TargetParam.  # noqa: E501


        :return: The _reserved of this TargetParam.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self.__reserved

    @property
    def _object_type(self):
        """Gets the _object_type of this TargetParam.  # noqa: E501


        :return: The _object_type of this TargetParam.  # noqa: E501
        :rtype: str
        """
        return self.__object_type

    @property
    def _unknown_fields(self):
        """Gets the _unknown_fields of this TargetParam.  # noqa: E501


        :return: The _unknown_fields of this TargetParam.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self.__unknown_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TargetParam, dict):
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
        if not isinstance(other, TargetParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
