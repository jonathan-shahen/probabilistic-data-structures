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
    print("| Number of Items | Bloom Filter Size (bytes) | Docs Filter Size (bytes) | Memory Usage (bytes) | Error Rate | Number of Filters |")
    print("|---|---|---|---|---|---|")
    for size in required_sizes:
        bloom_name = f"bloom_{size}_{error_rate}"
        # print(f"Creating Bloom Filter: {bloom_name}")
        r.delete(bloom_name)
        filter = r.bf().create(bloom_name, error_rate, size, noScale=True)
        info = r.bf().info(bloom_name)

        # The MEMORY USAGE command reports the number of bytes that a key and its value require to be stored in RAM.
        mem_usage = r.memory_usage(bloom_name)

        # This comes from a comment and thus might not be accurate
        num_bits_per_item = -math.log10(error_rate)/math.log(2)
        num_bits = int(size * num_bits_per_item)
        num_hashes = int(-math.log10(error_rate)/math.log(2)**2)

        print(f"| {size:,} | {info.size:,} | {math.ceil(num_bits/8):,} | {mem_usage:,} | {error_rate} | {num_hashes} |")
    print("")
print("")
print("You can connect to Redis and inspect the newly created bloom filters.")
print(f"Redis Instance: localhost:{os.environ.get('REDIS_PORT')}")