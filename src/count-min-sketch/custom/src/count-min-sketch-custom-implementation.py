import math
import os
import numpy as np
import mmh3
import random

byteUnits=['B','KiB','MiB','GiB','TiB','PiB']
def bytesHuman(size,precision=2):
    unit = int(math.log(size) / math.log(1024))
    value = size * (1/1024)**(unit)
    return f'{value: >5.{precision}f}{byteUnits[unit]}'

def calcCountersHashes(overEstimationError, failureProbability):
    '''
    This function returns the number of counters and number of hashes calculated to satisfy the parameters

    @param overEstimationError small value that limits the maximum overestimation (epsilon * Sum_All_Frequencies)
    @param failureProbability small value to reduce the probability of an overestimation exceeding epsilon * Sum_All_Frequencies
    '''
    return {
        "num_counters": int(math.ceil(math.e / overEstimationError)),
        "num_hashes": int(math.ceil(math.log( 1 / failureProbability))),
    }

class CustomCountMinSketch:
    def __init__(self, num_counters, num_hashes):
        '''
        @param num_counters The number of counters/columns for each row/hash (`width`)
        @param num_hashes the number of hashes/rows (`depth`)
        '''
        # The number of counters/columns for each row/hash
        self.num_counters = num_counters
        # the number of hashes/rows
        self.num_hashes = num_hashes

        self.counter_array = np.zeros(shape=(num_hashes,num_counters), dtype=np.uint32)
    
    def update(self, item, count):
        '''
        This function inserts into the Bloom Filter

        @param item Some object, that is hashable, to increase the frequency.
        @param count the amount to increase the frequency by.
        @return void
        '''

        for i in range(self.num_hashes):
            self.counter_array[i][mmh3.hash(item, i) % self.num_counters] += count
    
    def estimate(self, item):
        '''
        This function does have the possibility of over estimates, but no under estimates.

        @param item Some object, that is hashable, to check if it was already inserted.
        @return the estimated frequency for `item`
        '''

        min_val = self.counter_array[0][mmh3.hash(item, 0) % self.num_counters]
        for i in range(1,self.num_hashes):
            tmp = self.counter_array[i][mmh3.hash(item, i) % self.num_counters]
            if tmp < min_val:
                min_val = tmp

        return min_val
    
    def info(self):
        return {
            # 4 bytes per int32 * 2d array
            "num_bytes": self.counter_array.itemsize * self.counter_array.size,
            "num_counters": self.num_counters,
            "num_hashes": self.num_hashes,
        }


def testCustomCountMinSketch():
    for counters in [2,3,4,100]:
        for hashes in [1,2]:
            print(f'CMS(counters={counters}, hashes={hashes})')
            cms = CustomCountMinSketch(counters,hashes)

            frequencies = [0] * 11
            for i in range(100):
                cms.update('0', 1)
                frequencies[0] += 1
            
            total_random_values = 10_000
            for _ in range(total_random_values):
                index = random.randint(1,10)
                cms.update(f'{index}', 1)
                frequencies[index] += 1

            total = 0
            true_total = 0
            for i in range(0,11):
                tmp = cms.estimate(str(i))
                total += tmp
                true_total += frequencies[i]
                print(f'Estimate Frequency {i: >2}: {tmp:,} (True Value: {frequencies[i]:,}; Diff: {tmp - frequencies[i]:,})')

            print(f'Total frequencies (1-10) should equal: {true_total:,}')
            print(f'Total frequencies (1-10) in CMS equal: {total:,}')
            print(f'Total frequencies (1-10) difference  : {total - true_total:,}')
            print('')
            del cms


if __name__ == "__main__":

    if os.environ.get('RUN_TEST', '0') == '1':
        testCustomCountMinSketch()

    num_counters = [
        1, 10, 100, 1_000, 10_000, 100_000,
        1_000_000, 10_000_000, 100_000_000,
        1_000_000_000
    ]

    num_hashes = [
        1,2,3,5,10,15
    ]
    for num_hash in num_hashes:
        print(f"### Number Hashes: {num_hash}")
        print("| Number of Hashes | Number of Counters | Memory Usage (human)| Memory Usage (bytes) |")
        print("|---|---|---|---|")
        for num_counter in num_counters:
            cms = CustomCountMinSketch(num_counter, num_hash)
            info = cms.info()
            print(f"| {num_hash} | {num_counter:,} | {bytesHuman(info['num_bytes'])} | {info['num_bytes']:,} |")
            del cms
        print("")