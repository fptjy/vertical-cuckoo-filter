import random


class Bucket(object):

    def __init__(self, size=4):
        self.size = size
        self.bucket = [-1 for i in range(size)]

    def __repr__(self):
        return '<Bucket: ' + str(self.bucket) + '>'

    def __contains__(self, item):
        return item in self.bucket

    def __len__(self):
        return len(self.bucket)

    def insert(self, item):
        """
        Insert a fingerprint into the bucket
        :param item:
        :return:
        """
        if self.is_not_full():
            self.bucket[self.bucket.index(-1)] = item
            return True
        return False

    def delete(self, item):
        """
        Delete a fingerprint from the bucket.
        :param item:
        :return:
        """
        try:
            self.bucket[self.bucket.index(item)] = -1
            return True
        except ValueError:
            return False

    def is_not_full(self):
        return -1 in self.bucket

    def swap(self, item):
        """
        Swap fingerprint with a random entry stored in the bucket and return
        the swapped fingerprint
        :param item:
        :return:
        """
        index = random.choice(range(len(self.bucket)))
        swapped_item = self.bucket[index]
        self.bucket[index] = item
        return swapped_item
