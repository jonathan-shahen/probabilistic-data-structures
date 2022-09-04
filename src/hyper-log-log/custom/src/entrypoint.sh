#!/bin/sh

cd /project

pip install numpy mmh3 bitarray

exec "$@"
