# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from flask import request
from flask_restful import Resource

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource

from .schema import (
    record_list_schema,
    record_schema,
)


class RecordsResource(AuthResource):

    def __init__(self, queues_service):
        self._records_service = records_service

    @required_acl('calld.records.read')
    def get(self):
        records = self._records_service.list_records()

        return {
            'items': record_list_schema.dump(records, many=True)
        }, 200


class RecordResource(AuthResource):

    def __init__(self, records_service):
        self._records_service = records_service

    @required_acl('calld.records.{record_uuid}.read')
    def get(self, record_uuid):
        pass

    @required_acl('calld.records.{record_uuid}.delete')
    def delete(self, record_uuid):
        pass


class RecordStartResource(AuthResource):

    def __init__(self, records_service):
        self._records_service = records_service

    @required_acl('calld.records.{call_id}.start')
    def put(self, call_id):
        record = self._records_service.start_record(call_id)

        return record_schema.dump(record)


class RecordStopResource(AuthResource):

    def __init__(self, records_service):
        self._records_service = records_service

    @required_acl('calld.records.{call_id}.stop')
    def put(self, call_id):
        record = self._records_service.stop_record(call_id)

        return record_schema.dump(record)
