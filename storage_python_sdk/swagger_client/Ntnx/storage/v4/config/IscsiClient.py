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
from swagger_client.Ntnx.common.v1.config.IPAddressOrFQDN import IPAddressOrFQDN  # noqa: F401,E501
from swagger_client.Ntnx.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from swagger_client.Ntnx.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from swagger_client.Ntnx.storage.v4.config.AuthenticationType import AuthenticationType  # noqa: F401,E501
from swagger_client.Ntnx.storage.v4.config.TargetParam import TargetParam  # noqa: F401,E501


class IscsiClient(ExternalizableAbstractModel):
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
        'iscsi_initiator_name': 'str',
        'iscsi_initiator_network_id': 'common.v1.config.IPAddressOrFQDN',
        'client_secret': 'str',
        'enabled_authentications': 'storage.v4.config.AuthenticationType',
        'target_params': 'list[storage.v4.config.TargetParam]',
        'cluster_reference': 'str',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'iscsi_initiator_name': 'iscsiInitiatorName',
        'iscsi_initiator_network_id': 'iscsiInitiatorNetworkId',
        'client_secret': 'clientSecret',
        'enabled_authentications': 'enabledAuthentications',
        'target_params': 'targetParams',
        'cluster_reference': 'clusterReference',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }


    def __init__(self, iscsi_initiator_name=None, iscsi_initiator_network_id=None, client_secret=None, enabled_authentications=None, target_params=None, cluster_reference=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        """IscsiClient - a model defined in Swagger"""  # noqa: E501
        self._iscsi_initiator_name = None
        self._iscsi_initiator_network_id = None
        self._client_secret = None
        self._enabled_authentications = None
        self._target_params = None
        self._cluster_reference = None
        self.discriminator = None
        if iscsi_initiator_name is not None:
            self._iscsi_initiator_name = iscsi_initiator_name
        if iscsi_initiator_network_id is not None:
            self._iscsi_initiator_network_id = iscsi_initiator_network_id
        if client_secret is not None:
            self._client_secret = client_secret
        if enabled_authentications is not None:
            self._enabled_authentications = enabled_authentications
        if target_params is not None:
            self._target_params = target_params
        if cluster_reference is not None:
            self._cluster_reference = cluster_reference
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)

    def _initialize_object_type(self):
        return 'storage.v4.config.IscsiClient'

    def _initialize_fq_object_type(self):
        return 'storage.v4.r0.a1.config.IscsiClient'


    @property
    def iscsi_initiator_name(self):
        """Gets the iscsi_initiator_name of this IscsiClient.  # noqa: E501

        iSCSI Initiator Name.  # noqa: E501

        :return: The iscsi_initiator_name of this IscsiClient.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_initiator_name

    @iscsi_initiator_name.setter
    def iscsi_initiator_name(self, iscsi_initiator_name):
        """Sets the iscsi_initiator_name of this IscsiClient.

        iSCSI Initiator Name.  # noqa: E501

        :param iscsi_initiator_name: The iscsi_initiator_name of this IscsiClient.  # noqa: E501
        :type: str
        """
        if iscsi_initiator_name is not None and len(iscsi_initiator_name) > 64:
            raise ValueError("Invalid value for `iscsi_initiator_name`, length must be less than or equal to `64`")  # noqa: E501

        self._iscsi_initiator_name = iscsi_initiator_name

    @property
    def iscsi_initiator_network_id(self):
        """Gets the iscsi_initiator_network_id of this IscsiClient.  # noqa: E501


        :return: The iscsi_initiator_network_id of this IscsiClient.  # noqa: E501
        :rtype: common.v1.config.IPAddressOrFQDN
        """
        return self._iscsi_initiator_network_id

    @iscsi_initiator_network_id.setter
    def iscsi_initiator_network_id(self, iscsi_initiator_network_id):
        """Sets the iscsi_initiator_network_id of this IscsiClient.


        :param iscsi_initiator_network_id: The iscsi_initiator_network_id of this IscsiClient.  # noqa: E501
        :type: common.v1.config.IPAddressOrFQDN
        """

        self._iscsi_initiator_network_id = iscsi_initiator_network_id

    @property
    def client_secret(self):
        """Gets the client_secret of this IscsiClient.  # noqa: E501

        iSCSI initiator Client Secret in case of CHAP authentication. This field should not be provided in case the authentication type is not set to CHAP.  # noqa: E501

        :return: The client_secret of this IscsiClient.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this IscsiClient.

        iSCSI initiator Client Secret in case of CHAP authentication. This field should not be provided in case the authentication type is not set to CHAP.  # noqa: E501

        :param client_secret: The client_secret of this IscsiClient.  # noqa: E501
        :type: str
        """
        if client_secret is not None and len(client_secret) > 16:
            raise ValueError("Invalid value for `client_secret`, length must be less than or equal to `16`")  # noqa: E501
        if client_secret is not None and len(client_secret) < 12:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `12`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def enabled_authentications(self):
        """Gets the enabled_authentications of this IscsiClient.  # noqa: E501


        :return: The enabled_authentications of this IscsiClient.  # noqa: E501
        :rtype: storage.v4.config.AuthenticationType
        """
        return self._enabled_authentications

    @enabled_authentications.setter
    def enabled_authentications(self, enabled_authentications):
        """Sets the enabled_authentications of this IscsiClient.


        :param enabled_authentications: The enabled_authentications of this IscsiClient.  # noqa: E501
        :type: storage.v4.config.AuthenticationType
        """

        self._enabled_authentications = enabled_authentications

    @property
    def target_params(self):
        """Gets the target_params of this IscsiClient.  # noqa: E501


        :return: The target_params of this IscsiClient.  # noqa: E501
        :rtype: list[storage.v4.config.TargetParam]
        """
        return self._target_params

    @target_params.setter
    def target_params(self, target_params):
        """Sets the target_params of this IscsiClient.


        :param target_params: The target_params of this IscsiClient.  # noqa: E501
        :type: list[storage.v4.config.TargetParam]
        """

        self._target_params = target_params

    @property
    def cluster_reference(self):
        """Gets the cluster_reference of this IscsiClient.  # noqa: E501

        The UUID of cluster that will host the Volume Group. This is mandatory to be specified for creating a volume group on PC.  # noqa: E501

        :return: The cluster_reference of this IscsiClient.  # noqa: E501
        :rtype: str
        """
        return self._cluster_reference

    @cluster_reference.setter
    def cluster_reference(self, cluster_reference):
        """Sets the cluster_reference of this IscsiClient.

        The UUID of cluster that will host the Volume Group. This is mandatory to be specified for creating a volume group on PC.  # noqa: E501

        :param cluster_reference: The cluster_reference of this IscsiClient.  # noqa: E501
        :type: str
        """
        if cluster_reference is not None and not re.search(r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', cluster_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `cluster_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self._cluster_reference = cluster_reference

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
        if issubclass(IscsiClient, dict):
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
        if not isinstance(other, IscsiClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

