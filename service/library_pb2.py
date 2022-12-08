# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\x12\x07library\"\x9b\x01\n\rInventoryItem\x12\n\n\x02id\x18\x01 \x02(\t\x12 \n\x04type\x18\x02 \x01(\x0b\x32\x12.library.OneOfType\x12\x38\n\x06status\x18\x03 \x01(\x0e\x32\x1d.library.InventoryItem.Status:\tAVAILABLE\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\"8\n\tOneOfType\x12\x1d\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.BOOKH\x00\x42\x0c\n\ntype_oneof\"P\n\x04\x42OOK\x12\x0c\n\x04ISBN\x18\x01 \x02(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\r\n\x05genre\x18\x04 \x03(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\"]\n\x11\x42ookCreateRequest\x12\x0c\n\x04ISBN\x18\x01 \x02(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\r\n\x05genre\x18\x04 \x03(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\"%\n\x12\x42ookCreateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0e\x42ookGetRequest\x12\x0c\n\x04ISBN\x18\x01 \x02(\t\"\"\n\x0f\x42ookGetResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9b\x01\n\x10InventoryService\x12G\n\nCreateBook\x12\x1a.library.BookCreateRequest\x1a\x1b.library.BookCreateResponse\"\x00\x12>\n\x07GetBook\x12\x17.library.BookGetRequest\x1a\x18.library.BookGetResponse\"\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'library_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVENTORYITEM._serialized_start=27
  _INVENTORYITEM._serialized_end=182
  _INVENTORYITEM_STATUS._serialized_start=148
  _INVENTORYITEM_STATUS._serialized_end=182
  _ONEOFTYPE._serialized_start=184
  _ONEOFTYPE._serialized_end=240
  _BOOK._serialized_start=242
  _BOOK._serialized_end=322
  _BOOKCREATEREQUEST._serialized_start=324
  _BOOKCREATEREQUEST._serialized_end=417
  _BOOKCREATERESPONSE._serialized_start=419
  _BOOKCREATERESPONSE._serialized_end=456
  _BOOKGETREQUEST._serialized_start=458
  _BOOKGETREQUEST._serialized_end=488
  _BOOKGETRESPONSE._serialized_start=490
  _BOOKGETRESPONSE._serialized_end=524
  _INVENTORYSERVICE._serialized_start=527
  _INVENTORYSERVICE._serialized_end=682
# @@protoc_insertion_point(module_scope)
