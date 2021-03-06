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

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""


class KVPairvalue(object):
    """KVPairvalue - a model defined in Swagger"""
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
    }

    attribute_map = {
    }

    discriminator_value_class_map = {
        'EMPTY_LIST': 'list[str]',
        'String': 'str',
        'Integer': 'int'
    }

    ONE_OF_ITEM_DISCRIMINATOR_NAME = '$valueItemDiscriminator'


    def __init__(self, *args, **kwargs):  # noqa: E501
        """KVPairvalue - a model defined in Swagger
            
        """
        self.discriminator = None
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'OneOfcommon.v1.config.KVPairvalue'

    def _initialize_fq_object_type(self):
        return ''

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

    def get_real_child_model(self, discriminator):
        """Returns the real base class specified by the discriminator"""
        if discriminator is not None and discriminator in self.discriminator_value_class_map:
            return self.discriminator_value_class_map.get(discriminator)
        return None

    @staticmethod
    def get_discriminator_from_object(value):
        """Returns the model properties as a dict"""
        if not value:
            disc = 'list[str]'
        elif hasattr(value, "_object_type"):
            disc = value.get_object_type()
        elif type(value) == list:
            if hasattr(value[0], "_object_type"):
                datatype = value[0].get_object_type()
            else:
                datatype = type(value[0]).__name__
            disc = 'list[' + datatype + ']'
        else:
            disc = type(value).__name__
        if disc in KVPairvalue.discriminator_value_class_map.values():
            return list(KVPairvalue.discriminator_value_class_map.keys())[list(KVPairvalue.discriminator_value_class_map.values()).index(disc)]
        return None


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
        if issubclass(KVPairvalue, dict):
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
        if not isinstance(other, KVPairvalue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

