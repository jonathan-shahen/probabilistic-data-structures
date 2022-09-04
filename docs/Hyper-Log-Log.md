# Hyper Log Log (HLL)

## Overview



## Quick Features

* Operations: INSERT, COUNT, UNION
* Error Rate: The cardinality can be off from the true cardinality

## Operations

* **INSERT**: Insert an item into the HLL, only keeps track 
* **COUNT**: Able to estimate the cardinality (count of unique elements) stored in the HLL
* **UNION/MERGE**: The union of 2 or more HLLs. Able to to estimate cardinality without double counting between `sets`.