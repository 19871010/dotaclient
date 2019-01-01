# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ModelService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/ModelService.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19protos/ModelService.proto\"\x08\n\x06\x45mpty2\"\x1e\n\x0bWeightQuery\x12\x0f\n\x07version\x18\x01 \x01(\r\"k\n\x07Weights\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.Weights.Status\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\" \n\x06Status\x12\x06\n\x02OK\x10\x01\x12\x0e\n\nUP_TO_DATE\x10\x02\x32Y\n\x0cModelService\x12!\n\nPutWeights\x12\x08.Weights\x1a\x07.Empty2\"\x00\x12&\n\nGetWeights\x12\x0c.WeightQuery\x1a\x08.Weights\"\x00')
)



_WEIGHTS_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Weights.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UP_TO_DATE', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=146,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_WEIGHTS_STATUS)


_EMPTY2 = _descriptor.Descriptor(
  name='Empty2',
  full_name='Empty2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=37,
)


_WEIGHTQUERY = _descriptor.Descriptor(
  name='WeightQuery',
  full_name='WeightQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='WeightQuery.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=69,
)


_WEIGHTS = _descriptor.Descriptor(
  name='Weights',
  full_name='Weights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Weights.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='Weights.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='Weights.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEIGHTS_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=178,
)

_WEIGHTS.fields_by_name['status'].enum_type = _WEIGHTS_STATUS
_WEIGHTS_STATUS.containing_type = _WEIGHTS
DESCRIPTOR.message_types_by_name['Empty2'] = _EMPTY2
DESCRIPTOR.message_types_by_name['WeightQuery'] = _WEIGHTQUERY
DESCRIPTOR.message_types_by_name['Weights'] = _WEIGHTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty2 = _reflection.GeneratedProtocolMessageType('Empty2', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY2,
  __module__ = 'protos.ModelService_pb2'
  # @@protoc_insertion_point(class_scope:Empty2)
  ))
_sym_db.RegisterMessage(Empty2)

WeightQuery = _reflection.GeneratedProtocolMessageType('WeightQuery', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTQUERY,
  __module__ = 'protos.ModelService_pb2'
  # @@protoc_insertion_point(class_scope:WeightQuery)
  ))
_sym_db.RegisterMessage(WeightQuery)

Weights = _reflection.GeneratedProtocolMessageType('Weights', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTS,
  __module__ = 'protos.ModelService_pb2'
  # @@protoc_insertion_point(class_scope:Weights)
  ))
_sym_db.RegisterMessage(Weights)



_MODELSERVICE = _descriptor.ServiceDescriptor(
  name='ModelService',
  full_name='ModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=180,
  serialized_end=269,
  methods=[
  _descriptor.MethodDescriptor(
    name='PutWeights',
    full_name='ModelService.PutWeights',
    index=0,
    containing_service=None,
    input_type=_WEIGHTS,
    output_type=_EMPTY2,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWeights',
    full_name='ModelService.GetWeights',
    index=1,
    containing_service=None,
    input_type=_WEIGHTQUERY,
    output_type=_WEIGHTS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELSERVICE)

DESCRIPTOR.services_by_name['ModelService'] = _MODELSERVICE

# @@protoc_insertion_point(module_scope)