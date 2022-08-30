#!/bin/sh

cd /project

pip install redis

exec "$@"
