import sys
import csv

sys.path.append(r"C:/Users/fptjy/ArkFilter_experiment/VCF_for_Dynamics")

import random
from Vcuckoofilter_DJBhash import VCuckooFilter_DJBhash
import VCF_dynamic_operations as VCF_d_o


sys.path.append(r"C:/Users/fptjy/ArkFilter_experiment/Dynamic_CF")
from Dynamic_cuckoo_filter import single_CF
import Dynamic_cuckoo_filter as CF_d_o
from cuckoofilter import CuckooFilter


"""
#Read insertion data and data preprocess
"""
raw_data1 = []
with open('C:/Users/fptjy/ArkFilter_experiment/experiment/IP_final_min_int_sort.csv', 'r') as fin:
    for line in fin:
        raw_data1.append(line.replace("\n", ""))
fin.close()

# raw_data1 = []
# delta = 100000
# for i in range(len(raw_data0) - delta):
#     raw_data1.append(raw_data0[i])

insert_result = [[]]
tem = 0
for i in range(len(raw_data1)):

    x = int(raw_data1[i].split(",")[1])
    y = raw_data1[i].split(",")[0]
    if x == tem:
        insert_result[x].append(y)
    elif x == tem + 1:
        insert_result.append([])
        insert_result[x].append(y)
        tem += 1
    else:
        distance = x - tem
        for j in range(distance - 1):
            insert_result.append(["non"])
            tem += 1
        insert_result.append([])
        insert_result[x].append(y)
        tem += 1

print(len(insert_result))  # 81230

"""
#Read deletion data and data preprocess
"""
raw_data2 = []
with open('C:/Users/fptjy/ArkFilter_experiment/experiment/IP_final_max_int_sort.csv', 'r') as fin:
    for line in fin:
        raw_data2.append(line.replace("\n", ""))
fin.close()

delete_result = [[]]
tem = 0
for i in range(len(raw_data2)):

    x = int(raw_data2[i].split(",")[1])
    y = raw_data2[i].split(",")[0]
    if x == tem:
        delete_result[x].append(y)
    elif x == tem + 1:
        delete_result.append([])
        delete_result[x].append(y)
        tem += 1
    else:
        distance = x - tem
        for j in range(distance - 1):
            delete_result.append(["non"])
            tem += 1
        delete_result.append([])
        delete_result[x].append(y)
        tem += 1

##过滤掉到达但未离开的元素
CF_filtrate = CuckooFilter(capacity=2 ** 21, bucket_size=4, fingerprint_size=18)
# CF_mur_filter = CuckooFilter_mur(capacity=2 ** 21, bucket_size=4, fingerprint_size=18)
for i in range(len(delete_result)):
    if delete_result[i] == "non":
        print("non appear in delete")
    else:
        for j in range(len(delete_result[i])):
            CF_filtrate.insert(delete_result[i][j])
            # CF_mur_filter.insert(delete_result[i][j])

count = 0
for i in range(len(insert_result)):
    if insert_result[i] == "non":
        print("non appear in insert")
    else:
        for j in range(len(insert_result[i])):
            # if not CF_filtrate.contains(insert_result[i][j]) or not CF_mur_filter.contains(insert_result[i][j]):
            if not CF_filtrate.contains(insert_result[i][j]):
                count += 1
                insert_result[i][j] = "extra_element"
print(count)

count2 = 0
for i in range(len(insert_result)):
    while "extra_element" in insert_result[i]:
        insert_result[i].remove("extra_element")
        count2 += 1
print(count2)

"""
###Initialize the data structure

Initial parameters:
the threshold of relocate
ave_item = 1080000*2s/90s = 24000 = 2**15 = 32768

DVCF: capacity = 2**13 = 8192
    b = 1
    ave_item_fp = 4.8*10^-4
    length of fingerprint =  15

AF: m = 2**13=8192
    b = 1
    ave_item_fp = 4.8*10^-4
    length of fingerprint =  log(m/2,2) = 12

DCF_4:(Same granularity as AF)
    ave_item = 2**15
    exp_block_num=4
    b = 4
    single_table_length = 2**11 = 2048
    ave_item_fp = 4.8*10^-4
    length of fingerprint =  17

DCF_8:(The granularity is equal to half of the AF)
    ave_item = 2**15
    exp_block_num = 8
    b = 4
    single_table_length = 2**10 = 1024
    ave_item_fp = 4.8*10^-4
    length of fingerprint =  18
"""

DVCF = VCuckooFilter_DJBhash(capacity=2 ** 13)
# DCF_4 = single_CF(item_num=2 ** 15, fp=0.00048, exp_block_num=4)
# DCF_8 = single_CF(item_num=2 ** 15, fp=0.00048, exp_block_num=8)

DVCF_test_result = []
# DCF_4_test_result = []
# DCF_8_test_result = []
# contrast_result = []
tem = 0

