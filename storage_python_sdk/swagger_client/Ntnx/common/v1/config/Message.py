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
from swagger_client.Ntnx.common.v1.config.MessageSeverity import MessageSeverity  # noqa: F401,E501


class Message(object):
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
        'code': 'str',
        'message': 'str',
        'locale': 'str',
        'severity': 'common.v1.config.MessageSeverity',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'locale': 'locale',
        'severity': 'severity',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }


    def __init__(self, code=None, message=None, locale='en_US', severity=None, *args, **kwargs):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._locale = None
        self._severity = None
        self.discriminator = None
        if code is not None:
            self._code = code
        if message is not None:
            self._message = message
        if locale is not None:
            self._locale = locale
        if severity is not None:
            self._severity = severity
        self.__reserved = {"$fqObjectType": self._initialize_fq_object_type()}
        self.__unknown_fields = {}
        self.__object_type = self._initialize_object_type()

    def _initialize_object_type(self):
        return 'common.v1.config.Message'

    def _initialize_fq_object_type(self):
        return 'common.v1.r0.a3.config.Message'

    def get_object_type(self):
        return self.__object_type

    def get_reserved(self):
        return self.__reserved

    def get_unknown_fields(self):
        return self.__unknown_fields

    @property
    def code(self):
        """Gets the code of this Message.  # noqa: E501

        A code that uniquely identifies a message.   # noqa: E501

        :return: The code of this Message.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Message.

        A code that uniquely identifies a message.   # noqa: E501

        :param code: The code of this Message.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this Message.  # noqa: E501


        :return: The message of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Message.


        :param message: The message of this Message.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def locale(self):
        """Gets the locale of this Message.  # noqa: E501

        The locale for the message description.   # noqa: E501

        :return: The locale of this Message.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Message.

        The locale for the message description.   # noqa: E501

        :param locale: The locale of this Message.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def severity(self):
        """Gets the severity of this Message.  # noqa: E501


        :return: The severity of this Message.  # noqa: E501
        :rtype: common.v1.config.MessageSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Message.


        :param severity: The severity of this Message.  # noqa: E501
        :type: common.v1.config.MessageSeverity
        """

        self._severity = severity

    @property
    def _reserved(self):
        """Gets the _reserved of this Message.  # noqa: E501


        :return: The _reserved of this Message.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self.__reserved

    @property
    def _object_type(self):
        """Gets the _object_type of this Message.  # noqa: E501


        :return: The _object_type of this Message.  # noqa: E501
        :rtype: str
        """
        return self.__object_type

    @property
    def _unknown_fields(self):
        """Gets the _unknown_fields of this Message.  # noqa: E501


        :return: The _unknown_fields of this Message.  # noqa: E501
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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

