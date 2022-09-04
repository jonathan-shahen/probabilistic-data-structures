# Count Min Sketch: Custom Implementation

## Description

This repo shows how much storage is required for creating a Custom Count Min Sketch with XX counters and YY hashes.

## Setup

1. Requires Docker and Docker Compose
1. Open a terminal and `cd` into this directory
1. `docker compose up`
1. `docker composer logs bloom_filter_custom`
    * This will display the logs from the python container


## References

This is inspired by the implementation presented in the book `Algorithms and Data Structures for Massive Datasets`
by Dzejla Medjedovic and Emin Tahirovic

## Conclusion

The custom implementation allows us to reduce the counter size, compared to Redis, thus the results below show half the
storage requirements since counters only go up to 4.3 billion.

## Results

1. **Number of Hashes** - The number of hashes to use when creating the CMS
1. **Number of Counters** - The number of counters to use when creating the CMS
1. **Memory Usage (human)** - The size of the CMS in human readable format
1. **Memory Usage (bytes)** - The number of bytes that a key and its value require to be stored in RAM

### Number Hashes: 1
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 1 | 1 |  4.00B | 4 |
| 1 | 10 | 40.00B | 40 |
| 1 | 100 | 400.00B | 400 |
| 1 | 1,000 |  3.91KiB | 4,000 |
| 1 | 10,000 | 39.06KiB | 40,000 |
| 1 | 100,000 | 390.62KiB | 400,000 |
| 1 | 1,000,000 |  3.81MiB | 4,000,000 |
| 1 | 10,000,000 | 38.15MiB | 40,000,000 |
| 1 | 100,000,000 | 381.47MiB | 400,000,000 |
| 1 | 1,000,000,000 |  3.73GiB | 4,000,000,000 |

### Number Hashes: 2
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 2 | 1 |  8.00B | 8 |
| 2 | 10 | 80.00B | 80 |
| 2 | 100 | 800.00B | 800 |
| 2 | 1,000 |  7.81KiB | 8,000 |
| 2 | 10,000 | 78.12KiB | 80,000 |
| 2 | 100,000 | 781.25KiB | 800,000 |
| 2 | 1,000,000 |  7.63MiB | 8,000,000 |
| 2 | 10,000,000 | 76.29MiB | 80,000,000 |
| 2 | 100,000,000 | 762.94MiB | 800,000,000 |
| 2 | 1,000,000,000 |  7.45GiB | 8,000,000,000 |

### Number Hashes: 3
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 3 | 1 | 12.00B | 12 |
| 3 | 10 | 120.00B | 120 |
| 3 | 100 |  1.17KiB | 1,200 |
| 3 | 1,000 | 11.72KiB | 12,000 |
| 3 | 10,000 | 117.19KiB | 120,000 |
| 3 | 100,000 |  1.14MiB | 1,200,000 |
| 3 | 1,000,000 | 11.44MiB | 12,000,000 |
| 3 | 10,000,000 | 114.44MiB | 120,000,000 |
| 3 | 100,000,000 |  1.12GiB | 1,200,000,000 |
| 3 | 1,000,000,000 | 11.18GiB | 12,000,000,000 |

### Number Hashes: 5
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 5 | 1 | 20.00B | 20 |
| 5 | 10 | 200.00B | 200 |
| 5 | 100 |  1.95KiB | 2,000 |
| 5 | 1,000 | 19.53KiB | 20,000 |
| 5 | 10,000 | 195.31KiB | 200,000 |
| 5 | 100,000 |  1.91MiB | 2,000,000 |
| 5 | 1,000,000 | 19.07MiB | 20,000,000 |
| 5 | 10,000,000 | 190.73MiB | 200,000,000 |
| 5 | 100,000,000 |  1.86GiB | 2,000,000,000 |
| 5 | 1,000,000,000 | 18.63GiB | 20,000,000,000 |

### Number Hashes: 10
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 10 | 1 | 40.00B | 40 |
| 10 | 10 | 400.00B | 400 |
| 10 | 100 |  3.91KiB | 4,000 |
| 10 | 1,000 | 39.06KiB | 40,000 |
| 10 | 10,000 | 390.62KiB | 400,000 |
| 10 | 100,000 |  3.81MiB | 4,000,000 |
| 10 | 1,000,000 | 38.15MiB | 40,000,000 |
| 10 | 10,000,000 | 381.47MiB | 400,000,000 |
| 10 | 100,000,000 |  3.73GiB | 4,000,000,000 |
| 10 | 1,000,000,000 | 37.25GiB | 40,000,000,000 |

### Number Hashes: 15
| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |
|---|---|---|---|
| 15 | 1 | 60.00B | 60 |
| 15 | 10 | 600.00B | 600 |
| 15 | 100 |  5.86KiB | 6,000 |
| 15 | 1,000 | 58.59KiB | 60,000 |
| 15 | 10,000 | 585.94KiB | 600,000 |
| 15 | 100,000 |  5.72MiB | 6,000,000 |
| 15 | 1,000,000 | 57.22MiB | 60,000,000 |
| 15 | 10,000,000 | 572.20MiB | 600,000,000 |
| 15 | 100,000,000 |  5.59GiB | 6,000,000,000 |
| 15 | 1,000,000,000 | 55.88GiB | 60,000,000,000 |