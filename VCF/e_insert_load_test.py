# 在不同空间利用率下的存储的吞吐量实验

import math
import random
from random import randint
import time
import numpy as np

from Vcuckoofilter14_7 import VCuckooFilter14_7
from Vcuckoofilter14_6 import VCuckooFilter14_6
from Vcuckoofilter14_5 import VCuckooFilter14_5
from Vcuckoofilter14_4 import VCuckooFilter14_4
from Vcuckoofilter14_3 import VCuckooFilter14_3
from Vcuckoofilter14_2 import VCuckooFilter14_2
from Vcuckoofilter14_1 import VCuckooFilter14_1

raw_data = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
    for line in fin:
        raw_data.append(line.replace(",\n", ""))
fin.close()

fingersize = 14
print("实验中指纹值长度为：", fingersize)

cf_insert_thp = []
vcf7_insert_thp = []
vcf6_insert_thp = []
vcf5_insert_thp = []
vcf4_insert_thp = []
vcf3_insert_thp = []
vcf2_insert_thp = []
vcf1_insert_thp = []

dvcf8_insert_thp = []
dvcf7_insert_thp = []
dvcf6_insert_thp = []
dvcf5_insert_thp = []
dvcf4_insert_thp = []
dvcf3_insert_thp = []
dvcf2_insert_thp = []
dvcf1_insert_thp = []

cf_kicks = []
vcf7_kicks = []
vcf6_kicks = []
vcf5_kicks = []
vcf4_kicks = []
vcf3_kicks = []
vcf2_kicks = []
vcf1_kicks = []

dvcf8_kicks = []
dvcf7_kicks = []
dvcf6_kicks = []
dvcf5_kicks = []
dvcf4_kicks = []
dvcf3_kicks = []
dvcf2_kicks = []
dvcf1_kicks = []

