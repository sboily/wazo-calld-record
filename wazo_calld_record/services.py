# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


class RecordService(object):

    def __init__(self, amid, ari, publisher):
        self.amid = amid
        self.ari = ari
        self.publisher = publisher

    def list_records(self):
        return []

    def start_record(self, call_id):
        channel_name = self._get_channel_name(call_id)
        record = {
            'Channel': channel_name,
            'File':  filename
        }
        return self.amid.action('MixMonitor', record)

    def stop_record(self, call_id):
        channel_name = self._get_channel_name(call_id)
        record = {
            'Channel': call_id
        }
        return self.amid.action('StopMixMonitor', record)

    def _get_channel_name(self, call_id):
        channel = self.ari.channels.get(channelId=call_id)
        return channel.json['name']
