#!/bin/bash

export PGPASSWORD='123456'; psql -h 'pg_proxy' -U 'postgres' -c 'CREATE DATABASE db;'
