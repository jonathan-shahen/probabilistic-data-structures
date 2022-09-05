# Hyper Log Log: Size

## Description

This repo shows how much storage is required for creating a REDIS Hyper Log Log.

## Setup

1. Requires Docker and Docker Compose
1. Open a terminal and `cd` into this directory
1. `docker compose up`
    * If this fails, then change the port in `.env`
1. `docker composer logs bloom_filter_size`
    * This will display the logs from the python container


## Results

### HLL Size per Elements Added
| Number of Items | HLL Estimate | Percent Error (%) | HLL Size (human) | HLL Size (bytes) |
|---|---|---|---|---|
| 1.0E+01 | 1.0E+01 |   0.0% |   152.00B |    152 |
| 1.0E+02 | 1.0E+02 |   0.0% |   576.00B |    576 |
| 1.0E+03 | 1.0E+03 |   0.1% |   2.06KiB |  2,112 |
| 1.0E+04 | 1.0E+04 |   0.1% |  14.06KiB | 14,400 |
| 1.0E+05 | 1.0E+05 |   0.4% |  14.06KiB | 14,400 |
| 1.0E+06 | 1.0E+06 |   1.0% |  14.06KiB | 14,400 |

