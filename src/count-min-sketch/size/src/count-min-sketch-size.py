import os
import math

import redis

required_sizes = [
    1, 10, 100, 1_000, 10_000, 100_000,
    1_000_000, 10_000_000, 100_000_000,
    1_000_000_000
]

error_rates = [
    1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9
]

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)

# From redis docs: https://redis.io/commands/bf.reserve/
# The number of hash functions is -log(error)/ln(2)^2.
# The number of bits per item is -log(error)/ln(2) ≈ 1.44.

for error_rate in error_rates:
    print(f"### Error Rate: {error_rate}")
    print("| Number of Items | Count Min Sketch Size (bytes) | Memory Usage (bytes) | Error Rate |")
    print("|---|---|---|---|---|")
    for size in required_sizes:
        count_min_sketch = f"count_min_sketch_{size}_{error_rate}"
        # print(f"Creating Count Min Sketch {count_min_sketch}")
        r.delete(count_min_sketch)
        filter = r.bf().create(count_min_sketch, error_rate, size, noScale=True)
        info = r.bf().info(count_min_sketch)

        # The MEMORY USAGE command reports the number of bytes that a key and its value require to be stored in RAM.
        mem_usage = r.memory_usage(count_min_sketch)

        print(f"| {size:,} | {info.size:,} | {mem_usage:,} | {error_rate} |")
    print("")
print("")
print("You can connect to Redis and inspect the newly created Count Min Sketch.")
print(f"Redis Instance: localhost:{os.environ.get('REDIS_PORT')}")