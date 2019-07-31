# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 IBM.
#
# APAC is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('apac', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='apac',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='apac Invenio',
    license='MIT',
    author='IBM',
    author_email='adam.holliday@ibm.com',
    url='https://github.com/dochollidayxx/apac',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'apac = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'apac_records = apac.records:APAC',
        ],
        'invenio_base.blueprints': [
            'apac = apac.theme.views:blueprint',
            'apac_records = apac.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'apac_theme = apac.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'apac = apac.config',
        ],
        'invenio_i18n.translations': [
            'messages = apac',
        ],
        'invenio_base.api_apps': [
            'apac = apac.records:APAC',
         ],
        'invenio_jsonschemas.schemas': [
            'apac = apac.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = apac.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
