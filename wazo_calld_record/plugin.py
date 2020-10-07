# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_amid_client import Client as AmidClient
from wazo_auth_client import Client as AuthClient

from .resources import (
    RecordsResource,
    RecordResource,
    RecordStartResource,
    RecordStopResource,
    )
from .services import RecordService
from .bus_consume import RecordBusEventHandler


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        ari = dependencies['ari']
        bus_publisher = dependencies['bus_publisher']
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']
        bus_consumer = dependencies['bus_consumer']
        bus_publisher = dependencies['bus_publisher']

        amid_client = AmidClient(**config['amid'])

        token_changed_subscribe(amid_client.set_token)

        records_bus_event_handler = RecordBusEventHandler(bus_publisher)
        records_bus_event_handler.subscribe(bus_consumer)

        records_service = RecordService(amid_client, ari.client, records_bus_event_handler)

        api.add_resource(RecordsResource, '/records', resource_class_args=[records_service])
        api.add_resource(RecordResource, '/records/<record_name>', resource_class_args=[records_service])
        api.add_resource(RecordStartResource, '/records/<call_id>/start', resource_class_args=[records_service])
        api.add_resource(RecordStopResource, '/records/<call_id>/stop', resource_class_args=[records_service])
