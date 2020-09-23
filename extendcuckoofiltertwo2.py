"""
extend-Cuckoo Filter
"""

import random

import bucket2      # 相对导入from . import bucket这种导入方式会报错
import exceptions
import hashutils

class extendCuckooFilter(object):
    """
    Cuckoo Filter class.

    Implements insert, delete and contains operations for the filter.
    """

    def __init__(self, capacity, num, bucket_size=4, fingerprint_size=2,
                 max_displacements=500):
        """
        Initialize CuckooFilter object.

        :param capacity: Size of the Cuckoo Filter
        :param bucket_size: Number of entries in a bucket
        :param fingerprint_size: Fingerprint size in bytes
        :param max_displacements: Maximum number of evictions before filter is
        considered full
        """
        self.capacity = capacity
        self.num = num
        self.bucket_size = bucket_size
        self.fingerprint_size = fingerprint_size
        self.max_displacements = max_displacements
        self.buckets = [bucket2.Bucket(size=bucket_size)
                        for _ in range(self.capacity)]
        self.size = 0

    def __repr__(self):        # 重写__repr__()，定义打印class的信息
        return '<CuckooFilter: capacity=' + str(self.capacity) + \
               ', size=' + str(self.size) + ', fingerprint size=' + \
               str(self.fingerprint_size) + ' byte(s)>'

    def __len__(self):
        return self.size

  #  def __contains__(self, item):
   #     return self.contains(item)

    def _get_index(self, item):
        index = hashutils.hash_code(item) % self.capacity
        return index

    def _get_alternate_index(self, index, fingerprint, yanmanumber):
        alt_index2 = (index ^ (hashutils.hash_code(fingerprint) & yanmanumber)) % self.capacity
        return alt_index2

    def insert(self, item):
        """
        0000 0000 0000 0000
        Insert an item into the filter.

        :param item: Item to be inserted.
                number: serial number of buckets corresponding item
        :return: True if insert is successful; CuckooFilterFullException if
        filter is full.
        """
        if self.num == 5:
            yanmanumber = [0b1111111111000000, 0b00011111111000, 0b0000001111111111, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])

            def number(index):
                if index == i:
                    return 4
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3

            if self.buckets[i].insert([4, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[a].insert([0, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[b].insert([1, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[c].insert([2, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[d].insert([3, fingerprint]):
                self.size += 1
                return True

            zz = self.buckets[i]
            z1 = self.buckets[a]
            z2 = self.buckets[b]
            z3 = self.buckets[c]
            z4 = self.buckets[d]
            z5 = type(self.buckets[d])
            z6 = type(self.buckets[d].bucket)
            z7 = type(self.buckets[d].bucket[2])

            eviction_index = random.choice([i, a, b, c, d])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                zzz = number(eviction_index)
                if f[0] == 4:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                elif f[0] != 4:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])

                if self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice([eviction_index1, eviction_index2, eviction_index3, eviction_index4])
                item = f
            # Filter is full

            return self.size
            #raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')




