# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service/service_spec/example_executable_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service/service_spec/example_executable_service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n5service/service_spec/example_executable_service.proto\"\x1f\n\x07Numbers\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x17\n\x06Result\x12\r\n\x05value\x18\x01 \x01(\x02\x32&\n\x08\x41\x64\x64ition\x12\x1a\n\x03\x61\x64\x64\x12\x08.Numbers\x1a\x07.Result\"\x00\x62\x06proto3')
)




_NUMBERS = _descriptor.Descriptor(
  name='Numbers',
  full_name='Numbers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='Numbers.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='Numbers.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=88,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Result.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['Numbers'] = _NUMBERS
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numbers = _reflection.GeneratedProtocolMessageType('Numbers', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERS,
  __module__ = 'service.service_spec.example_executable_service_pb2'
  # @@protoc_insertion_point(class_scope:Numbers)
  ))
_sym_db.RegisterMessage(Numbers)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'service.service_spec.example_executable_service_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  ))
_sym_db.RegisterMessage(Result)



_ADDITION = _descriptor.ServiceDescriptor(
  name='Addition',
  full_name='Addition',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=115,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='Addition.add',
    index=0,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_RESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADDITION)

DESCRIPTOR.services_by_name['Addition'] = _ADDITION

# @@protoc_insertion_point(module_scope)
