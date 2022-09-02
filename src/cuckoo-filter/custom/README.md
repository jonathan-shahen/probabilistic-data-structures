# Bloom Filter: Custom Implementation

## Description

This repo shows a custom implementation of a Bloom Filter.

## Setup

1. Requires Docker and Docker Compose
1. Open a terminal and `cd` into this directory
1. `docker compose up`
1. `docker composer logs bloom_filter_custom`
    * This will display the logs from the python container


## References

This is inspired by the implementation presented in the book `Algorithms and Data Structures for Massive Datasets`
by Dzejla Medjedovic and Emin Tahirovic

## Results

### Error Rate: 0.001
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 4 | 0.001 | 9 |
| 10 | 18 | 0.001 | 9 |
| 100 | 180 | 0.001 | 9 |
| 1,000 | 1,798 | 0.001 | 9 |
| 10,000 | 17,972 | 0.001 | 9 |
| 100,000 | 179,720 | 0.001 | 9 |
| 1,000,000 | 1,797,199 | 0.001 | 9 |
| 10,000,000 | 17,971,985 | 0.001 | 9 |
| 100,000,000 | 179,719,845 | 0.001 | 9 |
| 1,000,000,000 | 1,797,198,446 | 0.001 | 9 |

### Error Rate: 0.0001
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 5 | 0.0001 | 13 |
| 10 | 24 | 0.0001 | 13 |
| 100 | 240 | 0.0001 | 13 |
| 1,000 | 2,397 | 0.0001 | 13 |
| 10,000 | 23,963 | 0.0001 | 13 |
| 100,000 | 239,627 | 0.0001 | 13 |
| 1,000,000 | 2,396,265 | 0.0001 | 13 |
| 10,000,000 | 23,962,646 | 0.0001 | 13 |
| 100,000,000 | 239,626,460 | 0.0001 | 13 |
| 1,000,000,000 | 2,396,264,595 | 0.0001 | 13 |

### Error Rate: 1e-05
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 6 | 1e-05 | 16 |
| 10 | 30 | 1e-05 | 16 |
| 100 | 300 | 1e-05 | 16 |
| 1,000 | 2,996 | 1e-05 | 16 |
| 10,000 | 29,954 | 1e-05 | 16 |
| 100,000 | 299,533 | 1e-05 | 16 |
| 1,000,000 | 2,995,331 | 1e-05 | 16 |
| 10,000,000 | 29,953,308 | 1e-05 | 16 |
| 100,000,000 | 299,533,075 | 1e-05 | 16 |
| 1,000,000,000 | 2,995,330,743 | 1e-05 | 16 |

### Error Rate: 1e-06
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 8 | 1e-06 | 19 |
| 10 | 36 | 1e-06 | 19 |
| 100 | 360 | 1e-06 | 19 |
| 1,000 | 3,595 | 1e-06 | 19 |
| 10,000 | 35,944 | 1e-06 | 19 |
| 100,000 | 359,440 | 1e-06 | 19 |
| 1,000,000 | 3,594,397 | 1e-06 | 19 |
| 10,000,000 | 35,943,969 | 1e-06 | 19 |
| 100,000,000 | 359,439,690 | 1e-06 | 19 |
| 1,000,000,000 | 3,594,396,892 | 1e-06 | 19 |

### Error Rate: 1e-07
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 9 | 1e-07 | 23 |
| 10 | 42 | 1e-07 | 23 |
| 100 | 420 | 1e-07 | 23 |
| 1,000 | 4,194 | 1e-07 | 23 |
| 10,000 | 41,935 | 1e-07 | 23 |
| 100,000 | 419,347 | 1e-07 | 23 |
| 1,000,000 | 4,193,463 | 1e-07 | 23 |
| 10,000,000 | 41,934,631 | 1e-07 | 23 |
| 100,000,000 | 419,346,304 | 1e-07 | 23 |
| 1,000,000,000 | 4,193,463,040 | 1e-07 | 23 |

### Error Rate: 1e-08
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 10 | 1e-08 | 26 |
| 10 | 48 | 1e-08 | 26 |
| 100 | 480 | 1e-08 | 26 |
| 1,000 | 4,793 | 1e-08 | 26 |
| 10,000 | 47,926 | 1e-08 | 26 |
| 100,000 | 479,253 | 1e-08 | 26 |
| 1,000,000 | 4,792,530 | 1e-08 | 26 |
| 10,000,000 | 47,925,292 | 1e-08 | 26 |
| 100,000,000 | 479,252,919 | 1e-08 | 26 |
| 1,000,000,000 | 4,792,529,189 | 1e-08 | 26 |

### Error Rate: 1e-09
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 11 | 1e-09 | 29 |
| 10 | 54 | 1e-09 | 29 |
| 100 | 540 | 1e-09 | 29 |
| 1,000 | 5,392 | 1e-09 | 29 |
| 10,000 | 53,916 | 1e-09 | 29 |
| 100,000 | 539,160 | 1e-09 | 29 |
| 1,000,000 | 5,391,596 | 1e-09 | 29 |
| 10,000,000 | 53,915,954 | 1e-09 | 29 |
| 100,000,000 | 539,159,534 | 1e-09 | 29 |
| 1,000,000,000 | 5,391,595,338 | 1e-09 | 29 |