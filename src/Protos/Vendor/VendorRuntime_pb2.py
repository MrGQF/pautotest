# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protos/Vendor/VendorRuntime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Protos.Common import Common_pb2 as Protos_dot_Common_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!Protos/Vendor/VendorRuntime.proto\x12\x10VendorRuntimeRpc\x1a\x1aProtos/Common/Common.proto2\xc7\x01\n\x14VendorRuntimeService\x12\x35\n\x06Invoke\x12\x18.CommonRpc.InvokeRequest\x1a\x11.CommonRpc.Result\x12\x42\n\x11InvokeReturnAsync\x12\x18.CommonRpc.InvokeRequest\x1a\x11.CommonRpc.Result0\x01\x12\x34\n\x06Notify\x12\x17.CommonRpc.Notification\x1a\x11.CommonRpc.ResultB\x16\xaa\x02\x13VendorRuntimeRpc.V1b\x06proto3')



_VENDORRUNTIMESERVICE = DESCRIPTOR.services_by_name['VendorRuntimeService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\023VendorRuntimeRpc.V1'
  _VENDORRUNTIMESERVICE._serialized_start=84
  _VENDORRUNTIMESERVICE._serialized_end=283
# @@protoc_insertion_point(module_scope)
