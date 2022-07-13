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
from prism_client.Ntnx.prism.v4.config.AssociationDetail import AssociationDetail  # noqa: F401,E501
from prism_client.Ntnx.prism.v4.config.Reference import Reference  # noqa: F401,E501

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""

class AssociationDetailProjection(AssociationDetail):
    """AssociationDetailProjection - a model defined in Swagger"""
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
        'resource_references': 'list[prism.v4.config.Reference]',
        'category_id': 'str',
        'resource_type': 'prism.v4.config.ResourceType',
        'resource_group': 'prism.v4.config.ResourceGroup',
        'count': 'int',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'resource_references': 'resourceReferences',
        'category_id': 'categoryId',
        'resource_type': 'resourceType',
        'resource_group': 'resourceGroup',
        'count': 'count',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, resource_references=None, category_id=None, resource_type=None, resource_group=None, count=None, *args, **kwargs):  # noqa: E501
        """AssociationDetailProjection - a model defined in Swagger
            
        """
        AssociationDetail.__init__(self, resource_references, category_id, resource_type, resource_group, count, *args, **kwargs)
        self.discriminator = None

    def _initialize_object_type(self):
        return 'prism.v4.config.AssociationDetailProjection'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.AssociationDetailProjection'


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
        if issubclass(AssociationDetailProjection, dict):
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
        if not isinstance(other, AssociationDetailProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

