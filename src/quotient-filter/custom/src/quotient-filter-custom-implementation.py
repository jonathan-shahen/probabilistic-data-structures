import math
import mmh3

from bitarray import bitarray

class CustomQuotientFilter:
    def __init__(self, num_elements, error_rate):
        '''
        @param num_elements an estimated number of total unique elements to be inserted (i.e. 1e12)
        @param error_rate the desired false positive error rate (i.e. 1e-4)
        '''
        pass
        
    
    def insert(self, item):
        '''
        This function inserts into the Bloom Filter

        @param item Some object, that is hashable, to insert into the bloom filter.
        @return void
        '''
        pass

    
    def exists(self, item):
        '''
        This function does have the possibility of false positives, but no false negatives.

        @param item Some object, that is hashable, to check if it was already inserted.
        @return TRUE if previously inserted (error possible); FALSE if never inserted (no error)
        '''

        pass
    
    def info(self):
        return {
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
            filter = CustomQuotientFilter(size, error_rate)
            info = filter.info()
            print(f"| {size:,} | {info['num_bytes']:,} | {error_rate} | {info['num_hashes']} |")
            del filter
        print("")