"""
extend-Cuckoo Filter
"""

import random

import bucket # 相对导入from . import bucket这种导入方式会报错
import exceptions
import hashutils


class VCuckooFilter14_2(object):
    """
    Cuckoo Filter class.

    Implements insert, delete and contains operations for the filter.
    """

    def __init__(self, capacity, bucket_size=4, fingerprint_size=14,
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
        self.bucket_size = bucket_size
        self.fingerprint_size = fingerprint_size
        self.max_displacements = max_displacements
        self.buckets = [bucket.Bucket(size=bucket_size)
                        for _ in range(self.capacity)]
        self.size = 0
        self.kicks = 0  #自己写的，用来获取踢出重放次数

    def __repr__(self):        # 重写__repr__()，定义打印class的信息
        return '<CuckooFilter: capacity=' + str(self.capacity) + \
               ', size=' + str(self.size) + ', fingerprint size=' + \
               str(self.fingerprint_size) + ' byte(s)>'

    def __len__(self):
        return self.size

    #def __contains__(self, item):
     #   return self.contains(item)

    def _get_index(self, item):
        index = hashutils.hash_code(item) % self.capacity
        return index

    def _get_alternate1_index(self, index, fingerprint):
        alt_index1 = (index ^ (hashutils.hash_code(fingerprint) & 0b11111111111100)) % self.capacity
        return alt_index1

    def _get_alternate2_index(self, index, fingerprint):
        alt_index2 = (index ^ (hashutils.hash_code(fingerprint) & 0b00000000000011)) % self.capacity
        return alt_index2

    def _get_alternate3_index(self, index, fingerprint):
        alt_index3 = (index ^ hashutils.hash_code(fingerprint)) % self.capacity
        return alt_index3


    def I_insert2(self, item):
        """
        Insert an item into the filter.

        :param item: Item to be inserted.
        :return: True if insert is successful; CuckooFilterFullException if
        filter is full.
        """
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        i = self._get_index(item)
        j = self._get_alternate1_index(i, fingerprint)
        x = self._get_alternate2_index(i, fingerprint)
        y = self._get_alternate3_index(i, fingerprint)

        if i == j or x:     # 候选桶扩展失败
            if self.buckets[i].insert(fingerprint) \
                    or self.buckets[y].insert(fingerprint):
                self.size += 1
                return True

        if i != j or x:  # 候选桶扩展成功
            if self.buckets[i].insert(fingerprint):
                self.size += 1
                return True
            elif self.buckets[y].insert(fingerprint):
                self.size += 1
                return True
            elif self.buckets[j].insert(fingerprint):
                self.size += 1
                return True
            elif self.buckets[x].insert(fingerprint):
                self.size += 1
                return True

        eviction_index = random.choice([i, j, x, y])
        for _ in range(self.max_displacements):
            self.kicks += 1
            f = self.buckets[eviction_index].swap(fingerprint)
            eviction_index1 = self._get_alternate1_index(eviction_index, f)
            eviction_index2 = self._get_alternate2_index(eviction_index, f)
            eviction_index3 = self._get_alternate3_index(eviction_index, f)

            if eviction_index == eviction_index2 or eviction_index1:  # 扩展候选桶失败
                if self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                eviction_index = eviction_index3

            if eviction_index != eviction_index2 or eviction_index1:  # 扩展候选桶成功
                if self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                eviction_index = random.choice([eviction_index1, eviction_index2, eviction_index3])

            fingerprint = f  # 源码有问题，这一条代码还是得加上，不然导致重复插入初始的fingerprint，查询时会有问题
        # Filter is full
        return self.size, self.kicks
        #raise exceptions.CuckooFilterFullException('Insert operation failed. '
        #                                           'Filter is full.')


    def I_contains2(self, item):
        """
        Check if the filter contains the item.

        :param item: Item to check its presence in the filter.
        :return: True, if item is in the filter; False, otherwise.
        """
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        i = self._get_index(item)
        j = self._get_alternate1_index(i, fingerprint)
        x = self._get_alternate2_index(i, fingerprint)
        y = self._get_alternate3_index(i, fingerprint)

        if fingerprint in self.buckets[i]:
            return True
        elif fingerprint in self.buckets[y]:
            return True
        elif fingerprint in self.buckets[j]:
            return True
        elif fingerprint in self.buckets[x]:
            return True
        else:
            return False