cishu = 1
capacity_of_filter = 2 ** 18
for cs in range(cishu):
    testdata = random.sample(raw_data, capacity_of_filter * 4)

    # # 参数设置并测试
    # alpha_array = [0.025, 0.075, 0.125, 0.175]
    # for i in range(len(alpha_array)):
    #     print("##########################################")
    #     print("##########################################")
    #     print("##########################################")
    #
    #     alpha = alpha_array[i]
    #     print("table occupancy:", alpha)
    #     delta = 5000
    #     print("delta items:", delta)
    #
    #     # 先存储达到alpha时的一定数量的对象
    #     f = BloomFilter(capacity=2 ** 20, error_rate=0.00001)
    #     for i in range_fn(int(alpha * len(testdata) - delta / 2)):
    #         f.add(testdata[i], skip_check=True)
    #
    #     cf = CuckooFilter(capacity=2 ** 18, bucket_size=4, fingerprint_size=19)
    #     for i in range(int(alpha * len(testdata) - delta / 2)):
    #         cf.insert(testdata[i])
    #
    #     ARK = Ark_Filter(capacity=2 ** 18)
    #     for i in range(int(alpha * len(testdata) - delta / 2)):
    #         ARK.insert(testdata[i])
    #
    #     qf = QuotientFilter()
    #     _testdata = [0 for i in range(qf.p)]
    #     for i in range(qf.p):
    #         _testdata[i] = testdata[i]
    #     for i in range(int(alpha * qf.p - delta / 2)):
    #         qf.addKey(_testdata[i])
    #
    #     # 开始测试达到alpha时，插入delta个对象的吞吐量
    #     start = datetime.datetime.now()
    #     for i in range(delta):
    #         f.add(testdata[int(alpha * len(testdata) - delta / 2) + i], skip_check=True)
    #     end = datetime.datetime.now()
    #     time_ms = (end - start).microseconds
    #     time_s = (end - start).seconds
    #     time_consume = time_s * 10 ** 6 + time_ms
    #     # print("用的微妙", time_ms)
    #     # print("时间消耗：", time_consume)
    #     if time_consume == 0:
    #         insert_thp_BF.append(0)
    #     else:
    #         insert_thp_BF.append(delta * 10 ** 6 / time_consume)
    #     # print("bloom filter:")
    #     # print("{:5.3f} microseconds to insert delta items, {:10.2f} entries/microsecond".format(
    #     #     time_consume, delta / time_consume))
    #     #
    #     # insert_thp_BF.append(delta * 10 ** 6 / time_consume)
    #
    #
    #     start = datetime.datetime.now()
    #     for i in range(delta):
    #         cf.insert(testdata[int(alpha * len(testdata) - delta / 2) + i])
    #     end = datetime.datetime.now()
    #     time_ms = (end - start).microseconds
    #     time_s = (end - start).seconds
    #     time_consume = time_s * 10 ** 6 + time_ms
    #     # print("用的微妙", time_ms)
    #     # print("时间消耗：", time_consume)
    #     if time_consume == 0:
    #         insert_thp_CF.append(0)
    #     else:
    #         insert_thp_CF.append(delta * 10 ** 6 / time_consume)
    #
    #     # print("cuckoo filter:")
    #     # print("{:5.3f} microseconds to insert delta items, {:10.2f} entries/microsecond".format(
    #     #     time_consume, delta / time_consume))
    #     # insert_thp_CF.append(delta * 10 ** 6 / time_consume)
    #
    #
    #     start = datetime.datetime.now()
    #     for i in range(delta):
    #         ARK.insert(testdata[int(alpha * len(testdata) - delta / 2) + i])
    #     end = datetime.datetime.now()
    #     time_ms = (end - start).microseconds
    #     time_s = (end - start).seconds
    #     time_consume = time_s * 10 ** 6 + time_ms
    #     # print("用的微妙", time_ms)
    #     # print("时间消耗：", time_consume)
    #     if time_consume == 0:
    #         insert_thp_ArkF.append(0)
    #     else:
    #         insert_thp_ArkF.append(delta * 10 ** 6 / time_consume)
    #     # print("Ark filter:")
    #     # print("{:5.3f} microseconds to insert delta items, {:10.2f} entries/microsecond".format(
    #     #     time_consume, delta / time_consume))
    #     # insert_thp_ArkF.append(delta * 10 ** 6 / time_consume)
    #
    #     qf_delta = 3000
    #     start = datetime.datetime.now()
    #     for i in range(qf_delta):
    #         qf.addKey(_testdata[int(alpha * len(_testdata) - qf_delta / 2) + i])
    #     end = datetime.datetime.now()
    #     time_ms = (end - start).microseconds
    #     time_s = (end - start).seconds
    #     time_consume = time_s * 10 ** 6 + time_ms
    #     # print("用的微妙", time_ms)
    #     # print("时间消耗：", time_consume)
    #     if time_consume == 0:
    #         insert_thp_QF.append(0)
    #     else:
    #         insert_thp_QF.append(qf_delta * 10 ** 6 / time_consume)
    #
    #     # print("Quotient filter:")
    #     # print("qf_delta=", qf_delta)
    #     # print("{:5.3f} microseconds to insert delta items, {:10.2f} entries/microsecond".format(
    #     #     time_consume, qf_delta / time_consume))
    #     # insert_thp_QF.append(qf_delta * 10 ** 6 / time_consume)

    # 参数设置并测试0.025
    # alpha_array = np.arange(0.225, 1, 0.05)
    alpha_array = np.arange(0.025, 1, 0.05)
    for i in range(len(alpha_array)):
        print("##########################################")
        print("##########################################")
        print("##########################################")

        alpha = alpha_array[i]
        print("table occupancy:", alpha)
        delta = 3000
        print("delta items:", delta)

        # 先存储达到alpha时的一定数量的对象
        cf = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        for j in range(int(alpha * len(testdata) - delta / 2)):
            cf.I_insert0(testdata[j])

        # vcf7 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf7.I_insert7(testdata[j])
        #
        # vcf6 = VCuckooFilter14_6(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf6.I_insert6(testdata[j])
        #
        # vcf5 = VCuckooFilter14_5(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf5.I_insert5(testdata[j])
        #
        # vcf4 = VCuckooFilter14_4(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf4.I_insert4(testdata[j])
        #
        # vcf3 = VCuckooFilter14_3(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf3.I_insert3(testdata[j])
        #
        # vcf2 = VCuckooFilter14_2(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf2.I_insert2(testdata[j])
        #
        # vcf1 = VCuckooFilter14_1(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     vcf1.I_insert1(testdata[j])

        # DVCF的实验
        dvcf8 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        for j in range(int(alpha * len(testdata) - delta / 2)):
            dvcf8.D_insert(testdata[j], threshold1=2 ** 14 * 0.2, threshold2=2 ** 14 * 0.8)

        # dvcf7 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf7.D_insert(testdata[j], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))
        #
        # dvcf6 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf6.D_insert(testdata[j], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))
        #
        # dvcf5 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf5.D_insert(testdata[j], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))
        #
        # dvcf4 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf4.D_insert(testdata[j], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))
        #
        # dvcf3 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf3.D_insert(testdata[j], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))
        #
        # dvcf2 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf2.D_insert(testdata[j], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))
        #
        # dvcf1 = VCuckooFilter14_7(capacity=capacity_of_filter, bucket_size=4, fingerprint_size=fingersize)
        # for j in range(int(alpha * len(testdata) - delta / 2)):
        #     dvcf1.D_insert(testdata[j], 2 ** 13 * (1 - 0.125), 2 ** 13 * (1 + 0.125))

        # 开始测试达到alpha时，插入delta个对象的吞吐量

        start = time.time()
        for j in range(delta):
            cf.I_insert0(testdata[int(alpha * len(testdata) - delta / 2) + j])
        end = time.time()
        cf_insert_thp.append(delta / (end - start))
        cf_kicks.append(cf.kicks)

        # # test of vcf
        # start = time.time()
        # for j in range(delta):
        #     vcf7.I_insert7(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf7_insert_thp.append(delta / (end - start))
        # vcf7_kicks.append(vcf7.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf6.I_insert6(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf6_insert_thp.append(delta / (end - start))
        # vcf6_kicks.append(vcf6.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf5.I_insert5(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf5_insert_thp.append(delta / (end - start))
        # vcf5_kicks.append(vcf5.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf4.I_insert4(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf4_insert_thp.append(delta / (end - start))
        # vcf4_kicks.append(vcf4.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf3.I_insert3(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf3_insert_thp.append(delta / (end - start))
        # vcf3_kicks.append(vcf3.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf2.I_insert2(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf2_insert_thp.append(delta / (end - start))
        # vcf2_kicks.append(vcf2.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     vcf1.I_insert1(testdata[int(alpha * len(testdata) - delta / 2) + j])
        # end = time.time()
        # vcf1_insert_thp.append(delta / (end - start))
        # vcf1_kicks.append(vcf1.kicks)

        # test of dvcf
        start = time.time()
        for j in range(delta):
            dvcf8.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], threshold1=2 ** 14 * 0.2, threshold2=2 ** 14 * 0.8)
        end = time.time()
        dvcf8_insert_thp.append(delta / (end - start))
        dvcf8_kicks.append(dvcf8.kicks)

        # start = time.time()
        # for j in range(delta):
        #     dvcf7.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.875),
        #                    2 ** 13 * (1 + 0.875))
        # end = time.time()
        # dvcf7_insert_thp.append(delta / (end - start))
        # dvcf7_kicks.append(dvcf7.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf6.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.75),
        #                    2 ** 13 * (1 + 0.75))
        # end = time.time()
        # dvcf6_insert_thp.append(delta / (end - start))
        # dvcf6_kicks.append(dvcf6.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf5.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.625),
        #                    2 ** 13 * (1 + 0.625))
        # end = time.time()
        # dvcf5_insert_thp.append(delta / (end - start))
        # dvcf5_kicks.append(dvcf5.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf4.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.5),
        #                    2 ** 13 * (1 + 0.5))
        # end = time.time()
        # dvcf4_insert_thp.append(delta / (end - start))
        # dvcf4_kicks.append(dvcf4.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf3.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.375),
        #                    2 ** 13 * (1 + 0.375))
        # end = time.time()
        # dvcf3_insert_thp.append(delta / (end - start))
        # dvcf3_kicks.append(dvcf3.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf2.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.25),
        #                    2 ** 13 * (1 + 0.25))
        # end = time.time()
        # dvcf2_insert_thp.append(delta / (end - start))
        # dvcf2_kicks.append(dvcf2.kicks)
        #
        # start = time.time()
        # for j in range(delta):
        #     dvcf1.D_insert(testdata[int(alpha * len(testdata) - delta / 2) + j], 2 ** 13 * (1 - 0.125),
        #                    2 ** 13 * (1 + 0.125))
        # end = time.time()
        # dvcf1_insert_thp.append(delta / (end - start))
        # dvcf1_kicks.append(dvcf1.kicks)

