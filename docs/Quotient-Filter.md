# Quotient Filters

## Overview

A Quotient Filter is a probabilistic data structure that is used for Approximate Membership Queries (AMQ).
It is able to `insert` items into the data structure, and then check to see if an item has been inserted.
These types of queries are very useful for large distributed operations that can be expensive.
A quotient filter is usually stored in RAM and provides a POTENTIALLY or NO response as to if a resource
(identified by some key) is stored on a distributed resource.
This saves time as we don't need to go to each distributed resource and ask if the item is there.
We know make 1 request to the first resource where the quotient filter says POTENTIALLY.
If we have a low error rate, than that is a our only request, but some times we can be forced to make multiple requests.

Quotient filters are similar to Bloom Filters, but provide more features at the expense of more storage.
Added features include: Delete, Resize, Merge, Iterate/Get.

**Delete** is the ability to remove an item/fingerprint from the quotient filter.
This is a very important feature for dynamic systems; our example above works better with quotient filters since we are
able to remove assets from one distributed resource to another and not have to rebuild the filter.

**Resize** is the ability to create a new quotient filter (bigger or smaller) since we can reconstruct all fingerprints
(hashes) that were inserted. Since we are utilizing the number of initial bits as the bucket number, and this has to be
a whole value, thus increasing or decreasing the filter is by factors of 2 (2x bigger, 16x smaller, etc)

**Merge**  is the ability to merge a Quotient Filter, with the same fingerprinting function (hash), into itself.
This operation is very similar to resizing, but instead of inserting into the blank quotient filter, you insert into
the target filter.

**Iterate/Get** is the ability to traverse the filter and retrieve all fingerprints that were inserted into it.
The Get operation just retrieves the set of fingerprints associated with a single slot.

### Handling Hash Collisions 

Quotient Filters use only a fixed number of bits of the finger print for the slot in the storage table
(where the remainder is stored), thus we should consider the possibility of hash collisions with the reduced key space.
Quotient filters utilize a modified version of linear probing; the modification add meta bits (3 bits) to allow for
reconstruction of full fingerprint even when the remainder has been shifted down.
Exponential probing would be inefficient due to the number of bytes needed to go backwards for the reconstruction step.

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