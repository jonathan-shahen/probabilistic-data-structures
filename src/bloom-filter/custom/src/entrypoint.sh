#!/bin/sh

cd /project

pip install mmh3 bitarray

exec "$@"
