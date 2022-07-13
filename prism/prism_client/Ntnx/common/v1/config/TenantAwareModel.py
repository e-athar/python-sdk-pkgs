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

class TenantAwareModel(object):
    """TenantAwareModel - a model defined in Swagger"""
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
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, tenant_id=None, *args, **kwargs):  # noqa: E501
        """TenantAwareModel - a model defined in Swagger
            \nA model base class whose instances are bound to a specific tenant.  This model adds a tenantId to the base model class that it extends and is automatically set by the server. 
        """
        self._tenant_id = None
        self.discriminator = None
        if tenant_id is not None:
            self._tenant_id = tenant_id
        # populate hidden vars if not empty
        self._populate_hidden_vars(kwargs)

    def _initialize_object_type(self):
        return 'common.v1.config.TenantAwareModel'

    def _initialize_fq_object_type(self):
        return 'common.v1.r0.a3.config.TenantAwareModel'

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
    def tenant_id(self):
        """`{ str }`
            \nA globally unique identifier that represents the tenant that owns this entity.  It is automatically assigned by the system and is immutable from an API consumer perspective (some use cases may cause this Id to change - for instance a use case may require the transfer of ownership of the entity, but these cases are handled automatically on the server). 
        """ # noqa: E501
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        if tenant_id is not None and not re.search(r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', tenant_id):  # noqa: E501
            raise ValueError(r"Invalid value for `tenant_id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self._tenant_id = tenant_id

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
        if issubclass(TenantAwareModel, dict):
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
        if not isinstance(other, TenantAwareModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

