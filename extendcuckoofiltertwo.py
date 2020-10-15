"""
extend-Cuckoo Filter
"""

import random

import bucket # 相对导入from . import bucket这种导入方式会报错
import exceptions
import hashutils


class extendCuckooFilter(object):
    """
    Cuckoo Filter class.

    Implements insert, delete and contains operations for the filter.
    """

    def __init__(self, capacity, bucket_size=4, fingerprint_size=1,
                 max_displacements=1000):
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

    def __repr__(self):        # 重写__repr__()，定义打印class的信息
        return '<CuckooFilter: capacity=' + str(self.capacity) + \
               ', size=' + str(self.size) + ', fingerprint size=' + \
               str(self.fingerprint_size) + ' byte(s)>'

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return self.contains(item)

    def _get_index(self, item):
        index = hashutils.hash_code(item) % self.capacity
        return index

    def _get_alternate1_index(self, index, fingerprint):
        alt_index1 = (index ^ (hashutils.hash_code(fingerprint) & 0b00001111)) % self.capacity
        return alt_index1

    def _get_alternate2_index(self, index, fingerprint):
        alt_index2 = (index ^ (hashutils.hash_code(fingerprint) & 0b11110000)) % self.capacity
        return alt_index2

    def _get_alternate3_index(self, index, fingerprint):
        alt_index3 = (index ^ hashutils.hash_code(fingerprint)) % self.capacity
        return alt_index3

    def insert1(self, item):
        """
        Insert an item into the filter.

        :param item: Item to be inserted.
        :return: True if insert is successful; CuckooFilterFullException if
        filter is full.
        """
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        i = self._get_index(item)
        j = self._get_alternate3_index(i, fingerprint)

        if self.buckets[i].insert(fingerprint) \
                or self.buckets[j].insert(fingerprint):
            self.size += 1
            return True

        eviction_index = random.choice([i, j])
        for _ in range(self.max_displacements):
            f = self.buckets[eviction_index].swap(fingerprint)
            eviction_index = self._get_alternate3_index(eviction_index, f)
            if self.buckets[eviction_index].insert(f):
                self.size += 1
                return True
            fingerprint = f    # 我自己感觉fingerprint没有改变，有问题，然后我加上了这行代码
        # Filter is full
        return self.size

        #raise exceptions.CuckooFilterFullException('Insert operation failed. '
        #                                           'Filter is full.')


    def insert2(self, item):
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
        return self.size
        #raise exceptions.CuckooFilterFullException('Insert operation failed. '
        #                                           'Filter is full.')


    def contains(self, item):
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
        elif fingerprint in self.buckets[x]:
            return True
        elif fingerprint in self.buckets[j]:
            return True
        else:
            return False

    def delete(self, item):
        """
        Delete an item from the filter.

        To delete an item safely, it must have been previously inserted.
        Otherwise, deleting a non-inserted item might unintentionally remove
        a real, different item that happens to share the same fingerprint.

        :param item: Item to delete from the filter.
        :return: True, if item is found and deleted; False, otherwise.
        """
        fingerprint = hashutils.fingerprint(item, size=self.fingerprint_size)
        i = self._get_index(item)
        j = self._get_alternate1_index(i, fingerprint)
        x = self._get_alternate2_index(i, fingerprint)
        y = self._get_alternate3_index(i, fingerprint)

        if self.buckets[i].delete(fingerprint):
            self.size -= 1
            return True
        elif self.buckets[j].delete(fingerprint):
            self.size -= 1
            return True
        elif self.buckets[x].delete(fingerprint):
            self.size -= 1
            return True
        elif self.buckets[y].delete(fingerprint):
            self.size -= 1
            return True
        else:
            return False



