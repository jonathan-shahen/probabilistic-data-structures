# Bloom Filters

## Overview

Bloom filters are a probabilistic data structure that simulates a Hash Table but only for the features:
Insert/Add (add a potentially new item) and Exists (check if the item exits).
This data structure is useful as an intermediate data store to direct more expensive operations.
Commonly a bloom filter is stored in RAM and directs expensive information retrievals to the correct location
(most of the time).
Bloom filters have one sided error, with false positives occurring.
Bloom filters can be tweaked to decrease the probability of error by increasing the number of bits utilized for storage.

## Quick Features

* Operations: INSERT, EXISTS, COUNT
* False Positives: Yes
* False Negatives: No