import math
import numpy as np
import mmh3


class CustomCountMinSketchFilter:
    def __init__(self, num_counters, num_hashes):
        '''
        @param num_counters The number of counters/columns for each row/hash
        @param num_hashes the number of hashes/rows
        '''
        # The number of counters/columns for each row/hash
        self.num_counters = num_counters
        # the number of hashes/rows
        self.num_hashes = num_hashes

        self.count_array = np.zeros(shape=(num_hashes,num_counters), dtype=np.int32)
    
    def update(self, item, count):
        '''
        This function inserts into the Bloom Filter

        @param item Some object, that is hashable, to increase the frequency.
        @param count the amount to increase the frequency by.
        @return void
        '''

        for i in range(self.num_hashes):
            self.counter_array[mmh3.hash(item, i) % self.num_counters] += count
    
    def estimate(self, item):
        '''
        This function does have the possibility of over estimates, but no under estimates.

        @param item Some object, that is hashable, to check if it was already inserted.
        @return the estimated frequency for `item`
        '''

        min_val = self.counter_array[mmh3.hash(item, 0) % self.num_counters]
        for i in range(1,self.num_hashes):
            if self.counter_array[mmh3.hash(item, i) % self.num_counters] < min_val:
                min_val = self.counter_array[mmh3.hash(item, i) % self.num_counters]

        return min_val
    
    def info(self):
        return {
            # 4 bytes per int32 * 2d array
            "num_bytes": 4 * self.num_counters * self.num_hashes,
            "num_counters": self.num_counters,
            "num_hashes": self.num_hashes,
        }

if __name__ == "__main__":
    required_sizes = [
        1, 10, 100, 1_000, 10_000, 100_000,
        1_000_000, 10_000_000, 100_000_000,
        1_000_000_000
    ]

    error_rates = [
        1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9
    ]

    for error_rate in error_rates:
        print(f"### Error Rate: {error_rate}")
        print("| Number of Items | Bloom Filter Size (bytes) | Error Rate | Number of Filters |")
        print("|---|---|---|---|")
        for size in required_sizes:
            filter = CustomBloomFilter(size, error_rate)
            info = filter.info()
            print(f"| {size:,} | {info['num_bytes']:,} | {error_rate} | {info['num_hashes']} |")
            del filter
        print("")