cf_insert_thp2 = [0 for i in range(20)]
# vcf7_insert_thp2 = [0 for i in range(20)]
# vcf6_insert_thp2 = [0 for i in range(20)]
# vcf5_insert_thp2 = [0 for i in range(20)]
# vcf4_insert_thp2 = [0 for i in range(20)]
# vcf3_insert_thp2 = [0 for i in range(20)]
# vcf2_insert_thp2 = [0 for i in range(20)]
# vcf1_insert_thp2 = [0 for i in range(20)]

dvcf8_insert_thp2 = [0 for i in range(20)]
# dvcf7_insert_thp2 = [0 for i in range(20)]
# dvcf6_insert_thp2 = [0 for i in range(20)]
# dvcf5_insert_thp2 = [0 for i in range(20)]
# dvcf4_insert_thp2 = [0 for i in range(20)]
# dvcf3_insert_thp2 = [0 for i in range(20)]
# dvcf2_insert_thp2 = [0 for i in range(20)]
# dvcf1_insert_thp2 = [0 for i in range(20)]

for j in range(20):
    k = j
    for i in range(cishu):
        cf_insert_thp2[j] += cf_insert_thp[k]
        # vcf7_insert_thp2[j] += vcf7_insert_thp[k]
        # vcf6_insert_thp2[j] += vcf6_insert_thp[k]
        # vcf5_insert_thp2[j] += vcf5_insert_thp[k]
        # vcf4_insert_thp2[j] += vcf4_insert_thp[k]
        # vcf3_insert_thp2[j] += vcf3_insert_thp[k]
        # vcf2_insert_thp2[j] += vcf2_insert_thp[k]
        # vcf1_insert_thp2[j] += vcf1_insert_thp[k]

        dvcf8_insert_thp2[j] += dvcf8_insert_thp[k]
        # dvcf7_insert_thp2[j] += dvcf7_insert_thp[k]
        # dvcf6_insert_thp2[j] += dvcf6_insert_thp[k]
        # dvcf5_insert_thp2[j] += dvcf5_insert_thp[k]
        # dvcf4_insert_thp2[j] += dvcf4_insert_thp[k]
        # dvcf3_insert_thp2[j] += dvcf3_insert_thp[k]
        # dvcf2_insert_thp2[j] += dvcf2_insert_thp[k]
        # dvcf1_insert_thp2[j] += dvcf1_insert_thp[k]

        k += 20

