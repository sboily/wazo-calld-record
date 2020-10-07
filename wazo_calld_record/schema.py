# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    fields,
    Schema,
)
from marshmallow.validate import Length

from wazo_calld.plugin_helpers.mallow import StrictDict


class RecordsListSchema(Schema):
    queue = fields.Str(validate=Length(min=1))
    available = fields.Integer()
    logged_in = fields.Integer()
    talk_time = fields.Integer()
    longest_hold_time = fields.Integer()
    talking = fields.Integer()
    callers = fields.Integer()
    hold_time = fields.Integer()

    class Meta:
        strict = True

class RecordSchema(Schema):
    queue = fields.Str(validate=Length(min=1))
    talk_time = fields.Integer()
    hold_time = fields.Integer()
    service_level = fields.Integer()
    abandoned = fields.Integer()
    weight = fields.Integer()
    service_level_perf = fields.Str()
    service_level_perf2 = fields.Str()
    completed = fields.Integer()
    strategy = fields.Str()
    max = fields.Integer()
    calls = fields.Integer()
    members = fields.List(StrictDict(key_field=fields.String(required=True, validate=Length(min=1)),
                                     value_field=fields.String(required=True, validate=Length(min=1)),
                                     missing=dict))

    class Meta:
        strict = True


record_list_schema = RecordsListSchema()
record_schema = RecordSchema()
