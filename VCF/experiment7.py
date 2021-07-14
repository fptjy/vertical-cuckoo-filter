import random
from four_ary_cf14_7 import D_ary_CF14_7
from random import randint

import datetime
import numpy as np

#存储实验，测试D-ary CF的空间利用率、存储时间消耗以及踢出重放次数。
raw_data = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
    for line in fin:
        raw_data.append(line.replace(",\n", ""))
fin.close()

number = 10

#存储结果

dcf_alpha_result = []
dcf_time_result = []

dcf_space_overhead = []
dcf_time_overhead = []

dcf_kicks_result = []
dcf_kicks = []


fingersize = 14
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 20
##设置参数
capacity1 = [2 ** 10, 2 ** 11, 2 ** 12, 2 ** 13, 2 ** 14, 2 ** 15, 2 ** 16, 2 ** 17, 2 ** 18, 2 ** 19, 2 ** 20, 2 ** 21,
             2 ** 22, 2 ** 23]


for j in range(len(capacity1)):
    for num in range(number):
        testdata1 = random.sample(raw_data, capacity1[j])

        dcf = D_ary_CF14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            dcf.I_insert7(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time_ms = (end - start).microseconds
        time_s = (end - start).seconds
        load_factor = dcf.size / capacity1[j]
        k = dcf.kicks / capacity1[j]

        dcf_space_overhead.append(load_factor)
        dcf_time_overhead.append(time_s + time_ms / 10 ** 6)
        dcf_kicks.append(k)


    dcf_alpha_result.append(np.mean(dcf_space_overhead))
    dcf_time_result.append(np.mean(dcf_time_overhead))
    dcf_kicks_result.append(np.mean(dcf_kicks))



print("dcf")
print(dcf_alpha_result)
print(dcf_time_result)
print(dcf_kicks_result)
print("   ")
print("   ")


# ##查询实验，测试D-ary CF的平均查询时间消耗。
#
# raw_data = []
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
#     for line in fin:
#         raw_data.append(line.replace(",\n", ""))
# fin.close()
#
# number = 10
#
# #存储结果
# dcf_time_overhead_100 = []
# dcf_time_result_100 = []
# dcf_time_overhead_50 = []
# dcf_time_result_50 = []
#
#
# fingersize = 14
# print("实验中指纹值长度为：", fingersize)
#
# ###filter size取2 ** 20
# ##设置参数
# capacity1 = [2 ** 20]
#
# for j in range(len(capacity1)):
#     for num in range(number):
#         testdata1 = random.sample(raw_data, capacity1[j])
#
#         #构造50%mixed的数据
#         list1 = list(set(raw_data) - set(testdata1))
#         list2 = random.sample(list1, capacity1[j] // 2)
#         list3 = random.sample(testdata1, capacity1[j] // 2)
#         list4 = list2 + list3
#         testdata2 = random.sample(list4, capacity1[j])
#
#
#         dcf = D_ary_CF14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
#         for i in range(capacity1[j]):
#             dcf.I_insert7(testdata1[i])
#
#         #进行100%existed的对象查询实验
#         start = datetime.datetime.now()  # 开始时间
#         for i in range(capacity1[j]):
#             dcf.I_contains7(testdata1[i])
#         end = datetime.datetime.now()  # 结束时间
#         time1 = (end - start).microseconds
#         time2 = (end - start).seconds
#         dcf_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])
#
#         # 进行50%mixed的对象查询实验
#         start = datetime.datetime.now()  # 开始时间
#         for i in range(capacity1[j]):
#             dcf.I_contains7(testdata2[i])
#         end = datetime.datetime.now()  # 结束时间
#         time1 = (end - start).microseconds
#         time2 = (end - start).seconds
#         dcf_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])
#
#     dcf_time_result_100.append(np.mean(dcf_time_overhead_100))
#     dcf_time_result_50.append(np.mean(dcf_time_overhead_50))
#
#
# print("dcf")
# print("100%查询结果")
# print(dcf_time_result_100)
# print("50%mixed查询结果")
# print(dcf_time_result_50)
# print("   ")
# print("   ")

#
# ##查询实验，测试D-ary CF的假阳性
# raw_data = []
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
#     for line in fin:
#         raw_data.append(line.replace(",\n", ""))
# fin.close()
#
# number = 1
#
# # 存储结果
#
# dcf_fp_result = []
# fingersize = 14
# print("实验中指纹值长度为：", fingersize)
#
# ###filter size取2 ** 20
# ##设置参数
# capacity1 = [2 ** 20]
#
# for j in range(len(capacity1)):
#     for num in range(number):
#
#         # 局部变量存储查询返回True的结果数量
#         dcf_fp = 0
#
#         # 构造100% none existed 的数据
#         testdata1 = random.sample(raw_data, capacity1[j])
#         list1 = list(set(raw_data) - set(testdata1))
#         testdata2 = random.sample(list1, capacity1[j])
#
#         dcf = D_ary_CF14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
#         for i in range(capacity1[j]):
#             dcf.I_insert7(testdata1[i])
#
#         #  进行100% none existed的对象查询实验，以测试假阳性
#         for i in range(capacity1[j]):
#             if dcf.I_contains7(testdata1[i]):
#                 dcf_fp += 1
#         dcf_fp_result.append((dcf_fp) / dcf.size)
#
# print("dcf")
# print(np.mean(dcf_fp_result))
# print("   ")
# print("   ")