cf_kicks2 = [0 for i in range(20)]
# vcf7_kicks2 = [0 for i in range(20)]
# vcf6_kicks2 = [0 for i in range(20)]
# vcf5_kicks2 = [0 for i in range(20)]
# vcf4_kicks2 = [0 for i in range(20)]
# vcf3_kicks2 = [0 for i in range(20)]
# vcf2_kicks2 = [0 for i in range(20)]
# vcf1_kicks2 = [0 for i in range(20)]

dvcf8_kicks2 = [0 for i in range(20)]
# dvcf7_kicks2 = [0 for i in range(20)]
# dvcf6_kicks2 = [0 for i in range(20)]
# dvcf5_kicks2 = [0 for i in range(20)]
# dvcf4_kicks2 = [0 for i in range(20)]
# dvcf3_kicks2 = [0 for i in range(20)]
# dvcf2_kicks2 = [0 for i in range(20)]
# dvcf1_kicks2 = [0 for i in range(20)]

for j in range(20):
    k = j
    for i in range(cishu):
        cf_kicks2[j] += cf_kicks[k]
        # vcf7_kicks2[j] += vcf7_kicks[k]
        # vcf6_kicks2[j] += vcf6_kicks[k]
        # vcf5_kicks2[j] += vcf5_kicks[k]
        # vcf4_kicks2[j] += vcf4_kicks[k]
        # vcf3_kicks2[j] += vcf3_kicks[k]
        # vcf2_kicks2[j] += vcf2_kicks[k]
        # vcf1_kicks2[j] += vcf1_kicks[k]

        dvcf8_kicks2[j] += dvcf8_kicks[k]
        # dvcf7_kicks2[j] += dvcf7_kicks[k]
        # dvcf6_kicks2[j] += dvcf6_kicks[k]
        # dvcf5_kicks2[j] += dvcf5_kicks[k]
        # dvcf4_kicks2[j] += dvcf4_kicks[k]
        # dvcf3_kicks2[j] += dvcf3_kicks[k]
        # dvcf2_kicks2[j] += dvcf2_kicks[k]
        # dvcf1_kicks2[j] += dvcf1_kicks[k]

        k += 20

