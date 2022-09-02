# Count Min Sketch: Size

## Description

This repo shows how much storage is required for storing XX items into a REDIS Count Min Sketch.

## Setup

1. Requires Docker and Docker Compose
1. Open a terminal and `cd` into this directory
1. `docker compose up`
    * If this fails, then change the port in `.env`
1. `docker composer logs bloom_filter_size`
    * This will display the logs from the python container


## Results

The Redis Count Min Sketch is created with NO_SCALING to be more memory efficient.

Columns presented below:

1. **Number of Items** - The expected number of items to be inserted
1. **Count Min Sketch Size (bytes)** - The size of the bloom filter, as reported by the bloom filter, in bytes
1. **Memory Usage (bytes)** - The number of bytes that a key and its value require to be stored in RAM
1. **Error Rate** - The error rate that is set
1. **Number of Filters** - The number of sub-bloom filters, a technique use to enable expansion and scaling. Sub-filters require extra space and extra hash functions.

