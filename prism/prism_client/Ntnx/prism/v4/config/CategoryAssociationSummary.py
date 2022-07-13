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
from prism_client.Ntnx.prism.v4.config.ResourceGroup import ResourceGroup  # noqa: F401,E501
from prism_client.Ntnx.prism.v4.config.ResourceType import ResourceType  # noqa: F401,E501

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""

class CategoryAssociationSummary(object):
    """CategoryAssociationSummary - a model defined in Swagger"""
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
        'category_id': 'str',
        'resource_type': 'prism.v4.config.ResourceType',
        'resource_group': 'prism.v4.config.ResourceGroup',
        'count': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'category_id': 'categoryId',
        'resource_type': 'resourceType',
        'resource_group': 'resourceGroup',
        'count': 'count',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, category_id=None, resource_type=None, resource_group=None, count=None, *args, **kwargs):  # noqa: E501
        """CategoryAssociationSummary - a model defined in Swagger
            \nThis attribute contains the list of entities which have been assigned the given category.<br> These entities are grouped by entity types (like VM or HOST).<br> Each associations object contains the total entities belonging to the given entity type, and category extId. 
        """
        self._category_id = None
        self._resource_type = None
        self._resource_group = None
        self._count = None
        self.discriminator = None
        if category_id is not None:
            self._category_id = category_id
        if resource_type is not None:
            self._resource_type = resource_type
        if resource_group is not None:
            self._resource_group = resource_group
        if count is not None:
            self._count = count
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'prism.v4.config.CategoryAssociationSummary'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.CategoryAssociationSummary'

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
    def category_id(self):
        """`{ str }`
            \nExternal identifier for the given category. 
        """ # noqa: E501
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):

        self._category_id = category_id

    @property
    def resource_type(self):
        """`{ prism.v4.config.ResourceType }`
            
        """ # noqa: E501
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):

        self._resource_type = resource_type

    @property
    def resource_group(self):
        """`{ prism.v4.config.ResourceGroup }`
            
        """ # noqa: E501
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):

        self._resource_group = resource_group

    @property
    def count(self):
        """`{ int }`
            \nThere are three category types: - SYSTEM: Defined by an administrator. Cannot be modified by the user. - INTERNAL: Defined by any internal process within Nutanix ecosystem. Cannot be viewed directly through a list call.             Can be modified by the user. - USER: Defined by a user through the v4 api Currently v4 apis allow the creation of only User Category Type. 
        """ # noqa: E501
        return self._count

    @count.setter
    def count(self, count):

        self._count = count

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
        if issubclass(CategoryAssociationSummary, dict):
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
        if not isinstance(other, CategoryAssociationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