count_cf = [0 for i in range(20)]
# count_vcf7 = [0 for i in range(20)]
# count_vcf6 = [0 for i in range(20)]
# count_vcf5 = [0 for i in range(20)]
# count_vcf4 = [0 for i in range(20)]
# count_vcf3 = [0 for i in range(20)]
# count_vcf2 = [0 for i in range(20)]
# count_vcf1 = [0 for i in range(20)]

count_dvcf8 = [0 for i in range(20)]
# count_dvcf7 = [0 for i in range(20)]
# count_dvcf6 = [0 for i in range(20)]
# count_dvcf5 = [0 for i in range(20)]
# count_dvcf4 = [0 for i in range(20)]
# count_dvcf3 = [0 for i in range(20)]
# count_dvcf2 = [0 for i in range(20)]
# count_dvcf1 = [0 for i in range(20)]

for j in range(20):
    k = j
    for i in range(cishu):
        if cf_insert_thp[k] == 0:
            count_cf[j] += 1

        # if vcf7_insert_thp[k] == 0:
        #     count_vcf7[j] += 1
        # if vcf6_insert_thp[k] == 0:
        #     count_vcf6[j] += 1
        # if vcf5_insert_thp[k] == 0:
        #     count_vcf5[j] += 1
        # if vcf4_insert_thp[k] == 0:
        #     count_vcf4[j] += 1
        # if vcf3_insert_thp[k] == 0:
        #     count_vcf3[j] += 1
        # if vcf2_insert_thp[k] == 0:
        #     count_vcf2[j] += 1
        # if vcf1_insert_thp[k] == 0:
        #     count_vcf1[j] += 1

        if dvcf8_insert_thp[k] == 0:
            count_dvcf8[j] += 1
        # if dvcf7_insert_thp[k] == 0:
        #     count_dvcf7[j] += 1
        # if dvcf6_insert_thp[k] == 0:
        #     count_dvcf6[j] += 1
        # if dvcf5_insert_thp[k] == 0:
        #     count_dvcf5[j] += 1
        # if dvcf4_insert_thp[k] == 0:
        #     count_dvcf4[j] += 1
        # if dvcf3_insert_thp[k] == 0:
        #     count_dvcf3[j] += 1
        # if dvcf2_insert_thp[k] == 0:
        #     count_dvcf2[j] += 1
        # if dvcf1_insert_thp[k] == 0:
        #     count_dvcf1[j] += 1

        k += 20

print("count_cf为：", count_cf)
# print("count_vcf7为：", count_vcf7)
# print("count_vcf6为：", count_vcf6)
# print("count_vcf5为：", count_vcf5)
# print("count_vcf4为：", count_vcf4)
# print("count_vcf3为：", count_vcf3)
# print("count_vcf2为：", count_vcf2)
# print("count_vcf1为：", count_vcf1)

print("count_dvcf8为：", count_dvcf8)
# print("count_dvcf7为：", count_dvcf7)
# print("count_dvcf6为：", count_dvcf6)
# print("count_dvcf5为：", count_dvcf5)
# print("count_dvcf4为：", count_dvcf4)
# print("count_dvcf3为：", count_dvcf3)
# print("count_dvcf2为：", count_dvcf2)
# print("count_dvcf1为：", count_dvcf1)

for j in range(20):
    cf_insert_thp2[j] = cf_insert_thp2[j] / (cishu - count_cf[j])

    # vcf7_insert_thp2[j] = vcf7_insert_thp2[j] / (cishu - count_vcf7[j])
    # vcf6_insert_thp2[j] = vcf6_insert_thp2[j] / (cishu - count_vcf6[j])
    # vcf5_insert_thp2[j] = vcf5_insert_thp2[j] / (cishu - count_vcf5[j])
    # vcf4_insert_thp2[j] = vcf4_insert_thp2[j] / (cishu - count_vcf4[j])
    # vcf3_insert_thp2[j] = vcf3_insert_thp2[j] / (cishu - count_vcf3[j])
    # vcf2_insert_thp2[j] = vcf2_insert_thp2[j] / (cishu - count_vcf2[j])
    # vcf1_insert_thp2[j] = vcf1_insert_thp2[j] / (cishu - count_vcf1[j])

    dvcf8_insert_thp2[j] = dvcf8_insert_thp2[j] / (cishu - count_dvcf8[j])
    # dvcf7_insert_thp2[j] = dvcf7_insert_thp2[j] / (cishu - count_dvcf7[j])
    # dvcf6_insert_thp2[j] = dvcf6_insert_thp2[j] / (cishu - count_dvcf6[j])
    # dvcf5_insert_thp2[j] = dvcf5_insert_thp2[j] / (cishu - count_dvcf5[j])
    # dvcf4_insert_thp2[j] = dvcf4_insert_thp2[j] / (cishu - count_dvcf4[j])
    # dvcf3_insert_thp2[j] = dvcf3_insert_thp2[j] / (cishu - count_dvcf3[j])
    # dvcf2_insert_thp2[j] = dvcf2_insert_thp2[j] / (cishu - count_dvcf2[j])
    # dvcf1_insert_thp2[j] = dvcf1_insert_thp2[j] / (cishu - count_dvcf1[j])

