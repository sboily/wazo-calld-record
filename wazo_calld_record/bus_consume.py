# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from xivo_bus.resources.common.event import ArbitraryEvent


logger = logging.getLogger(__name__)


class RecordBusEventHandler(object):

    def __init__(self, bus_publisher):
        self.bus_publisher = bus_publisher

    def subscribe(self, bus_consumer):
        bus_consumer.on_ami_event('MonitorStart', self._monitor_start)
        bus_consumer.on_ami_event('MonitorStop', self._monitor_stop)

    def _monitor_start(self, event):
        bus_event = ArbitraryEvent(
            name='monitor_start',
            body=event,
            required_acl='events.record'
        )
        bus_event.routing_key = 'calls.record.start'
        logger.info(bus_event)
        self.bus_publisher.publish(bus_event)

    def _monitor_stop(self, event):
        bus_event = ArbitraryEvent(
            name='monitor_stop',
            body=event,
            required_acl='events.record'
        )
        logger.info(bus_event)
        bus_event.routing_key = 'calls.record.stop'
        self.bus_publisher.publish(bus_event)
