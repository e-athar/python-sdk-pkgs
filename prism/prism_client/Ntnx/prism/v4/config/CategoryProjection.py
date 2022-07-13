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
from prism_client.Ntnx.common.v1.config.KVPair import KVPair  # noqa: F401,E501
from prism_client.Ntnx.prism.v4.config.Category import Category  # noqa: F401,E501
from prism_client.Ntnx.prism.v4.config.CategoryAssociationSummaryProjection import CategoryAssociationSummaryProjection  # noqa: F401,E501
from prism_client.Ntnx.prism.v4.config.CategorySummaryProjection import CategorySummaryProjection  # noqa: F401,E501

"""
IGNORE:
NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
IGNORE
"""

class CategoryProjection(Category):
    """CategoryProjection - a model defined in Swagger"""
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
        'category_association_summary_projection': 'prism.v4.config.CategoryAssociationSummaryProjection',
        'category_summary_projection': 'prism.v4.config.CategorySummaryProjection',
        'metadata': 'list[common.v1.config.KVPair]',
        'fq_name': 'str',
        'name': 'str',
        'parent_ext_id': 'str',
        'user_specified_name': 'str',
        'type': 'prism.v4.config.CategoryType',
        'description': 'str',
        'associations': 'list[prism.v4.config.CategoryAssociationSummary]',
        'child_categories': 'list[prism.v4.config.CategorySummary]',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'category_association_summary_projection': 'categoryAssociationSummaryProjection',
        'category_summary_projection': 'categorySummaryProjection',
        'metadata': 'metadata',
        'fq_name': 'fqName',
        'name': 'name',
        'parent_ext_id': 'parentExtId',
        'user_specified_name': 'userSpecifiedName',
        'type': 'type',
        'description': 'description',
        'associations': 'associations',
        'child_categories': 'childCategories',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }



    def __init__(self, category_association_summary_projection=None, category_summary_projection=None, metadata=None, fq_name=None, name=None, parent_ext_id=None, user_specified_name=None, type=None, description=None, associations=None, child_categories=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        """CategoryProjection - a model defined in Swagger
            
        """
        Category.__init__(self, metadata, fq_name, name, parent_ext_id, user_specified_name, type, description, associations, child_categories, ext_id, links, tenant_id, *args, **kwargs)
        self._category_association_summary_projection = None
        self._category_summary_projection = None
        self.discriminator = None
        if category_association_summary_projection is not None:
            self._category_association_summary_projection = category_association_summary_projection
        if category_summary_projection is not None:
            self._category_summary_projection = category_summary_projection

    def _initialize_object_type(self):
        return 'prism.v4.config.CategoryProjection'

    def _initialize_fq_object_type(self):
        return 'prism.v4.r0.a1.config.CategoryProjection'


    @property
    def category_association_summary_projection(self):
        """`{ prism.v4.config.CategoryAssociationSummaryProjection }`
            
        """ # noqa: E501
        return self._category_association_summary_projection

    @category_association_summary_projection.setter
    def category_association_summary_projection(self, category_association_summary_projection):

        self._category_association_summary_projection = category_association_summary_projection

    @property
    def category_summary_projection(self):
        """`{ prism.v4.config.CategorySummaryProjection }`
            
        """ # noqa: E501
        return self._category_summary_projection

    @category_summary_projection.setter
    def category_summary_projection(self, category_summary_projection):

        self._category_summary_projection = category_summary_projection

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
        if issubclass(CategoryProjection, dict):
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
        if not isinstance(other, CategoryProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

