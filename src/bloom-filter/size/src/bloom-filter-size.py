import redis
import os

required_sizes = [
    1, 10, 100, 1_000, 10_000, 100_000,
    1_000_000, 10_000_000, 100_000_000,
    1_000_000_000
]

error_rates = [
    0.01, 0.001, 0.0001
]

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)

for error_rate in error_rates:
    print(f"### Error Rate: {error_rate}")
    print("| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |")
    print("|---|---|---|---|")
    for size in required_sizes:
        bloom_name = f"bloom_{size}_{error_rate}"
        # print(f"Creating Bloom Filter: {bloom_name}")
        filter = r.bf().create(bloom_name, error_rate, size)
        info = r.bf().info(bloom_name)
        print(f"| {size:,} | {info.size:,} | {error_rate} | {info.filterNum} |")
    print("")