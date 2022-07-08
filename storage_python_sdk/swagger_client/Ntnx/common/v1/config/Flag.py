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


class Flag(object):
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
        'name': 'str',
        'value': 'bool',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }


    def __init__(self, name=None, value=False, *args, **kwargs):  # noqa: E501
        """Flag - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self._name = name
        if value is not None:
            self._value = value
        self.__reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        self.__unknown_fields = {}
        self.__object_type = self._initialize_object_type()

    def _initialize_object_type(self):
        return 'common.v1.config.Flag'

    def _initialize_fq_object_type(self):
        return 'common.v1.r0.a3.config.Flag'

    def get_object_type(self):
        return self.__object_type

    def get_reserved(self):
        return self.__reserved

    def get_unknown_fields(self):
        return self.__unknown_fields

    @property
    def name(self):
        """Gets the name of this Flag.  # noqa: E501


        :return: The name of this Flag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flag.


        :param name: The name of this Flag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this Flag.  # noqa: E501


        :return: The value of this Flag.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Flag.


        :param value: The value of this Flag.  # noqa: E501
        :type: bool
        """

        self._value = value

    @property
    def _reserved(self):
        """Gets the _reserved of this Flag.  # noqa: E501


        :return: The _reserved of this Flag.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self.__reserved

    @property
    def _object_type(self):
        """Gets the _object_type of this Flag.  # noqa: E501


        :return: The _object_type of this Flag.  # noqa: E501
        :rtype: str
        """
        return self.__object_type

    @property
    def _unknown_fields(self):
        """Gets the _unknown_fields of this Flag.  # noqa: E501


        :return: The _unknown_fields of this Flag.  # noqa: E501
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
        if issubclass(Flag, dict):
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
        if not isinstance(other, Flag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

