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
from swagger_client.Ntnx.OneOfstorage.v4.config.MigrateVolumeGroupApiResponsedata import MigrateVolumeGroupApiResponsedata  # noqa: F401,E501
from swagger_client.Ntnx.common.v1.response.ApiResponseMetadata import ApiResponseMetadata  # noqa: F401,E501


class MigrateVolumeGroupApiResponse(object):
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
        'metadata': 'common.v1.response.ApiResponseMetadata',
        'data': 'OneOfstorage.v4.config.MigrateVolumeGroupApiResponsedata',
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
        """MigrateVolumeGroupApiResponse - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._data = None
        self.discriminator = None
        if metadata is not None:
            self._metadata = metadata
        if data is not None:
            self._data = data
        self.__reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        self.__unknown_fields = {}
        self.__object_type = self._initialize_object_type()

    def _initialize_object_type(self):
        return 'storage.v4.config.MigrateVolumeGroupApiResponse'

    def _initialize_fq_object_type(self):
        return 'storage.v4.r0.a1.config.MigrateVolumeGroupApiResponse'

    def get_object_type(self):
        return self.__object_type

    def get_reserved(self):
        return self.__reserved

    def get_unknown_fields(self):
        return self.__unknown_fields

    @property
    def metadata(self):
        """Gets the metadata of this MigrateVolumeGroupApiResponse.  # noqa: E501


        :return: The metadata of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :rtype: common.v1.response.ApiResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MigrateVolumeGroupApiResponse.


        :param metadata: The metadata of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :type: common.v1.response.ApiResponseMetadata
        """

        self._metadata = metadata

    @property
    def data(self):
        """Gets the data of this MigrateVolumeGroupApiResponse.  # noqa: E501


        :return: The data of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :rtype: OneOfstorage.v4.config.MigrateVolumeGroupApiResponsedata
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MigrateVolumeGroupApiResponse.


        :param data: The data of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :type: OneOfstorage.v4.config.MigrateVolumeGroupApiResponsedata
        """

        self._data = data

    @property
    def _reserved(self):
        """Gets the _reserved of this MigrateVolumeGroupApiResponse.  # noqa: E501


        :return: The _reserved of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self.__reserved

    @property
    def _object_type(self):
        """Gets the _object_type of this MigrateVolumeGroupApiResponse.  # noqa: E501


        :return: The _object_type of this MigrateVolumeGroupApiResponse.  # noqa: E501
        :rtype: str
        """
        return self.__object_type

    @property
    def _unknown_fields(self):
        """Gets the _unknown_fields of this MigrateVolumeGroupApiResponse.  # noqa: E501


        :return: The _unknown_fields of this MigrateVolumeGroupApiResponse.  # noqa: E501
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
        if issubclass(MigrateVolumeGroupApiResponse, dict):
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
        if not isinstance(other, MigrateVolumeGroupApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

