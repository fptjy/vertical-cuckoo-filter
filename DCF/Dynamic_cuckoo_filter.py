from cuckoofilter import CuckooFilter
import math


def Dynamic_CF(item_num, fp, exp_block_num=6):
    """

    """
    capacity = item_num
    single_table_length = int(capacity / 4 / exp_block_num)
    single_capacity = single_table_length * 0.9375 * 4
    false_positive = fp
    single_false_positive = 1 - (1.0 - false_positive) ** (single_capacity / capacity)

    fingerprint_size_double = math.ceil(math.log(8.0 / single_false_positive, 2))

    # if fingerprint_size_double > 0 and fingerprint_size_double <= 4:
    #     dcf_fingerprint_size = 4
    # elif fingerprint_size_double > 4 and fingerprint_size_double <= 8:
    #     dcf_fingerprint_size = 8
    # elif fingerprint_size_double > 8 and fingerprint_size_double <= 12:
    #     dcf_fingerprint_size = 12
    # elif fingerprint_size_double > 12 and fingerprint_size_double <= 16:
    #     dcf_fingerprint_size = 16
    # elif fingerprint_size_double > 16 and fingerprint_size_double <= 24:
    #     dcf_fingerprint_size = 16
    # elif fingerprint_size_double > 24 and fingerprint_size_double <= 32:
    #     dcf_fingerprint_size = 16
    # else:
    #     print("fingerprint out of range!!!")
    #     dcf_fingerprint_size = 16

    dcf_fingerprint_size = fingerprint_size_double

    DCF_list = [None] * exp_block_num
    for i in range(exp_block_num):
        DCF_list[i] = CuckooFilter(capacity=single_table_length, fingerprint_size=dcf_fingerprint_size)
    return DCF_list


def single_CF(item_num, fp, exp_block_num=6):
    """

    """
    capacity = item_num
    single_table_length = int(capacity / 4 / exp_block_num)
    single_capacity = single_table_length * 0.9375 * 4
    false_positive = fp
    single_false_positive = 1 - (1.0 - false_positive) ** (single_capacity / capacity)

    fingerprint_size_double = math.ceil(math.log(8.0 / single_false_positive, 2))

    dcf_fingerprint_size = fingerprint_size_double

    single_cf = CuckooFilter(capacity=single_table_length, fingerprint_size=dcf_fingerprint_size)
    return [single_cf]


def dcf_insert(data, sketch):
    cur = len(sketch) - 1
    # while sketch[cur].size == 0 and cur > 1:
    #     cur -= 1
    for i in range(len(data)):
        result = sketch[cur].insert(data[i])
        if result != "yes":
            cur += 1
            if cur >= len(sketch):
                single_cf = CuckooFilter(capacity=sketch[0].capacity, fingerprint_size=sketch[0].fingerprint_size)
                sketch.append(0)
                sketch[cur] = single_cf
                sketch[cur].buckets[result[0]].insert(result[1])
                sketch[cur].size += 1
            else:
                sketch[cur].buckets[result[0]].insert(result[1])
                sketch[cur].size += 1
    return True


def dcf_delete(data, sketch):
    for i in range(len(data)):
        j = 0
        while j < len(sketch):
            if sketch[j].delete(data[i]):
                break
            else:
                j += 1
    return True


#
# def dcf_delete(data, sketch):
#     for i in range(len(sketch)):
#         if sketch[i].delete(data):
#             return True
#     return False


def is_compact(sketch):
    sort_list = [[i, sketch[i].size] for i in range(len(sketch))]
    result = sorted(sort_list, key=(lambda x: x[1]))
    sort = [result[i][0] for i in range(len(sketch))]

    for i in range(sketch[sort[0]].capacity):
        if len(sketch[sort[0]].buckets[i].bucket) > 0:
            for j in range(len(sketch[sort[0]].buckets[i].bucket)):
                interim = False
                num = 1
                while num < len(sort):
                    if len(sketch[sort[len(sort) - num]].buckets[i].bucket) < sketch[0].bucket_size:
                        # print(len(sketch[sort[len(sort) - num]].buckets[i].bucket))
                        # print(sketch[0].bucket_size)
                        interim = True
                        break
                    num += 1
                if not interim:
                    # print("sketch[sort[0]].size", sketch[sort[0]].size)
                    return False
    return True


def dcf_compact(sketch):
    sort_list = [[i, sketch[i].size] for i in range(len(sketch))]
    result = sorted(sort_list, key=(lambda x: x[1]))
    sort = [result[i][0] for i in range(len(sketch))]

    if not is_compact(sketch):
        # print("the filter is too full to compact, consider removing more elements")
        return False

    if sketch[sort[0]].size == 0:
        del sketch[sort[0]]
        return True

    if sketch[sort[0]].size > 0 and is_compact(sketch):
        for i in range(sketch[sort[0]].capacity):
            if len(sketch[sort[0]].buckets[i].bucket) > 0:
                for l in range(len(sketch[sort[0]].buckets[i].bucket)):
                    evict_item = sketch[sort[0]].buckets[i].bucket[l]
                    num = 1
                    while num < len(sort):
                        if sketch[sort[len(sort) - num]].buckets[i].insert(evict_item):
                            sketch[sort[len(sort) - num]].size += 1
                            break
                        num += 1

        del sketch[sort[0]]
        return True
