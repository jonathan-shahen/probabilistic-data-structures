import math
import mmh3

from bitarray import bitarray

class CustomQuotientFilter:
    def __init__(self, num_elements, error_rate):
        '''
        @param num_elements an estimated number of total unique elements to be inserted (i.e. 1e12)
        @param error_rate the desired false positive error rate (i.e. 1e-4)
        '''
        self.count = 0
        
    
    def count(self):
        '''
        This function the count of unique inserts into the Quotient Filter

        @return integer of the number of unique inserts that occurred 
        '''
        return self.count
    
    def exists(self, item):
        '''
        This function does have the possibility of false positives, but no false negatives.

        @param item Some object, that is hashable, to check if it was already inserted.
        @return TRUE if previously inserted (error possible); FALSE if never inserted (no error)
        '''

        pass

    def insert(self, item):
        '''
        This function inserts into the Quotient Filter

        @param item Some object, that is hashable, to insert the fingerprint into the Quotient filter.
        @return TRUE if the item hasn't already been inserted, FALSE if it was already in the filter
        '''
        pass

    def remove(self, item):
        '''
        This function removes from the Quotient Filter.

        This function has the possibility of removing an item with the same fingerprint

        @param item Some object, that is hashable, to remove the fingerprint from the Quotient filter.
        @return TRUE if the item was removed, FALSE if it wasn't found
        '''
        pass

    def merge(self, filter):
        '''
        This function merges a Quotient Filter into itself.

        @param filter the Quotient filter to merge into itself 
        @return TRUE if the filter was merged, FALSE if the filter is not mergable (not a filter or not the same hash length)
        '''
        pass

    def resize(self, newSize):
        '''
        This function resizes the Quotient Filter.

        @param newSize 
        @return TRUE if the item was removed, FALSE if it wasn't found
        '''
        pass

    
    def info(self):
        return {
            "count": self.count,
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