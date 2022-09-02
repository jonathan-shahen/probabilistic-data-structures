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

### Number Hashes: 1
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 1 | 1 | 64.00B | 64 |
| 1 | 10 | 136.00B | 136 |
| 1 | 100 | 856.00B | 856 |
| 1 | 1,000 |  7.88KiB | 8,064 |
| 1 | 10,000 | 78.19KiB | 80,064 |
| 1 | 100,000 | 781.31KiB | 800,064 |
| 1 | 1,000,000 |  7.63MiB | 8,000,064 |
| 1 | 10,000,000 | 76.29MiB | 80,000,064 |
| 1 | 100,000,000 | 762.94MiB | 800,000,064 |
| 1 | 1,000,000,000 |  7.45GiB | 8,000,000,064 |

### Number Hashes: 2
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 2 | 1 | 72.00B | 72 |
| 2 | 10 | 216.00B | 216 |
| 2 | 100 |  1.62KiB | 1,656 |
| 2 | 1,000 | 15.69KiB | 16,064 |
| 2 | 10,000 | 156.31KiB | 160,064 |
| 2 | 100,000 |  1.53MiB | 1,600,064 |
| 2 | 1,000,000 | 15.26MiB | 16,000,064 |
| 2 | 10,000,000 | 152.59MiB | 160,000,064 |
| 2 | 100,000,000 |  1.49GiB | 1,600,000,064 |
| 2 | 1,000,000,000 | 14.90GiB | 16,000,000,064 |

### Number Hashes: 3
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 3 | 1 | 80.00B | 80 |
| 3 | 10 | 296.00B | 296 |
| 3 | 100 |  2.40KiB | 2,456 |
| 3 | 1,000 | 23.50KiB | 24,064 |
| 3 | 10,000 | 234.44KiB | 240,064 |
| 3 | 100,000 |  2.29MiB | 2,400,064 |
| 3 | 1,000,000 | 22.89MiB | 24,000,064 |
| 3 | 10,000,000 | 228.88MiB | 240,000,064 |
| 3 | 100,000,000 |  2.24GiB | 2,400,000,064 |
| 3 | 1,000,000,000 | 22.35GiB | 24,000,000,064 |

### Number Hashes: 5
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 5 | 1 | 96.00B | 96 |
| 5 | 10 | 456.00B | 456 |
| 5 | 100 |  3.96KiB | 4,056 |
| 5 | 1,000 | 39.12KiB | 40,064 |
| 5 | 10,000 | 390.69KiB | 400,064 |
| 5 | 100,000 |  3.81MiB | 4,000,064 |
| 5 | 1,000,000 | 38.15MiB | 40,000,064 |
| 5 | 10,000,000 | 381.47MiB | 400,000,064 |
| 5 | 100,000,000 |  3.73GiB | 4,000,000,064 |
| 5 | 1,000,000,000 | 37.25GiB | 40,000,000,064 |

### Number Hashes: 10
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 10 | 1 | 136.00B | 136 |
| 10 | 10 | 856.00B | 856 |
| 10 | 100 |  7.88KiB | 8,064 |
| 10 | 1,000 | 78.19KiB | 80,064 |
| 10 | 10,000 | 781.31KiB | 800,064 |
| 10 | 100,000 |  7.63MiB | 8,000,064 |
| 10 | 1,000,000 | 76.29MiB | 80,000,064 |
| 10 | 10,000,000 | 762.94MiB | 800,000,064 |
| 10 | 100,000,000 |  7.45GiB | 8,000,000,064 |
| 10 | 1,000,000,000 | 74.51GiB | 80,000,000,064 |

### Number Hashes: 15
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 15 | 1 | 176.00B | 176 |
| 15 | 10 |  1.23KiB | 1,256 |
| 15 | 100 | 11.78KiB | 12,064 |
| 15 | 1,000 | 117.25KiB | 120,064 |
| 15 | 10,000 |  1.14MiB | 1,200,064 |
| 15 | 100,000 | 11.44MiB | 12,000,064 |
| 15 | 1,000,000 | 114.44MiB | 120,000,064 |
| 15 | 10,000,000 |  1.12GiB | 1,200,000,064 |
| 15 | 100,000,000 | 11.18GiB | 12,000,000,064 |
| 15 | 1,000,000,000 | 111.76GiB | 120,000,000,064 |