# Bloom Filter: Size

## Description

This repo shows how much storage is required for storing XX items into a REDIS Bloom Filter.

## Setup

1. Requires Docker and Docker Compose
1. Open a terminal and `cd` into this directory
1. `docker compose up`
    * If this fails, then change the port in `.env`
1. `docker composer logs bloom_filter_size`
    * This will display the logs from the python container


## Results

The Redis Bloom Filter is created with NO_SCALING to be more memory efficient.

Columns presented below:

1. **Number of Items** - The expected number of items to be inserted
1. **Bloom Filter Size (bytes)** - The size of the bloom filter, as reported by the bloom filter, in bytes
1. **Docs Filter Size (bytes)** - The documentation for [Bloom filters](https://redis.io/commands/bf.reserve/) provides an estimate on the expected size, but we can see that this is very different from what is actually used
1. **Memory Usage (bytes)** - The number of bytes that a key and its value require to be stored in RAM
1. **Error Rate** - The error rate that is set
1. **Number of Filters** - The number of sub-bloom filters, a technique use to enable expansion and scaling. Sub-filters require extra space and extra hash functions.

### Error Rate: 0.001
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 1 | 144 | 0.001 | 6 |
| 10 | 176 | 6 | 160 | 0.001 | 6 |
| 100 | 336 | 54 | 328 | 0.001 | 6 |
| 1,000 | 1,952 | 541 | 1,944 | 0.001 | 6 |
| 10,000 | 18,128 | 5,410 | 18,120 | 0.001 | 6 |
| 100,000 | 179,872 | 54,101 | 179,864 | 0.001 | 6 |
| 1,000,000 | 1,797,352 | 541,011 | 1,797,344 | 0.001 | 6 |
| 10,000,000 | 17,972,144 | 5,410,107 | 17,972,136 | 0.001 | 6 |
| 100,000,000 | 179,720,000 | 54,101,064 | 179,719,992 | 0.001 | 6 |
| 1,000,000,000 | 1,797,198,600 | 541,010,641 | 1,797,198,592 | 0.001 | 6 |

### Error Rate: 0.0001
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 1 | 144 | 0.0001 | 8 |
| 10 | 176 | 8 | 168 | 0.0001 | 8 |
| 100 | 392 | 73 | 384 | 0.0001 | 8 |
| 1,000 | 2,552 | 722 | 2,544 | 0.0001 | 8 |
| 10,000 | 24,120 | 7,214 | 24,112 | 0.0001 | 8 |
| 100,000 | 239,784 | 72,135 | 239,776 | 0.0001 | 8 |
| 1,000,000 | 2,396,424 | 721,348 | 2,396,416 | 0.0001 | 8 |
| 10,000,000 | 23,962,800 | 7,213,476 | 23,962,792 | 0.0001 | 8 |
| 100,000,000 | 239,626,616 | 72,134,752 | 239,626,608 | 0.0001 | 8 |
| 1,000,000,000 | 2,396,264,752 | 721,347,521 | 2,396,264,752 | 0.0001 | 8 |

### Error Rate: 1e-05
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 1 | 144 | 1e-05 | 10 |
| 10 | 184 | 9 | 168 | 1e-05 | 10 |
| 100 | 456 | 91 | 448 | 1e-05 | 10 |
| 1,000 | 3,152 | 902 | 3,144 | 1e-05 | 10 |
| 10,000 | 30,112 | 9,017 | 30,104 | 1e-05 | 10 |
| 100,000 | 299,688 | 90,169 | 299,680 | 1e-05 | 10 |
| 1,000,000 | 2,995,488 | 901,685 | 2,995,480 | 1e-05 | 10 |
| 10,000,000 | 29,953,464 | 9,016,844 | 29,953,456 | 1e-05 | 10 |
| 100,000,000 | 299,533,232 | 90,168,440 | 299,533,224 | 1e-05 | 10 |
| 1,000,000,000 | 2,995,330,896 | 901,684,401 | 2,995,330,888 | 1e-05 | 10 |

### Error Rate: 1e-06
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 1 | 144 | 1e-06 | 12 |
| 10 | 192 | 11 | 176 | 1e-06 | 12 |
| 100 | 512 | 109 | 504 | 1e-06 | 12 |
| 1,000 | 3,752 | 1,082 | 3,744 | 1e-06 | 12 |
| 10,000 | 36,096 | 10,821 | 36,088 | 1e-06 | 12 |
| 100,000 | 359,592 | 108,203 | 359,584 | 1e-06 | 12 |
| 1,000,000 | 3,594,552 | 1,082,022 | 3,594,544 | 1e-06 | 12 |
| 10,000,000 | 35,944,128 | 10,820,213 | 35,944,120 | 1e-06 | 12 |
| 100,000,000 | 359,439,848 | 108,202,128 | 359,439,840 | 1e-06 | 12 |
| 1,000,000,000 | 3,594,397,048 | 1,082,021,281 | 3,594,397,040 | 1e-06 | 12 |

### Error Rate: 1e-07
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 2 | 144 | 1e-07 | 14 |
| 10 | 200 | 13 | 184 | 1e-07 | 14 |
| 100 | 576 | 127 | 568 | 1e-07 | 14 |
| 1,000 | 4,352 | 1,263 | 4,344 | 1e-07 | 14 |
| 10,000 | 42,088 | 12,624 | 42,080 | 1e-07 | 14 |
| 100,000 | 419,504 | 126,236 | 419,496 | 1e-07 | 14 |
| 1,000,000 | 4,193,616 | 1,262,359 | 4,193,608 | 1e-07 | 14 |
| 10,000,000 | 41,934,784 | 12,623,582 | 41,934,776 | 1e-07 | 14 |
| 100,000,000 | 419,346,456 | 126,235,816 | 419,346,448 | 1e-07 | 14 |
| 1,000,000,000 | 4,193,463,192 | 1,262,358,161 | 4,193,463,184 | 1e-07 | 14 |

### Error Rate: 1e-08
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 2 | 144 | 1e-08 | 16 |
| 10 | 200 | 15 | 184 | 1e-08 | 16 |
| 100 | 632 | 145 | 624 | 1e-08 | 16 |
| 1,000 | 4,952 | 1,443 | 4,944 | 1e-08 | 16 |
| 10,000 | 48,080 | 14,427 | 48,072 | 1e-08 | 16 |
| 100,000 | 479,408 | 144,270 | 479,400 | 1e-08 | 16 |
| 1,000,000 | 4,792,688 | 1,442,695 | 4,792,680 | 1e-08 | 16 |
| 10,000,000 | 47,925,448 | 14,426,951 | 47,925,440 | 1e-08 | 16 |
| 100,000,000 | 479,253,072 | 144,269,504 | 479,253,064 | 1e-08 | 16 |
| 1,000,000,000 | 4,792,529,344 | 1,442,695,041 | 4,792,529,336 | 1e-08 | 16 |

### Error Rate: 1e-09
| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |
|---|---|---|---|---|---|
| 1 | 160 | 2 | 144 | 1e-09 | 18 |
| 10 | 208 | 17 | 192 | 1e-09 | 18 |
| 100 | 696 | 163 | 688 | 1e-09 | 18 |
| 1,000 | 5,544 | 1,623 | 5,536 | 1e-09 | 18 |
| 10,000 | 54,072 | 16,231 | 54,064 | 1e-09 | 18 |
| 100,000 | 539,312 | 162,304 | 539,304 | 1e-09 | 18 |
| 1,000,000 | 5,391,752 | 1,623,032 | 5,391,744 | 1e-09 | 18 |
| 10,000,000 | 53,916,112 | 16,230,320 | 53,916,104 | 1e-09 | 18 |
| 100,000,000 | 539,159,688 | 162,303,192 | 539,159,680 | 1e-09 | 18 |
| 1,000,000,000 | 5,391,595,496 | 1,623,031,921 | 5,391,595,488 | 1e-09 | 18 |