for j in range(20):
    cf_kicks2[j] = cf_kicks2[j] / cishu

    # vcf7_kicks2[j] = vcf7_kicks2[j] / cishu
    # vcf6_kicks2[j] = vcf6_kicks2[j] / cishu
    # vcf5_kicks2[j] = vcf5_kicks2[j] / cishu
    # vcf4_kicks2[j] = vcf4_kicks2[j] / cishu
    # vcf3_kicks2[j] = vcf3_kicks2[j] / cishu
    # vcf2_kicks2[j] = vcf2_kicks2[j] / cishu
    # vcf1_kicks2[j] = vcf1_kicks2[j] / cishu

    dvcf8_kicks2[j] = dvcf8_kicks2[j] / cishu
    # dvcf7_kicks2[j] = dvcf7_kicks2[j] / cishu
    # dvcf6_kicks2[j] = dvcf6_kicks2[j] / cishu
    # dvcf5_kicks2[j] = dvcf5_kicks2[j] / cishu
    # dvcf4_kicks2[j] = dvcf4_kicks2[j] / cishu
    # dvcf3_kicks2[j] = dvcf3_kicks2[j] / cishu
    # dvcf2_kicks2[j] = dvcf2_kicks2[j] / cishu
    # dvcf1_kicks2[j] = dvcf1_kicks2[j] / cishu

print("##############实验结果###############")
print("不同空间利用率下的插入吞吐量")
print("insert thp of cf", cf_insert_thp2)
# print("insert thp of vcf7", vcf7_insert_thp2)
# print("insert thp of vcf6", vcf6_insert_thp2)
# print("insert thp of vcf5", vcf5_insert_thp2)
# print("insert thp of vcf4", vcf4_insert_thp2)
# print("insert thp of vcf3", vcf3_insert_thp2)
# print("insert thp of vcf2", vcf2_insert_thp2)
# print("insert thp of vcf1", vcf1_insert_thp2)

print("insert thp of dvcf8", dvcf8_insert_thp2)
# print("insert thp of dvcf7", dvcf7_insert_thp2)
# print("insert thp of dvcf6", dvcf6_insert_thp2)
# print("insert thp of dvcf5", dvcf5_insert_thp2)
# print("insert thp of dvcf4", dvcf4_insert_thp2)
# print("insert thp of dvcf3", dvcf3_insert_thp2)
# print("insert thp of dvcf2", dvcf2_insert_thp2)
# print("insert thp of dvcf1", dvcf1_insert_thp2)

# print("   ")
# print("   ")
# print("   ")
# print("不同空间利用率下的踢出重放次数总数")
print("kicks of cf", cf_kicks2)
# print("kicks of vcf7", vcf7_kicks2)
# print("kicks of vcf6", vcf6_kicks2)
# print("kicks of vcf5", vcf5_kicks2)
# print("kicks of vcf4", vcf4_kicks2)
# print("kicks of vcf3", vcf3_kicks2)
# print("kicks of vcf2", vcf2_kicks2)
# print("kicks of vcf1", vcf1_kicks2)

print("kicks of dvcf8", dvcf8_kicks2)
# print("kicks of dvcf7", dvcf7_kicks2)
# print("kicks of dvcf6", dvcf6_kicks2)
# print("kicks of dvcf5", dvcf5_kicks2)
# print("kicks of dvcf4", dvcf4_kicks2)
# print("kicks of dvcf3", dvcf3_kicks2)
# print("kicks of dvcf2", dvcf2_kicks2)
# print("kicks of dvcf1", dvcf1_kicks2)
