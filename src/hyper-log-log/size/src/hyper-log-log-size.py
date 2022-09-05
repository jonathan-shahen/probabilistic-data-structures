import os
import math

import redis

byteUnits=['B','KiB','MiB','GiB','TiB','PiB']
def bytesHuman(size,precision=2):
    unit = int(math.log(size) / math.log(1024))
    value = size * (1/1024)**(unit)
    return f'{value: >5.{precision}f}{byteUnits[unit]}'

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)

print("### HLL Size per Elements Added")
print("| Number of Items | HLL Estimate | Percent Error (%) | HLL Size (human) | HLL Size (bytes) |")
print("|---|---|---|---|---|")
for num_items in [1e1,1e2,1e3,1e4,1e5,1e6]:
    hll = f"hll_{num_items}_items"
    r.delete(hll)

    for i in range(int(num_items/10)):
        r.pfadd(hll, 10*i, 10*i + 1, 10*i + 2, 10*i + 3, 10*i + 4, 10*i + 5, 10*i + 6, 10*i + 7, 10*i + 8, 10*i + 9)

    estimate = r.pfcount(hll)
    percent_error = abs(num_items - estimate) / num_items
    # The MEMORY USAGE command reports the number of bytes that a key and its value require to be stored in RAM.
    mem_usage = r.memory_usage(hll)

    print(f"| {num_items:.1E} | {estimate:.1E} | {percent_error: >6,.1%} | {bytesHuman(mem_usage): >9} | {mem_usage:,} |")

print("You can connect to Redis and inspect the newly created HLL.")
print(f"Redis Instance: localhost:{os.environ.get('REDIS_PORT')}")