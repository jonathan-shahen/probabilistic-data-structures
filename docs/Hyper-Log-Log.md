# Hyper Log Log (HLL)

## Overview

Hyper Log Log (HLL) is a probabilistic algorithm/data-structure for estimating the number of unique elements in a set
(cardinality). HLL's utilize statistics to come up with their estimates and assumes that the values being inserted
are from a random distribution, this means that the bits of an element have the same probability of being selected.
For normal data streams, utilizing the raw item will likely break this assumption, thus HLL's utilize hashing to come up
with a random value (hash functions are not random functions, but they can appear random).

HLLs work for situations where storing a linear list is impractical.
HLLs store the largest number of trailing zeros for a number, to increase the accuracy of the measurement HLLs have
multiple buckets, where each bucket stores the maximum number of trailing zeros seen within that bucket, and the leading
bits are used to find which bucket a hash should be compared to.
Estimates are made by taking the harmonic average of the number of trailing bits from each bucket; depending on the
harmonic average, there are multiple methods to to convert this to an estimate (these method are shown to empirically
improve the estimate).


**NOTE**: HLL estimates get more accurate with more inserts. HLLs have corrections for small, medium, large ranges.
But for space efficiency, it might be better to store the raw inserts linearly until the storage requirements increase
to the range of an HLL. Redis utilizes a 14400 bytes HLL (it dynamically grows with data), which can store 1800 hashes
(64 bits long).


## Quick Features

* Operations: INSERT, COUNT, UNION
* Error Rate: The cardinality can be off from the true cardinality

## Operations

* **INSERT**: Insert an item into the HLL, only keeps track 
* **COUNT**: Able to estimate the cardinality (count of unique elements) stored in the HLL
* **UNION/MERGE**: The union of 2 or more HLLs. Able to to estimate cardinality without double counting between `sets`.