import math
import mmh3

from bitarray import bitarray

byteUnits=['B','KiB','MiB','GiB','TiB','PiB']
def bytesHuman(size,precision=2):
    unit = int(math.log(size) / math.log(1024))
    value = size * (1/1024)**(unit)
    return f'{value: >5.{precision}f}{byteUnits[unit]}'

class CustomBloomFilter:
    def __init__(self, num_elements, error_rate):
        '''
        @param num_elements an estimated number of total unique elements to be inserted (i.e. 1e12)
        @param error_rate the desired false positive error rate (i.e. 1e-4)
        '''
        # Approximate number of unique items
        self.est_count = 0
        # Prevent math errors
        if num_elements <= 1:
            num_elements = 2
        
        # shown in the math with `m`
        self.num_bits = int(
            -math.log(error_rate) * num_elements /
            math.log(2)**2
        )
        # Shown in the math with `k`
        self.num_hashes = int(
            self.num_bits * math.log(2) /
            num_elements
        )

        self.bit_array = bitarray(self.num_bits)
        self.bit_array.setall(0)
    
    def insert(self, item):
        '''
        This function inserts into the Bloom Filter

        @param item Some object, that is hashable, to insert into the bloom filter.
        @return void
        '''

        never_seen_before = False
        for i in range(self.num_hashes):
            if self.bit_array[mmh3.hash(item, i) % self.num_bits] != 1:
                never_seen_before = True
                self.bit_array[mmh3.hash(item, i) % self.num_bits] = 1

        if never_seen_before:
            self.est_count += 1
    
    def exists(self, item):
        '''
        This function does have the possibility of false positives, but no false negatives.

        @param item Some object, that is hashable, to check if it was already inserted.
        @return TRUE if previously inserted (error possible); FALSE if never inserted (no error)
        '''

        for i in range(self.num_hashes):
            if self.bit_array[mmh3.hash(item, i) % self.num_bits] == 0:
                return False

        return True
    
    def info(self):
        return {
            "num_bits": self.num_bits,
            "num_bytes": math.ceil(self.num_bits/8),
            "num_hashes": self.num_hashes,
            "est_count": self.est_count,
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
        print("| Number of Items | Bloom Filter Size (human) | Bloom Filter Size (bytes) | Error Rate | Number of Filters |")
        print("|---|---|---|---|---|")
        for size in required_sizes:
            filter = CustomBloomFilter(size, error_rate)
            info = filter.info()
            print(f"| {size:,} | {bytesHuman(info['num_bytes'])} | {info['num_bytes']:,} | {error_rate} | {info['num_hashes']} |")
            del filter
        print("")