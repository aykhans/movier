# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: recommender.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'recommender.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11recommender.proto\x12\x0brecommender\"\xf8\x01\n\x06\x46ilter\x12\x13\n\tmin_votes\x18\x01 \x01(\rH\x00\x12\x13\n\tmax_votes\x18\x02 \x01(\rH\x01\x12\x12\n\x08min_year\x18\x03 \x01(\rH\x02\x12\x12\n\x08max_year\x18\x04 \x01(\rH\x03\x12\x14\n\nmin_rating\x18\x05 \x01(\x02H\x04\x12\x14\n\nmax_rating\x18\x06 \x01(\x02H\x05\x42\x11\n\x0fmin_votes_oneofB\x11\n\x0fmax_votes_oneofB\x10\n\x0emin_year_oneofB\x10\n\x0emax_year_oneofB\x12\n\x10min_rating_oneofB\x12\n\x10max_rating_oneof\"G\n\x06Weight\x12\x0c\n\x04year\x18\x01 \x01(\r\x12\x0e\n\x06rating\x18\x02 \x01(\r\x12\x0e\n\x06genres\x18\x03 \x01(\r\x12\x0f\n\x07nconsts\x18\x04 \x01(\r\"o\n\x07Request\x12\x0f\n\x07tconsts\x18\x01 \x03(\t\x12\t\n\x01n\x18\x02 \x01(\r\x12#\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x13.recommender.Filter\x12#\n\x06weight\x18\x04 \x01(\x0b\x32\x13.recommender.Weight\"9\n\x08Response\x12-\n\x06movies\x18\x01 \x03(\x0b\x32\x1d.recommender.RecommendedMovie\"3\n\x10RecommendedMovie\x12\x0e\n\x06tconst\x18\x01 \x01(\t\x12\x0f\n\x07weights\x18\x02 \x03(\t2R\n\x0bRecommender\x12\x43\n\x12GetRecommendations\x12\x14.recommender.Request\x1a\x15.recommender.Response\"\x00\x42,Z*github.com/aykhans/movier/server/pkg/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommender_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/aykhans/movier/server/pkg/proto'
  _globals['_FILTER']._serialized_start=35
  _globals['_FILTER']._serialized_end=283
  _globals['_WEIGHT']._serialized_start=285
  _globals['_WEIGHT']._serialized_end=356
  _globals['_REQUEST']._serialized_start=358
  _globals['_REQUEST']._serialized_end=469
  _globals['_RESPONSE']._serialized_start=471
  _globals['_RESPONSE']._serialized_end=528
  _globals['_RECOMMENDEDMOVIE']._serialized_start=530
  _globals['_RECOMMENDEDMOVIE']._serialized_end=581
  _globals['_RECOMMENDER']._serialized_start=583
  _globals['_RECOMMENDER']._serialized_end=665
# @@protoc_insertion_point(module_scope)