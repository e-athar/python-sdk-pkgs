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

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""

class EntityReference(object):
    """EntityReference - a model defined in Swagger"""
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
        'rel': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'ext_id': 'extId',
        'rel': 'rel',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, ext_id=None, rel=None, *args, **kwargs):  # noqa: E501
        """EntityReference - a model defined in Swagger
            \nDetails of entity.
        """
        self._ext_id = None
        self._rel = None
        self.discriminator = None
        if ext_id is not None:
            self._ext_id = ext_id
        if rel is not None:
            self._rel = rel
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'prism.v4.config.EntityReference'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.EntityReference'

    def _populate_hidden_vars(self, kwargs):
        if "_reserved" in kwargs and kwargs["_reserved"] is not None:
            self.__reserved = kwargs["_reserved"]
        elif "_reserved" in self.attribute_map and self.attribute_map["_reserved"] in kwargs and kwargs[self.attribute_map["_reserved"]] is not None:
            self.__reserved = kwargs[self.attribute_map["_reserved"]]
        else :
            self.__reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        if "_unknown_fields" in kwargs and kwargs["_unknown_fields"] is not None:
            self.__unknown_fields = kwargs["_unknown_fields"]
        elif "_unknown_fields" in self.attribute_map and self.attribute_map["_unknown_fields"] in kwargs and kwargs[self.attribute_map["_unknown_fields"]] is not None:
            self.__unknown_fields = kwargs[self.attribute_map["_unknown_fields"]]
        else :
            self.__unknown_fields = {}
        if "_object_type" in kwargs and kwargs["_object_type"] is not None:
            self.__object_type = kwargs["_object_type"]
        elif "_object_type" in self.attribute_map and self.attribute_map["_object_type"] in kwargs and kwargs[self.attribute_map["_object_type"]] is not None:
            self.__object_type = kwargs[self.attribute_map["_object_type"]]
        else:
            self.__object_type = self._initialize_object_type()

    def get_object_type(self):
        return self.__object_type

    def get_reserved(self):
        return self.__reserved

    def get_unknown_fields(self):
        return self.__unknown_fields

    @property
    def ext_id(self):
        """`{ str }`
            \nGlobally unique identifier of the entity.
        """ # noqa: E501
        return self._ext_id

    @ext_id.setter
    def ext_id(self, ext_id):

        self._ext_id = ext_id

    @property
    def rel(self):
        """`{ str }`
            \nEntity type identified as 'namespace:module[:submodule]:entityType such vmm:ahv:vm'
        """ # noqa: E501
        return self._rel

    @rel.setter
    def rel(self, rel):

        self._rel = rel

    @property
    def _reserved(self):
        """`{ dict(str, object) }`
            
        """ # noqa: E501
        return self.__reserved

    @property
    def _object_type(self):
        """`{ str }`
            
        """ # noqa: E501
        return self.__object_type

    @property
    def _unknown_fields(self):
        """`{ dict(str, object) }`
            
        """ # noqa: E501
        return self.__unknown_fields

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
        if issubclass(EntityReference, dict):
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
        if not isinstance(other, EntityReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

