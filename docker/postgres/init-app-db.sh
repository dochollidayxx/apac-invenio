#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 IBM.
#
# APAC is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE apac WITH LOGIN PASSWORD 'apac';
    ALTER ROLE apac CREATEDB;
    \du;
EOSQL
