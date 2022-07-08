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
from swagger_client.Ntnx.common.v1.response.ApiLink import ApiLink  # noqa: F401,E501
from swagger_client.Ntnx.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel  # noqa: F401,E501
from swagger_client.Ntnx.storage.v4.config.AuthenticationType import AuthenticationType  # noqa: F401,E501
from swagger_client.Ntnx.storage.v4.config.SharingStatus import SharingStatus  # noqa: F401,E501
from swagger_client.Ntnx.storage.v4.config.StorageFeatures import StorageFeatures  # noqa: F401,E501


class VolumeGroup(ExternalizableAbstractModel):
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
        'description': 'str',
        'load_balance_vm_attachments': 'bool',
        'sharing_status': 'storage.v4.config.SharingStatus',
        'iscsi_target_prefix': 'str',
        'iscsi_target_name': 'str',
        'target_secret': 'str',
        'enabled_authentications': 'storage.v4.config.AuthenticationType',
        'created_by': 'str',
        'cluster_reference': 'str',
        'storage_features': 'storage.v4.config.StorageFeatures',
        'ext_id': 'str',
        'links': 'list[common.v1.response.ApiLink]',
        'tenant_id': 'str',
        '_reserved': 'dict(str, object)',
        '_object_type': 'str',
        '_unknown_fields': 'dict(str, object)',
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'load_balance_vm_attachments': 'loadBalanceVmAttachments',
        'sharing_status': 'sharingStatus',
        'iscsi_target_prefix': 'iscsiTargetPrefix',
        'iscsi_target_name': 'iscsiTargetName',
        'target_secret': 'targetSecret',
        'enabled_authentications': 'enabledAuthentications',
        'created_by': 'createdBy',
        'cluster_reference': 'clusterReference',
        'storage_features': 'storageFeatures',
        'ext_id': 'extId',
        'links': 'links',
        'tenant_id': 'tenantId',
        '_reserved': '$reserved',
        '_object_type': '$objectType',
        '_unknown_fields': '$unknownFields',
    }


    def __init__(self, name=None, description=None, load_balance_vm_attachments=None, sharing_status=None, iscsi_target_prefix=None, iscsi_target_name=None, target_secret=None, enabled_authentications=None, created_by=None, cluster_reference=None, storage_features=None, ext_id=None, links=None, tenant_id=None, *args, **kwargs):  # noqa: E501
        """VolumeGroup - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._load_balance_vm_attachments = None
        self._sharing_status = None
        self._iscsi_target_prefix = None
        self._iscsi_target_name = None
        self._target_secret = None
        self._enabled_authentications = None
        self._created_by = None
        self._cluster_reference = None
        self._storage_features = None
        self.discriminator = None
        if name is not None:
            self._name = name
        if description is not None:
            self._description = description
        if load_balance_vm_attachments is not None:
            self._load_balance_vm_attachments = load_balance_vm_attachments
        if sharing_status is not None:
            self._sharing_status = sharing_status
        if iscsi_target_prefix is not None:
            self._iscsi_target_prefix = iscsi_target_prefix
        if iscsi_target_name is not None:
            self._iscsi_target_name = iscsi_target_name
        if target_secret is not None:
            self._target_secret = target_secret
        if enabled_authentications is not None:
            self._enabled_authentications = enabled_authentications
        if created_by is not None:
            self._created_by = created_by
        if cluster_reference is not None:
            self._cluster_reference = cluster_reference
        if storage_features is not None:
            self._storage_features = storage_features
        ExternalizableAbstractModel.__init__(self, ext_id, links, tenant_id, *args, **kwargs)

    def _initialize_object_type(self):
        return 'storage.v4.config.VolumeGroup'

    def _initialize_fq_object_type(self):
        return 'storage.v4.r0.a1.config.VolumeGroup'


    @property
    def name(self):
        """Gets the name of this VolumeGroup.  # noqa: E501

        The name of the Volume Group.  # noqa: E501

        :return: The name of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroup.

        The name of the Volume Group.  # noqa: E501

        :param name: The name of this VolumeGroup.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VolumeGroup.  # noqa: E501

        The description of the Volume Group.  # noqa: E501

        :return: The description of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeGroup.

        The description of the Volume Group.  # noqa: E501

        :param description: The description of this VolumeGroup.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self._description = description

    @property
    def load_balance_vm_attachments(self):
        """Gets the load_balance_vm_attachments of this VolumeGroup.  # noqa: E501

        Whether to enable volume group load balancing for VM attachments. This cannot be enabled if there are iSCSI client attachments already associated with the Volume Group, and vice-versa.  # noqa: E501

        :return: The load_balance_vm_attachments of this VolumeGroup.  # noqa: E501
        :rtype: bool
        """
        return self._load_balance_vm_attachments

    @load_balance_vm_attachments.setter
    def load_balance_vm_attachments(self, load_balance_vm_attachments):
        """Sets the load_balance_vm_attachments of this VolumeGroup.

        Whether to enable volume group load balancing for VM attachments. This cannot be enabled if there are iSCSI client attachments already associated with the Volume Group, and vice-versa.  # noqa: E501

        :param load_balance_vm_attachments: The load_balance_vm_attachments of this VolumeGroup.  # noqa: E501
        :type: bool
        """

        self._load_balance_vm_attachments = load_balance_vm_attachments

    @property
    def sharing_status(self):
        """Gets the sharing_status of this VolumeGroup.  # noqa: E501


        :return: The sharing_status of this VolumeGroup.  # noqa: E501
        :rtype: storage.v4.config.SharingStatus
        """
        return self._sharing_status

    @sharing_status.setter
    def sharing_status(self, sharing_status):
        """Sets the sharing_status of this VolumeGroup.


        :param sharing_status: The sharing_status of this VolumeGroup.  # noqa: E501
        :type: storage.v4.config.SharingStatus
        """

        self._sharing_status = sharing_status

    @property
    def iscsi_target_prefix(self):
        """Gets the iscsi_target_prefix of this VolumeGroup.  # noqa: E501

        iSCSI target prefix-name. The spec should not comprise both iscsi target prefix and iscsi target name.  # noqa: E501

        :return: The iscsi_target_prefix of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_target_prefix

    @iscsi_target_prefix.setter
    def iscsi_target_prefix(self, iscsi_target_prefix):
        """Sets the iscsi_target_prefix of this VolumeGroup.

        iSCSI target prefix-name. The spec should not comprise both iscsi target prefix and iscsi target name.  # noqa: E501

        :param iscsi_target_prefix: The iscsi_target_prefix of this VolumeGroup.  # noqa: E501
        :type: str
        """
        if iscsi_target_prefix is not None and len(iscsi_target_prefix) > 512:
            raise ValueError("Invalid value for `iscsi_target_prefix`, length must be less than or equal to `512`")  # noqa: E501
        if iscsi_target_prefix is not None and not re.search(r'^[\\da-zA-Z:\\.\\-]+$', iscsi_target_prefix):  # noqa: E501
            raise ValueError(r"Invalid value for `iscsi_target_prefix`, must be a follow pattern or equal to `/^[\\da-zA-Z:\\.\\-]+$/`")  # noqa: E501

        self._iscsi_target_prefix = iscsi_target_prefix

    @property
    def iscsi_target_name(self):
        """Gets the iscsi_target_name of this VolumeGroup.  # noqa: E501

        iSCSI target full name. The spec should not comprise both iscsi target prefix and iscsi target name.  # noqa: E501

        :return: The iscsi_target_name of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_target_name

    @iscsi_target_name.setter
    def iscsi_target_name(self, iscsi_target_name):
        """Sets the iscsi_target_name of this VolumeGroup.

        iSCSI target full name. The spec should not comprise both iscsi target prefix and iscsi target name.  # noqa: E501

        :param iscsi_target_name: The iscsi_target_name of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._iscsi_target_name = iscsi_target_name

    @property
    def target_secret(self):
        """Gets the target_secret of this VolumeGroup.  # noqa: E501

        Target Secret in case of CHAP authentication. This field should not be provided in case the authentication type is not set to CHAP.  # noqa: E501

        :return: The target_secret of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._target_secret

    @target_secret.setter
    def target_secret(self, target_secret):
        """Sets the target_secret of this VolumeGroup.

        Target Secret in case of CHAP authentication. This field should not be provided in case the authentication type is not set to CHAP.  # noqa: E501

        :param target_secret: The target_secret of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._target_secret = target_secret

    @property
    def enabled_authentications(self):
        """Gets the enabled_authentications of this VolumeGroup.  # noqa: E501


        :return: The enabled_authentications of this VolumeGroup.  # noqa: E501
        :rtype: storage.v4.config.AuthenticationType
        """
        return self._enabled_authentications

    @enabled_authentications.setter
    def enabled_authentications(self, enabled_authentications):
        """Sets the enabled_authentications of this VolumeGroup.


        :param enabled_authentications: The enabled_authentications of this VolumeGroup.  # noqa: E501
        :type: storage.v4.config.AuthenticationType
        """

        self._enabled_authentications = enabled_authentications

    @property
    def created_by(self):
        """Gets the created_by of this VolumeGroup.  # noqa: E501

        Service/user who created this Volume Group.  # noqa: E501

        :return: The created_by of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this VolumeGroup.

        Service/user who created this Volume Group.  # noqa: E501

        :param created_by: The created_by of this VolumeGroup.  # noqa: E501
        :type: str
        """
        if created_by is not None and len(created_by) > 512:
            raise ValueError("Invalid value for `created_by`, length must be less than or equal to `512`")  # noqa: E501

        self._created_by = created_by

    @property
    def cluster_reference(self):
        """Gets the cluster_reference of this VolumeGroup.  # noqa: E501

        The UUID of cluster that will host the Volume Group. This is mandatory to be specified for creating a volume group on PC.  # noqa: E501

        :return: The cluster_reference of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._cluster_reference

    @cluster_reference.setter
    def cluster_reference(self, cluster_reference):
        """Sets the cluster_reference of this VolumeGroup.

        The UUID of cluster that will host the Volume Group. This is mandatory to be specified for creating a volume group on PC.  # noqa: E501

        :param cluster_reference: The cluster_reference of this VolumeGroup.  # noqa: E501
        :type: str
        """
        if cluster_reference is not None and not re.search(r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', cluster_reference):  # noqa: E501
            raise ValueError(r"Invalid value for `cluster_reference`, must be a follow pattern or equal to `/^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$/`")  # noqa: E501

        self._cluster_reference = cluster_reference

    @property
    def storage_features(self):
        """Gets the storage_features of this VolumeGroup.  # noqa: E501


        :return: The storage_features of this VolumeGroup.  # noqa: E501
        :rtype: storage.v4.config.StorageFeatures
        """
        return self._storage_features

    @storage_features.setter
    def storage_features(self, storage_features):
        """Sets the storage_features of this VolumeGroup.


        :param storage_features: The storage_features of this VolumeGroup.  # noqa: E501
        :type: storage.v4.config.StorageFeatures
        """

        self._storage_features = storage_features

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
        if issubclass(VolumeGroup, dict):
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
        if not isinstance(other, VolumeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

