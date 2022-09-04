import os
import math

import redis

byteUnits=['B','KiB','MiB','GiB','TiB','PiB']
def bytesHuman(size,precision=2):
    unit = int(math.log(size) / math.log(1024))
    value = size * (1/1024)**(unit)
    return f'{value: >5.{precision}f}{byteUnits[unit]}'

num_counters = [
    1, 10, 100, 1_000, 10_000, 100_000,
    1_000_000, 10_000_000, 100_000_000,
    1_000_000_000
]

num_hashes = [
    1,2,3,5,10,15
]

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)

# From redis docs: https://redis.io/commands/bf.reserve/
# The number of hash functions is -log(error)/ln(2)^2.
# The number of bits per item is -log(error)/ln(2) ≈ 1.44.

for num_hash in num_hashes:
    print(f"### Number Hashes: {num_hash}")
    print("| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |")
    print("|---|---|---|---|")
    for num_counter in num_counters:
        count_min_sketch = f"count_min_sketch_{num_counter}_{num_hash}"
        # print(f"Creating Count Min Sketch {count_min_sketch}")
        r.delete(count_min_sketch)
        filter = r.cms().initbydim(count_min_sketch, num_counter, num_hash)

        # The MEMORY USAGE command reports the number of bytes that a key and its value require to be stored in RAM.
        mem_usage = r.memory_usage(count_min_sketch)

        print(f"| {num_hash} | {num_counter:,} | {bytesHuman(mem_usage)} | {mem_usage:,} |")
    print("")
print("")
print("You can connect to Redis and inspect the newly created Count Min Sketch.")
print(f"Redis Instance: localhost:{os.environ.get('REDIS_PORT')}")