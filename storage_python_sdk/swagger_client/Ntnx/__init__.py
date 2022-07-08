# coding: utf-8

# flake8: noqa

"""
    Storage APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 16.1.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from __future__ import absolute_import

# import models into model package
from swagger_client.Ntnx.OneOfcommon.v1.config.KVPairvalue import KVPairvalue
from swagger_client.Ntnx.OneOfstorage.v4.config.AssociateCategoryApiResponsedata import AssociateCategoryApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.AttachIscsiClientApiResponsedata import AttachIscsiClientApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.AttachVmApiResponsedata import AttachVmApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.CreateVolumeDiskApiResponsedata import CreateVolumeDiskApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.CreateVolumeGroupApiResponsedata import CreateVolumeGroupApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.DeleteVolumeDiskApiResponsedata import DeleteVolumeDiskApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.DeleteVolumeGroupApiResponsedata import DeleteVolumeGroupApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.DetachIscsiClientApiResponsedata import DetachIscsiClientApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.DetachVmApiResponsedata import DetachVmApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.DisassociateCategoryApiResponsedata import DisassociateCategoryApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetCategoryAssociationsApiResponsedata import GetCategoryAssociationsApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetExternalAttachmentsApiResponsedata import GetExternalAttachmentsApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetIscsiClientApiResponsedata import GetIscsiClientApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetIscsiClientsApiResponsedata import GetIscsiClientsApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetVmAttachmentsApiResponsedata import GetVmAttachmentsApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetVolumeDiskApiResponsedata import GetVolumeDiskApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetVolumeDisksApiResponsedata import GetVolumeDisksApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetVolumeGroupApiResponsedata import GetVolumeGroupApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.GetVolumeGroupsApiResponsedata import GetVolumeGroupsApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.MigrateVolumeGroupApiResponsedata import MigrateVolumeGroupApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.UpdateIscsiClientApiResponsedata import UpdateIscsiClientApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.UpdateVolumeDiskApiResponsedata import UpdateVolumeDiskApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.config.UpdateVolumeGroupApiResponsedata import UpdateVolumeGroupApiResponsedata
from swagger_client.Ntnx.OneOfstorage.v4.error.ErrorResponseerror import ErrorResponseerror
from swagger_client.Ntnx.common.v1.config.BaseEnum import BaseEnum
from swagger_client.Ntnx.common.v1.config.EntityReference import EntityReference
from swagger_client.Ntnx.common.v1.config.EntityType import EntityType
from swagger_client.Ntnx.common.v1.config.FQDN import FQDN
from swagger_client.Ntnx.common.v1.config.Flag import Flag
from swagger_client.Ntnx.common.v1.config.IPAddressOrFQDN import IPAddressOrFQDN
from swagger_client.Ntnx.common.v1.config.IPv4Address import IPv4Address
from swagger_client.Ntnx.common.v1.config.IPv6Address import IPv6Address
from swagger_client.Ntnx.common.v1.config.KVPair import KVPair
from swagger_client.Ntnx.common.v1.config.Message import Message
from swagger_client.Ntnx.common.v1.config.MessageSeverity import MessageSeverity
from swagger_client.Ntnx.common.v1.config.TenantAwareModel import TenantAwareModel
from swagger_client.Ntnx.common.v1.response.ApiLink import ApiLink
from swagger_client.Ntnx.common.v1.response.ApiResponseMetadata import ApiResponseMetadata
from swagger_client.Ntnx.common.v1.response.ExternalizableAbstractModel import ExternalizableAbstractModel
from swagger_client.Ntnx.storage.v4.config.AssociateCategoryApiResponse import AssociateCategoryApiResponse
from swagger_client.Ntnx.storage.v4.config.AttachIscsiClientApiResponse import AttachIscsiClientApiResponse
from swagger_client.Ntnx.storage.v4.config.AttachVmApiResponse import AttachVmApiResponse
from swagger_client.Ntnx.storage.v4.config.AuthenticationType import AuthenticationType
from swagger_client.Ntnx.storage.v4.config.CategoryDetails import CategoryDetails
from swagger_client.Ntnx.storage.v4.config.CategoryEntityReferences import CategoryEntityReferences
from swagger_client.Ntnx.storage.v4.config.CreateVolumeDiskApiResponse import CreateVolumeDiskApiResponse
from swagger_client.Ntnx.storage.v4.config.CreateVolumeGroupApiResponse import CreateVolumeGroupApiResponse
from swagger_client.Ntnx.storage.v4.config.DeleteVolumeDiskApiResponse import DeleteVolumeDiskApiResponse
from swagger_client.Ntnx.storage.v4.config.DeleteVolumeGroupApiResponse import DeleteVolumeGroupApiResponse
from swagger_client.Ntnx.storage.v4.config.DetachIscsiClientApiResponse import DetachIscsiClientApiResponse
from swagger_client.Ntnx.storage.v4.config.DetachVmApiResponse import DetachVmApiResponse
from swagger_client.Ntnx.storage.v4.config.DisassociateCategoryApiResponse import DisassociateCategoryApiResponse
from swagger_client.Ntnx.storage.v4.config.DiskStorageFeatures import DiskStorageFeatures
from swagger_client.Ntnx.storage.v4.config.FlashMode import FlashMode
from swagger_client.Ntnx.storage.v4.config.GetCategoryAssociationsApiResponse import GetCategoryAssociationsApiResponse
from swagger_client.Ntnx.storage.v4.config.GetExternalAttachmentsApiResponse import GetExternalAttachmentsApiResponse
from swagger_client.Ntnx.storage.v4.config.GetIscsiClientApiResponse import GetIscsiClientApiResponse
from swagger_client.Ntnx.storage.v4.config.GetIscsiClientsApiResponse import GetIscsiClientsApiResponse
from swagger_client.Ntnx.storage.v4.config.GetVmAttachmentsApiResponse import GetVmAttachmentsApiResponse
from swagger_client.Ntnx.storage.v4.config.GetVolumeDiskApiResponse import GetVolumeDiskApiResponse
from swagger_client.Ntnx.storage.v4.config.GetVolumeDisksApiResponse import GetVolumeDisksApiResponse
from swagger_client.Ntnx.storage.v4.config.GetVolumeGroupApiResponse import GetVolumeGroupApiResponse
from swagger_client.Ntnx.storage.v4.config.GetVolumeGroupsApiResponse import GetVolumeGroupsApiResponse
from swagger_client.Ntnx.storage.v4.config.IscsiClient import IscsiClient
from swagger_client.Ntnx.storage.v4.config.MigrateVolumeGroupApiResponse import MigrateVolumeGroupApiResponse
from swagger_client.Ntnx.storage.v4.config.SharingStatus import SharingStatus
from swagger_client.Ntnx.storage.v4.config.StorageFeatures import StorageFeatures
from swagger_client.Ntnx.storage.v4.config.TargetParam import TargetParam
from swagger_client.Ntnx.storage.v4.config.Task import Task
from swagger_client.Ntnx.storage.v4.config.UpdateIscsiClientApiResponse import UpdateIscsiClientApiResponse
from swagger_client.Ntnx.storage.v4.config.UpdateVolumeDiskApiResponse import UpdateVolumeDiskApiResponse
from swagger_client.Ntnx.storage.v4.config.UpdateVolumeGroupApiResponse import UpdateVolumeGroupApiResponse
from swagger_client.Ntnx.storage.v4.config.VmAttachment import VmAttachment
from swagger_client.Ntnx.storage.v4.config.VolumeDisk import VolumeDisk
from swagger_client.Ntnx.storage.v4.config.VolumeGroup import VolumeGroup
from swagger_client.Ntnx.storage.v4.config.VolumeGroupMigrationSpec import VolumeGroupMigrationSpec
from swagger_client.Ntnx.storage.v4.error.AppMessage import AppMessage
from swagger_client.Ntnx.storage.v4.error.ErrorResponse import ErrorResponse
from swagger_client.Ntnx.storage.v4.error.SchemaValidationError import SchemaValidationError
from swagger_client.Ntnx.storage.v4.error.SchemaValidationErrorMessage import SchemaValidationErrorMessage
from swagger_client.api_response import ApiResponse