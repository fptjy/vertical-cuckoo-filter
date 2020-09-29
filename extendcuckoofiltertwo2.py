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

        # 候选桶扩展为5个
        if self.num == 5:
            yanmanumber = [0b1111111111000000, 0b0001111001111000, 0b0000001111111111, 0b1111111111111111]
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


            eviction_index = random.choice([i, a, b, c, d])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
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



        # 候选桶扩展为6个
        if self.num == 6:
            yanmanumber = [0b1111111111000000, 0b0011111111110000, 0b0000111111111100, 0b0000001111111111, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])
            e = self._get_alternate_index(i, fingerprint, yanmanumber[4])
            def number(index):
                if index == i:
                    return 5
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3
                if index == e:
                    return 4

            if self.buckets[i].insert([5, fingerprint]):
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

            elif self.buckets[e].insert([4, fingerprint]):
                self.size += 1
                return True


            eviction_index = random.choice([i, a, b, c, d, e])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                if f[0] == 5:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(eviction_index, f[1], yanmanumber[4])
                elif f[0] != 5:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(index, f[1], yanmanumber[4])

                if self.buckets[eviction_index5].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice([eviction_index1, eviction_index2, eviction_index3, eviction_index4, eviction_index5])
                item = f
            # Filter is full

            return self.size
            #raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')



        # 候选桶扩展为7个
        if self.num == 7:
            yanmanumber = [0b1111111100000000, 0b0011111111000000, 0b0000111111110000, 0b0000001111111100,
                           0b0000000011111111, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])
            e = self._get_alternate_index(i, fingerprint, yanmanumber[4])
            f = self._get_alternate_index(i, fingerprint, yanmanumber[5])

            def number(index):
                if index == i:
                    return 6
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3
                if index == e:
                    return 4
                if index == f:
                    return 5

            if self.buckets[i].insert([6, fingerprint]):
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

            elif self.buckets[e].insert([4, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[f].insert([5, fingerprint]):
                self.size += 1
                return True

            eviction_index = random.choice([i, a, b, c, d, e, f])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                if f[0] == 6:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(eviction_index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(eviction_index, f[1], yanmanumber[5])
                elif f[0] != 6:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(index, f[1], yanmanumber[5])

                if self.buckets[eviction_index6].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index5].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice(
                    [eviction_index1, eviction_index2, eviction_index3, eviction_index4, eviction_index5, eviction_index6])
                item = f
            # Filter is full

            return self.size
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')



        # 候选桶扩展为8个
        if self.num == 8:
            yanmanumber = [0b1111110000000000, 0b0011111100000000, 0b0000111111000000, 0b0000001111110000,
                           0b0000000011111100, 0b0000000000111111, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])
            e = self._get_alternate_index(i, fingerprint, yanmanumber[4])
            f = self._get_alternate_index(i, fingerprint, yanmanumber[5])
            g = self._get_alternate_index(i, fingerprint, yanmanumber[6])

            def number(index):
                if index == i:
                    return 7
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3
                if index == e:
                    return 4
                if index == f:
                    return 5
                if index == g:
                    return 6

            if self.buckets[i].insert([7, fingerprint]):
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

            elif self.buckets[e].insert([4, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[f].insert([5, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[g].insert([6, fingerprint]):
                self.size += 1
                return True

            eviction_index = random.choice([i, a, b, c, d, e, f, g])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                if f[0] == 7:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(eviction_index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(eviction_index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(eviction_index, f[1], yanmanumber[6])
                elif f[0] != 7:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(index, f[1], yanmanumber[6])

                if self.buckets[eviction_index7].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index5].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index6].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice(
                    [eviction_index1, eviction_index2, eviction_index3, eviction_index4, eviction_index5, eviction_index6, eviction_index7])
                item = f
            # Filter is full

            return self.size
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')



        # 候选桶扩展为9个
        if self.num == 9:
            yanmanumber = [0b1111000000000000, 0b0011110000000000, 0b0000111100000000, 0b0000001111000000,
                           0b0000000011110000, 0b0000000000111100, 0b0000000000001111, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])
            e = self._get_alternate_index(i, fingerprint, yanmanumber[4])
            f = self._get_alternate_index(i, fingerprint, yanmanumber[5])
            g = self._get_alternate_index(i, fingerprint, yanmanumber[6])
            h = self._get_alternate_index(i, fingerprint, yanmanumber[7])

            def number(index):
                if index == i:
                    return 8
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3
                if index == e:
                    return 4
                if index == f:
                    return 5
                if index == g:
                    return 6
                if index == h:
                    return 7

            if self.buckets[i].insert([8, fingerprint]):
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

            elif self.buckets[e].insert([4, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[f].insert([5, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[g].insert([6, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[h].insert([7, fingerprint]):
                self.size += 1
                return True

            eviction_index = random.choice([i, a, b, c, d, e, f, g, h])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                if f[0] == 8:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(eviction_index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(eviction_index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(eviction_index, f[1], yanmanumber[6])
                    eviction_index8 = self._get_alternate_index(eviction_index, f[1], yanmanumber[7])

                elif f[0] != 8:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(index, f[1], yanmanumber[6])
                    eviction_index8 = self._get_alternate_index(index, f[1], yanmanumber[7])

                if self.buckets[eviction_index8].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index5].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index6].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index7].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice(
                    [eviction_index1, eviction_index2, eviction_index3, eviction_index4, eviction_index5,
                     eviction_index6, eviction_index7, eviction_index8])
                item = f
            # Filter is full

            return self.size
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')



       # 候选桶扩展为10个
        if self.num == 10:
            yanmanumber = [0b1100000000000000, 0b0011000000000000, 0b0000110000000000, 0b0000001100000000,
                           0b0000000011000000, 0b0000000000110000, 0b0000000000001100, 0b0000000000000011, 0b1111111111111111]
            fingerprint = hashutils.fingerprint(item, self.fingerprint_size)
            i = self._get_index(item)
            a = self._get_alternate_index(i, fingerprint, yanmanumber[0])
            b = self._get_alternate_index(i, fingerprint, yanmanumber[1])
            c = self._get_alternate_index(i, fingerprint, yanmanumber[2])
            d = self._get_alternate_index(i, fingerprint, yanmanumber[3])
            e = self._get_alternate_index(i, fingerprint, yanmanumber[4])
            f = self._get_alternate_index(i, fingerprint, yanmanumber[5])
            g = self._get_alternate_index(i, fingerprint, yanmanumber[6])
            h = self._get_alternate_index(i, fingerprint, yanmanumber[7])
            j = self._get_alternate_index(i, fingerprint, yanmanumber[8])

            def number(index):
                if index == i:
                    return 9
                if index == a:
                    return 0
                if index == b:
                    return 1
                if index == c:
                    return 2
                if index == d:
                    return 3
                if index == e:
                    return 4
                if index == f:
                    return 5
                if index == g:
                    return 6
                if index == h:
                    return 7
                if index == j:
                    return 8

            if self.buckets[i].insert([9, fingerprint]):
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

            elif self.buckets[e].insert([4, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[f].insert([5, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[g].insert([6, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[h].insert([7, fingerprint]):
                self.size += 1
                return True

            elif self.buckets[j].insert([8, fingerprint]):
                self.size += 1
                return True

            eviction_index = random.choice([i, a, b, c, d, e, f, g, h, j])
            item = [number(eviction_index), fingerprint]
            for _ in range(self.max_displacements):
                f = self.buckets[eviction_index].swap(item)
                if f[0] == 9:
                    eviction_index1 = self._get_alternate_index(eviction_index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(eviction_index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(eviction_index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(eviction_index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(eviction_index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(eviction_index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(eviction_index, f[1], yanmanumber[6])
                    eviction_index8 = self._get_alternate_index(eviction_index, f[1], yanmanumber[7])
                    eviction_index9 = self._get_alternate_index(eviction_index, f[1], yanmanumber[8])

                elif f[0] != 9:
                    index = eviction_index ^ (hashutils.hash_code(f[1]) & yanmanumber[f[0]])
                    eviction_index1 = self._get_alternate_index(index, f[1], yanmanumber[0])
                    eviction_index2 = self._get_alternate_index(index, f[1], yanmanumber[1])
                    eviction_index3 = self._get_alternate_index(index, f[1], yanmanumber[2])
                    eviction_index4 = self._get_alternate_index(index, f[1], yanmanumber[3])
                    eviction_index5 = self._get_alternate_index(index, f[1], yanmanumber[4])
                    eviction_index6 = self._get_alternate_index(index, f[1], yanmanumber[5])
                    eviction_index7 = self._get_alternate_index(index, f[1], yanmanumber[6])
                    eviction_index8 = self._get_alternate_index(index, f[1], yanmanumber[7])
                    eviction_index9 = self._get_alternate_index(index, f[1], yanmanumber[8])

                if self.buckets[eviction_index9].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index1].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index2].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index3].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index4].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index5].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index6].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index7].insert(f):
                    self.size += 1
                    return True
                elif self.buckets[eviction_index8].insert(f):
                    self.size += 1
                    return True

                eviction_index = random.choice(
                    [eviction_index1, eviction_index2, eviction_index3, eviction_index4, eviction_index5,
                     eviction_index6, eviction_index7, eviction_index8, eviction_index9])
                item = f
            # Filter is full

            return self.size
            # raise exceptions.CuckooFilterFullException('Insert operation failed. '
            #                                           'Filter is full.')
