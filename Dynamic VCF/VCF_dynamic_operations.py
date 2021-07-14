import Vcuckoofilter_DJBhash
import random
import exceptions


def dvcf_insert(data, target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024)):
    for i in range(len(data)):
        result = target_VCF.I_insert(data[i])
        if result != "yes":
            dynamic_increase(target_VCF=target_VCF)
            target_VCF.buckets[result[1]].insert(result[0])
            target_VCF.size += 1
    return True


def dvcf_delete(data, target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024)):
    for i in range(len(data)):
        target_VCF.I_delete(data[i])
    return True


def dynamic_increase(target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024), increase_size=1):
    """
    DAF scales up by increasing the number of slots in each bucket adaptively.

    Once the space utilization of filter reaching the predefined threshold value, it triggers dynamic_increase.

    :param target_VCF: target Ark Filter which needs to scale up.
    :param increase_size: the expanded size of target Ark Filter.
    :return: True.
    """
    for i in range(target_VCF.capacity):
        for j in range(increase_size):
            target_VCF.buckets[i].bucket.append(-1)
    return True


def sort(target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024)):
    for i in range(target_VCF.capacity):
        count = 0
        for j in range(len(target_VCF.buckets[i].bucket)):
            if -1 in target_VCF.buckets[i].bucket:
                del target_VCF.buckets[i].bucket[target_VCF.buckets[i].bucket.index(-1)]
                count += 1
        for j in range(count):
            target_VCF.buckets[i].bucket.append(-1)
    return True


def find_overflow(target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024)):
    """
    Find out a bucket with no empty slots
    :param target_VCF: target Ark Filter which needs to scale up.
    :return: The index value of the first bucket which has no empty slot. or
            False: all buckets have at least one empty slot.
    """
    for i in range(target_VCF.capacity):
        if not target_VCF.buckets[i].is_not_full():
            return i
    return -1


def solve_overflow(target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024), target_bucket=0):
    """

    """
    bucketsize = len(target_VCF.buckets[target_bucket])

    victim_fp = target_VCF.buckets[target_bucket].bucket[-1]
    target_VCF.buckets[target_bucket].bucket[-1] = -1

    fp_hash_value = target_VCF._get_fp_hash_value(victim_fp)
    h2 = target_VCF._get_alternate1_index(target_bucket, fp_hash_value)
    h3 = target_VCF._get_alternate2_index(target_bucket, fp_hash_value)
    h4 = target_VCF._get_alternate3_index(target_bucket, fp_hash_value)

    if -1 in target_VCF.buckets[h2].bucket and target_VCF.buckets[h2].bucket.index(-1) < bucketsize - 1:
        target_VCF.buckets[h2].insert(victim_fp)
        return True
    elif -1 in target_VCF.buckets[h3].bucket and target_VCF.buckets[h3].bucket.index(-1) < bucketsize - 1:
        target_VCF.buckets[h3].insert(victim_fp)
        return True
    elif -1 in target_VCF.buckets[h4].bucket and target_VCF.buckets[h4].bucket.index(-1) < bucketsize - 1:
        target_VCF.buckets[h4].insert(victim_fp)
        return True

    eviction_index = random.choice([target_bucket, h2, h3, h4])

    f = 0

    for _ in range(50):

        # f = target_VCF.buckets[eviction_index].swap(victim_fp)??

        index = random.choice(range(len(target_VCF.buckets[eviction_index].bucket) - 1))  # 从桶中除最后一个槽中随机选一个
        f = target_VCF.buckets[eviction_index].bucket[index]
        target_VCF.buckets[eviction_index].bucket[index] = victim_fp

        f_hash_value = target_VCF._get_fp_hash_value(f)
        eviction_index1 = target_VCF._get_alternate1_index(eviction_index, f_hash_value)
        eviction_index2 = target_VCF._get_alternate2_index(eviction_index, f_hash_value)
        eviction_index3 = target_VCF._get_alternate3_index(eviction_index, f_hash_value)

        if -1 in target_VCF.buckets[eviction_index1].bucket and target_VCF.buckets[eviction_index1].bucket.index(
                -1) < bucketsize - 1:
            target_VCF.buckets[eviction_index1].insert(f)
            return True
        elif -1 in target_VCF.buckets[eviction_index2].bucket and target_VCF.buckets[eviction_index2].bucket.index(
                -1) < bucketsize - 1:
            target_VCF.buckets[eviction_index2].insert(f)
            return True
        elif -1 in target_VCF.buckets[eviction_index3].bucket and target_VCF.buckets[eviction_index3].bucket.index(
                -1) < bucketsize - 1:
            target_VCF.buckets[eviction_index3].insert(f)
            return True
        eviction_index = random.choice([eviction_index1, eviction_index2, eviction_index3])
        victim_fp = f

    # The number of re-locate operations has reached the threshold
    # we need to put the victim items back into filter when relocation failed

    if -1 in target_VCF.buckets[eviction_index].bucket:
        target_VCF.buckets[eviction_index].insert(victim_fp)
        return False

    for _ in range(50):

        index = random.choice(range(len(target_VCF.buckets[eviction_index].bucket)))  # 从桶中除最后一个槽中随机选一个
        f = target_VCF.buckets[eviction_index].bucket[index]
        target_VCF.buckets[eviction_index].bucket[index] = victim_fp

        f_hash_value = target_VCF._get_fp_hash_value(f)
        eviction_index1 = target_VCF._get_alternate1_index(eviction_index, f_hash_value)
        eviction_index2 = target_VCF._get_alternate2_index(eviction_index, f_hash_value)
        eviction_index3 = target_VCF._get_alternate3_index(eviction_index, f_hash_value)

        if -1 in target_VCF.buckets[eviction_index1].bucket:
            target_VCF.buckets[eviction_index1].insert(f)
            return False
        elif -1 in target_VCF.buckets[eviction_index2].bucket:
            target_VCF.buckets[eviction_index2].insert(f)
            return False
        elif -1 in target_VCF.buckets[eviction_index3].bucket:
            target_VCF.buckets[eviction_index3].insert(f)
            return False
        eviction_index = random.choice([eviction_index1, eviction_index2, eviction_index3])
        victim_fp = f

    return False


def dynamic_decrease(target_VCF=Vcuckoofilter_DJBhash.VCuckooFilter_DJBhash(capacity=1024)):
    anychange = 1
    if target_VCF.size > 0.9 * (len(target_VCF.buckets[0].bucket) - 1) * target_VCF.capacity:
        # print("Did not meet the conditions for dynamic_decrease")
        return False

    if len(target_VCF.buckets[0].bucket) == 1:
        find_overflow_result = find_overflow(target_VCF=target_VCF)
        if find_overflow_result == -1:
            for j in range(target_VCF.capacity):
                del target_VCF.buckets[j].bucket[-1]
            return True
        else:
            return False

    # the third situation
    sort(target_VCF)
    while (anychange == 1):
        find_overflow_result = find_overflow(target_VCF=target_VCF)
        if find_overflow_result == -1:
            break
        else:
            if not solve_overflow(target_VCF=target_VCF, target_bucket=find_overflow_result):
                return False

    for j in range(target_VCF.capacity):
        del target_VCF.buckets[j].bucket[-1]

    return True
