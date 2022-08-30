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

### Error Rate: 0.01
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 160 | 0.01 | 1 |
| 10 | 168 | 0.01 | 1 |
| 100 | 296 | 0.01 | 1 |
| 1,000 | 1,536 | 0.01 | 1 |
| 10,000 | 13,944 | 0.01 | 1 |
| 100,000 | 138,000 | 0.01 | 1 |
| 1,000,000 | 1,378,624 | 0.01 | 1 |
| 10,000,000 | 13,784,848 | 0.01 | 1 |
| 100,000,000 | 137,847,072 | 0.01 | 1 |
| 1,000,000,000 | 1,378,469,336 | 0.01 | 1 |

### Error Rate: 0.001
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 160 | 0.001 | 1 |
| 10 | 176 | 0.001 | 1 |
| 100 | 352 | 0.001 | 1 |
| 1,000 | 2,136 | 0.001 | 1 |
| 10,000 | 19,928 | 0.001 | 1 |
| 100,000 | 197,912 | 0.001 | 1 |
| 1,000,000 | 1,977,688 | 0.001 | 1 |
| 10,000,000 | 19,775,512 | 0.001 | 1 |
| 100,000,000 | 197,753,688 | 0.001 | 1 |
| 1,000,000,000 | 1,977,535,480 | 0.001 | 1 |

### Error Rate: 0.0001
| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |
|---|---|---|---|
| 1 | 160 | 0.0001 | 1 |
| 10 | 184 | 0.0001 | 1 |
| 100 | 416 | 0.0001 | 1 |
| 1,000 | 2,736 | 0.0001 | 1 |
| 10,000 | 25,920 | 0.0001 | 1 |
| 100,000 | 257,816 | 0.0001 | 1 |
| 1,000,000 | 2,576,760 | 0.0001 | 1 |
| 10,000,000 | 25,766,168 | 0.0001 | 1 |
| 100,000,000 | 257,660,304 | 0.0001 | 1 |
| 1,000,000,000 | 2,576,601,632 | 0.0001 | 1 |