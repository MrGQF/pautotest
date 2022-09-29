# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protos/Vendor/VendorHealth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from Protos.Common import Common_pb2 as Protos_dot_Common_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n Protos/Vendor/VendorHealth.proto\x12\x0cVendorHealth\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1aProtos/Common/Common.proto\"M\n\x13VendorHealthRequest\x12\x36\n\x10WidgetInstanceId\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\"H\n\x0cVendorStatus\x12(\n\x02Id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06Status\x18\x02 \x01(\x05\"P\n\x0cWidgetStatus\x12\x30\n\nInstanceId\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06Status\x18\x02 \x01(\x05\"o\n\x14VendorHealthResponse\x12*\n\x06Vendor\x18\x01 \x01(\x0b\x32\x1a.VendorHealth.VendorStatus\x12+\n\x07Widgets\x18\x02 \x03(\x0b\x32\x1a.VendorHealth.WidgetStatus2Z\n\x13VendorHealthService\x12\x43\n\x0bHealthCheck\x12!.VendorHealth.VendorHealthRequest\x1a\x11.CommonRpc.ResultB\x15\xaa\x02\x12VendorHealthRpc.V1b\x06proto3')



_VENDORHEALTHREQUEST = DESCRIPTOR.message_types_by_name['VendorHealthRequest']
_VENDORSTATUS = DESCRIPTOR.message_types_by_name['VendorStatus']
_WIDGETSTATUS = DESCRIPTOR.message_types_by_name['WidgetStatus']
_VENDORHEALTHRESPONSE = DESCRIPTOR.message_types_by_name['VendorHealthResponse']
VendorHealthRequest = _reflection.GeneratedProtocolMessageType('VendorHealthRequest', (_message.Message,), {
  'DESCRIPTOR' : _VENDORHEALTHREQUEST,
  '__module__' : 'Protos.Vendor.VendorHealth_pb2'
  # @@protoc_insertion_point(class_scope:VendorHealth.VendorHealthRequest)
  })
_sym_db.RegisterMessage(VendorHealthRequest)

VendorStatus = _reflection.GeneratedProtocolMessageType('VendorStatus', (_message.Message,), {
  'DESCRIPTOR' : _VENDORSTATUS,
  '__module__' : 'Protos.Vendor.VendorHealth_pb2'
  # @@protoc_insertion_point(class_scope:VendorHealth.VendorStatus)
  })
_sym_db.RegisterMessage(VendorStatus)

WidgetStatus = _reflection.GeneratedProtocolMessageType('WidgetStatus', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETSTATUS,
  '__module__' : 'Protos.Vendor.VendorHealth_pb2'
  # @@protoc_insertion_point(class_scope:VendorHealth.WidgetStatus)
  })
_sym_db.RegisterMessage(WidgetStatus)

VendorHealthResponse = _reflection.GeneratedProtocolMessageType('VendorHealthResponse', (_message.Message,), {
  'DESCRIPTOR' : _VENDORHEALTHRESPONSE,
  '__module__' : 'Protos.Vendor.VendorHealth_pb2'
  # @@protoc_insertion_point(class_scope:VendorHealth.VendorHealthResponse)
  })
_sym_db.RegisterMessage(VendorHealthResponse)

_VENDORHEALTHSERVICE = DESCRIPTOR.services_by_name['VendorHealthService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022VendorHealthRpc.V1'
  _VENDORHEALTHREQUEST._serialized_start=110
  _VENDORHEALTHREQUEST._serialized_end=187
  _VENDORSTATUS._serialized_start=189
  _VENDORSTATUS._serialized_end=261
  _WIDGETSTATUS._serialized_start=263
  _WIDGETSTATUS._serialized_end=343
  _VENDORHEALTHRESPONSE._serialized_start=345
  _VENDORHEALTHRESPONSE._serialized_end=456
  _VENDORHEALTHSERVICE._serialized_start=458
  _VENDORHEALTHSERVICE._serialized_end=548
# @@protoc_insertion_point(module_scope)