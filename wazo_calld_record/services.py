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
        channel = self._get_channel_name(call_id)
        print(channel)
        filename = 'api/{}/user/{}-{}-{}'.format(channel['tenant_uuid'], channel['user_uuid'], channel['extension'], channel['id'])
        record = {
            'Channel': channel['name'],
            'File':  filename,
            'Format': 'wav',
            'Mix': 1
        }
        ami_action = self.amid.action('Monitor', record)
        print(ami_action)
        return ami_action

    def stop_record(self, call_id):
        channel = self._get_channel_name(call_id)
        record = {
            'Channel': channel['name']
        }
        return self.amid.action('StopMonitor', record)

    def _get_channel_name(self, call_id):
        channel = self.ari.channels.get(channelId=call_id)
        return self._channel(channel.json)

    def _channel(self, channel):
        return {
            'id': channel['id'],
            'name': channel['name'],
            'tenant_uuid': channel['channelvars']['WAZO_TENANT_UUID'],
            'created_at': channel['creationtime'],
            'extension': channel['channelvars']['XIVO_BASE_EXTEN'] or channel['caller']['number'],
            'user_uuid': channel['channelvars']['XIVO_USERUUID'] or 'no_user_uuid',
            'account_code': channel['accountcode']
        }
