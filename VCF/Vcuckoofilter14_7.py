"""
extend-Cuckoo Filter
"""

import random

import bucket # 相对导入from . import bucket这种导入方式会报错
import exceptions
import hashutils


class VCuckooFilter14_7(object):
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

    # def _get_alternate1_index(self, index, fingerprint):
    #     alt_index1 = (index ^ (hashutils.hash_code(fingerprint) & 0b00000001111111)) % self.capacity
    #     return alt_index1
    #
    # def _get_alternate2_index(self, index, fingerprint):
    #     alt_index2 = (index ^ (hashutils.hash_code(fingerprint) & 0b11111110000000)) % self.capacity
    #     return alt_index2

    def _get_alternate1_index(self, index, fingerprint):
        alt_index1 = (index ^ (hashutils.hash_code(fingerprint) & 0b01010101010101)) % self.capacity
        return alt_index1

    def _get_alternate2_index(self, index, fingerprint):
        alt_index2 = (index ^ (hashutils.hash_code(fingerprint) & 0b10101010101010)) % self.capacity
        return alt_index2

    def _get_alternate3_index(self, index, fingerprint):
        alt_index3 = (index ^ hashutils.hash_code(fingerprint)) % self.capacity
        return alt_index3

    def I_insert0(self, item):
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
            self.kicks += 1
            f = self.buckets[eviction_index].swap(fingerprint)
            eviction_index = self._get_alternate3_index(eviction_index, f)
            if self.buckets[eviction_index].insert(f):
                self.size += 1
                return True
            fingerprint = f    # 我自己感觉fingerprint没有改变，有问题，然后我加上了这行代码
        # Filter is full
        return self.size, self.kicks

        # raise exceptions.CuckooFilterFullException('Insert operation failed. '
        #                                            'Filter is full.')


    def I_insert7(self, item):
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


    def D_insert(self, item, threshold1, threshold2):
        """
        Insert an item into the filter.

        :param item: Item to be inserted.
        :return: True if insert is successful; CuckooFilterFullException if
        filter is full.
        """
        # 处于阈值区间则采用4个候选桶进行存储,注意：threshold1不能小于255，threshold2不能大于65280
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        if fingerprint >= threshold1 and fingerprint <= threshold2:
            i = self._get_index(item)
            j = self._get_alternate1_index(i, fingerprint)
            x = self._get_alternate2_index(i, fingerprint)
            y = self._get_alternate3_index(i, fingerprint)

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

                # 若交换得到的指纹值位于阈值区间，则4个桶
                if f >= threshold1 and f <= threshold2:
                    eviction_index1 = self._get_alternate1_index(eviction_index, f)
                    eviction_index2 = self._get_alternate2_index(eviction_index, f)
                    eviction_index3 = self._get_alternate3_index(eviction_index, f)

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
                    fingerprint = f

                else:
                    eviction_index = self._get_alternate3_index(eviction_index, f)
                    if self.buckets[eviction_index].insert(f):
                        self.size += 1
                        return True
                    fingerprint = f

            # Filter is full
            return self.size, self.kicks
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')

        # 否则采用2个候选桶存储
        else:
            i = self._get_index(item)
            j = self._get_alternate3_index(i, fingerprint)

            if self.buckets[i].insert(fingerprint) \
                    or self.buckets[j].insert(fingerprint):
                self.size += 1
                return True

            eviction_index = random.choice([i, j])
            for _ in range(self.max_displacements):
                self.kicks += 1
                f = self.buckets[eviction_index].swap(fingerprint)
                # 如果交换的指纹值位于阈值区间，则扩展到4个桶
                if f >= threshold1 and f <= threshold2:
                    eviction_index1 = self._get_alternate1_index(eviction_index, f)
                    eviction_index2 = self._get_alternate2_index(eviction_index, f)
                    eviction_index3 = self._get_alternate3_index(eviction_index, f)

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
                    fingerprint = f

                # 否则，还是两个桶
                else:
                    eviction_index = self._get_alternate3_index(eviction_index, f)
                    if self.buckets[eviction_index].insert(f):
                        self.size += 1
                        return True
                    fingerprint = f

            # Filter is full
            return self.size, self.kicks
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')


    def I_contains0(self, item):
        """
        Check if the filter contains the item.

        :param item: Item to check its presence in the filter.
        :return: True, if item is in the filter; False, otherwise.
        """
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        i = self._get_index(item)
        j = self._get_alternate3_index(i, fingerprint)

        return fingerprint in self.buckets[i] or fingerprint in self.buckets[j]


    def I_contains7(self, item):
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

    def D_contains(self, item, threshold1, threshold2):
        """
        Check if the filter contains the item.

        :param item: Item to check its presence in the filter.
        :return: True, if item is in the filter; False, otherwise.
        """
        fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
        if fingerprint >= threshold1 and fingerprint <= threshold2:
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

        else:
            i = self._get_index(item)
            j = self._get_alternate3_index(i, fingerprint)

            return fingerprint in self.buckets[i] or fingerprint in self.buckets[j]


    def delete1(self, item):
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
        j = self._get_alternate3_index(i, fingerprint)
        if self.buckets[i].delete(fingerprint) \
                or self.buckets[j].delete(fingerprint):
            self.size -= 1
            return True
        return False

    def delete2(self, item):
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
            return True
        elif self.buckets[y].delete(fingerprint):
            return True
        elif self.buckets[j].delete(fingerprint):
            return True
        elif self.buckets[x].delete(fingerprint):
            return True
        else:
            return False