# print(len(delete_result)) #82757
# print(len(insert_result)) #81943

for i in range(len(insert_result)):
    if insert_result[i] == "non" or len(insert_result[i]) == 0:
        print("non appear in insert_result", i)
        VCF_d_o.dvcf_delete(data=delete_result[i], target_VCF=DVCF)
        VCF_d_o.dynamic_decrease(target_VCF=DVCF)


        x0 = DVCF.capacity * len(DVCF.buckets[0].bucket)
        DVCF_test_result.append(x0)



    else:
        # DVCF
        VCF_d_o.dvcf_insert(data=insert_result[i], target_VCF=DVCF)
        VCF_d_o.dvcf_delete(data=delete_result[i], target_VCF=DVCF)
        VCF_d_o.dynamic_decrease(target_VCF=DVCF)


        # # DCF_4
        # CF_d_o.dcf_insert(data=insert_result[i], sketch=DCF_4)
        # CF_d_o.dcf_delete(data=delete_result[i], sketch=DCF_4)
        # CF_d_o.dcf_compact(sketch=DCF_4)
        #
        # # DCF_8
        # CF_d_o.dcf_insert(data=insert_result[i], sketch=DCF_8)
        # CF_d_o.dcf_delete(data=delete_result[i], sketch=DCF_8)
        # CF_d_o.dcf_compact(sketch=DCF_8)
        #
        # # contrast result
        # contrast = tem + len(insert_result[i]) - len(delete_result[i])
        # contrast_result.append(contrast)
        # tem = contrast_result[i]

        x0 = DVCF.capacity * len(DVCF.buckets[0].bucket)
        DVCF_test_result.append(x0)

        # x2 = len(DCF_4) * DCF_4[0].capacity * 4
        # DCF_4_test_result.append(x2)
        #
        # x3 = len(DCF_8) * DCF_8[0].capacity * 4
        # DCF_8_test_result.append(x3)

for i in range(len(delete_result) - len(insert_result)):
    # DVCF
    VCF_d_o.dvcf_delete(data=delete_result[i + len(insert_result)], target_VCF=DVCF)
    VCF_d_o.dynamic_decrease(target_VCF=DVCF)


    # # DCF_4
    # CF_d_o.dcf_delete(data=delete_result[i + len(insert_result)], sketch=DCF_4)
    # CF_d_o.dcf_compact(sketch=DCF_4)
    #
    # # DCF_8
    # CF_d_o.dcf_delete(data=delete_result[i + len(insert_result)], sketch=DCF_8)
    # CF_d_o.dcf_compact(sketch=DCF_8)
    #
    # # contrast result
    # contrast = contrast_result[i + len(insert_result) - 1] - len(delete_result[i + len(insert_result)])
    # contrast_result.append(contrast)

    y = DVCF.capacity * len(DVCF.buckets[0].bucket)
    DVCF_test_result.append(y)

    # y2 = len(DCF_4) * DCF_4[0].capacity * 4
    # DCF_4_test_result.append(y2)
    #
    #
    # y3 = len(DCF_8) * DCF_8[0].capacity * 4
    # DCF_8_test_result.append(y3)

# ##contrast_result
# # 1. 创建文件对象
# f = open('contrast_result.csv', 'w', encoding='utf-8', newline="")
# # 2. 基于文件对象构建 csv写入对象
# csv_writer = csv.writer(f)
# # 4. 写入csv文件内容
# for i in range(len(contrast_result)):
#     csv_writer.writerow([str(contrast_result[i])])
# # 5. 关闭文件
# f.close()

##DVCF_test_result
# 1. 创建文件对象
f = open('DVCF_test_result_jizhi.csv', 'w', encoding='utf-8', newline="")
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 4. 写入csv文件内容
for i in range(len(DVCF_test_result)):
    csv_writer.writerow([str(DVCF_test_result[i])])
# 5. 关闭文件
f.close()


# ##DCF_4_test_result
# # 1. 创建文件对象
# f = open('DCF_4_test_result.csv', 'w', encoding='utf-8', newline="")
# # 2. 基于文件对象构建 csv写入对象
# csv_writer = csv.writer(f)
# # 4. 写入csv文件内容
# for i in range(len(DCF_4_test_result)):
#     csv_writer.writerow([str(DCF_4_test_result[i])])
# # 5. 关闭文件
# f.close()
#
# ##DCF_8_test_result
# # 1. 创建文件对象
# f = open('DCF_8_test_result.csv', 'w', encoding='utf-8', newline="")
# # 2. 基于文件对象构建 csv写入对象
# csv_writer = csv.writer(f)
# # 4. 写入csv文件内容
# for i in range(len(DCF_8_test_result)):
#     csv_writer.writerow([str(DCF_8_test_result[i])])
# # 5. 关闭文件
# f.close()
