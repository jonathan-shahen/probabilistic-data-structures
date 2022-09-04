# Count Min Sketch

## Overview


## Quick Features

* Operations: INSERT, GET, EXISTS, DELETE, RESIZE, MERGE, COUNT, ITERATE
* False Positives: Yes
* False Negatives: No

## Operations

* **INSERT**: Insert an item into the quotient filter, this utilizes fingerprinting (hashing) and does not actually
    store the original item
* **GET**: Able to reconstruct the full fingerprint (hash of the item) given an slot
* **EXISTS**: Check if an item was previously inserted.
* **DELETE**: Able to remove previously inserted remainders 
* **RESIZE**: TODO
* **MERGE**: Merge 2 or more Quotient Filters