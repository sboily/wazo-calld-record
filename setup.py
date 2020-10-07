#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

from setuptools import setup
from setuptools import find_packages

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file)

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],

    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'wazo_calld_record': ['api.yml'],
    },
    entry_points={
        'wazo_calld.plugins': [
            'record = wazo_calld_record.plugin:Plugin'
        ],
    },
)
