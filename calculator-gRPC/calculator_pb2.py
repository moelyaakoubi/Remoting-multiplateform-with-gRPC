# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculator.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"/\n\x11\x41rithmeticRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"$\n\x12\x41rithmeticResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\xe8\x01\n\nCalculator\x12\x44\n\x03\x41\x64\x64\x12\x1d.calculator.ArithmeticRequest\x1a\x1e.calculator.ArithmeticResponse\x12I\n\x08Multiply\x12\x1d.calculator.ArithmeticRequest\x1a\x1e.calculator.ArithmeticResponse\x12I\n\x08Subtract\x12\x1d.calculator.ArithmeticRequest\x1a\x1e.calculator.ArithmeticResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ARITHMETICREQUEST']._serialized_start=32
  _globals['_ARITHMETICREQUEST']._serialized_end=79
  _globals['_ARITHMETICRESPONSE']._serialized_start=81
  _globals['_ARITHMETICRESPONSE']._serialized_end=117
  _globals['_CALCULATOR']._serialized_start=120
  _globals['_CALCULATOR']._serialized_end=352
# @@protoc_insertion_point(module_scope)
