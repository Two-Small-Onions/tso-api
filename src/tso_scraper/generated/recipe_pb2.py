# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tso_scraper/generated/recipe.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'tso_scraper/generated/recipe.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"tso_scraper/generated/recipe.proto\x12\x0btso_scraper\"\x1c\n\rScrapeRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xad\x05\n\x0eScrapeResponse\x12\x13\n\x06\x61uthor\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rcanonical_url\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08\x63\x61tegory\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tcook_time\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05image\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x13\n\x0bingredients\x18\x07 \x03(\t\x12\x19\n\x0cinstructions\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x19\n\x11instructions_list\x18\t \x03(\t\x12\x10\n\x08keywords\x18\n \x03(\t\x12\x15\n\x08language\x18\x0b \x01(\tH\x07\x88\x01\x01\x12\x16\n\tprep_time\x18\x0c \x01(\rH\x08\x88\x01\x01\x12\x12\n\x05title\x18\r \x01(\tH\t\x88\x01\x01\x12\x17\n\ntotal_time\x18\x0e \x01(\rH\n\x88\x01\x01\x12\x14\n\x07\x63uisine\x18\x0f \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04host\x18\x10 \x01(\tH\x0c\x88\x01\x01\x12\x46\n\x11ingredient_groups\x18\x11 \x03(\x0b\x32+.tso_scraper.ScrapeResponse.IngredientGroup\x1a\x37\n\x0fIngredientGroup\x12\x13\n\x0bingredients\x18\x12 \x03(\t\x12\x0f\n\x07purpose\x18\x13 \x01(\tB\t\n\x07_authorB\x10\n\x0e_canonical_urlB\x0b\n\t_categoryB\x0c\n\n_cook_timeB\x0e\n\x0c_descriptionB\x08\n\x06_imageB\x0f\n\r_instructionsB\x0b\n\t_languageB\x0c\n\n_prep_timeB\x08\n\x06_titleB\r\n\x0b_total_timeB\n\n\x08_cuisineB\x07\n\x05_host2S\n\x0eScraperService\x12\x41\n\x06Scrape\x12\x1a.tso_scraper.ScrapeRequest\x1a\x1b.tso_scraper.ScrapeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tso_scraper.generated.recipe_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SCRAPEREQUEST']._serialized_start=51
  _globals['_SCRAPEREQUEST']._serialized_end=79
  _globals['_SCRAPERESPONSE']._serialized_start=82
  _globals['_SCRAPERESPONSE']._serialized_end=767
  _globals['_SCRAPERESPONSE_INGREDIENTGROUP']._serialized_start=540
  _globals['_SCRAPERESPONSE_INGREDIENTGROUP']._serialized_end=595
  _globals['_SCRAPERSERVICE']._serialized_start=769
  _globals['_SCRAPERSERVICE']._serialized_end=852
# @@protoc_insertion_point(module_scope)