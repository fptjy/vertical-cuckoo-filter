import random
from random import randint
import datetime
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

number = 50

#存储结果
cf_time_overhead_100 = []
cf_time_result_100 = []
cf_time_overhead_50 = []
cf_time_result_50 = []

vcf7_time_overhead_100 = []
vcf7_time_result_100 = []
vcf7_time_overhead_50 = []
vcf7_time_result_50 = []

vcf6_time_overhead_100 = []
vcf6_time_result_100 = []
vcf6_time_overhead_50 = []
vcf6_time_result_50 = []

vcf5_time_overhead_100 = []
vcf5_time_result_100 = []
vcf5_time_overhead_50 = []
vcf5_time_result_50 = []

vcf4_time_overhead_100 = []
vcf4_time_result_100 = []
vcf4_time_overhead_50 = []
vcf4_time_result_50 = []

vcf3_time_overhead_100 = []
vcf3_time_result_100 = []
vcf3_time_overhead_50 = []
vcf3_time_result_50 = []

vcf2_time_overhead_100 = []
vcf2_time_result_100 = []
vcf2_time_overhead_50 = []
vcf2_time_result_50 = []

vcf1_time_overhead_100 = []
vcf1_time_result_100 = []
vcf1_time_overhead_50 = []
vcf1_time_result_50 = []

D_vcf1_time_overhead_100 = []
D_vcf1_time_result_100 = []
D_vcf1_time_overhead_50 = []
D_vcf1_time_result_50 = []

D_vcf2_time_overhead_100 = []
D_vcf2_time_result_100 = []
D_vcf2_time_overhead_50 = []
D_vcf2_time_result_50 = []

D_vcf3_time_overhead_100 = []
D_vcf3_time_result_100 = []
D_vcf3_time_overhead_50 = []
D_vcf3_time_result_50 = []

D_vcf4_time_overhead_100 = []
D_vcf4_time_result_100 = []
D_vcf4_time_overhead_50 = []
D_vcf4_time_result_50 = []

D_vcf5_time_overhead_100 = []
D_vcf5_time_result_100 = []
D_vcf5_time_overhead_50 = []
D_vcf5_time_result_50 = []

D_vcf6_time_overhead_100 = []
D_vcf6_time_result_100 = []
D_vcf6_time_overhead_50 = []
D_vcf6_time_result_50 = []

D_vcf7_time_overhead_100 = []
D_vcf7_time_result_100 = []
D_vcf7_time_overhead_50 = []
D_vcf7_time_result_50 = []

D_vcf8_time_overhead_100 = []
D_vcf8_time_result_100 = []
D_vcf8_time_overhead_50 = []
D_vcf8_time_result_50 = []


fingersize = 14
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 20
##设置参数
capacity1 = [2 ** 20]

for j in range(len(capacity1)):
    for num in range(number):
        testdata1 = random.sample(raw_data, capacity1[j])

        #构造50%mixed的数据
        list1 = list(set(raw_data) - set(testdata1))
        list2 = random.sample(list1, capacity1[j] // 2)
        list3 = random.sample(testdata1, capacity1[j] // 2)
        list4 = list2 + list3
        testdata2 = random.sample(list4, capacity1[j])


        cf = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            cf.I_insert0(testdata1[i])

        #进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            cf.I_contains0(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        cf_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            cf.I_contains0(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        cf_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf7.I_insert7(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf7.I_contains7(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf7_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf7.I_contains7(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf7_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf6 = VCuckooFilter14_6(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf6.I_insert6(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf6.I_contains6(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf6_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf6.I_contains6(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf6_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf5 = VCuckooFilter14_5(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf5.I_insert5(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf5.I_contains5(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf5_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf5.I_contains5(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf5_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf4 = VCuckooFilter14_4(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf4.I_insert4(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf4.I_contains4(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf4_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf4.I_contains4(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf4_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf3 = VCuckooFilter14_3(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf3.I_insert3(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf3.I_contains3(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf3_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf3.I_contains3(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf3_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf2 = VCuckooFilter14_2(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf2.I_insert2(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf2.I_contains2(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf2_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf2.I_contains2(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf2_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        Vcf1 = VCuckooFilter14_1(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf1.I_insert1(testdata1[i])

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf1.I_contains1(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf1_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Vcf1.I_contains1(testdata2[i])
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        vcf1_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])



        D_vcf1 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf1.D_insert(testdata1[i], 2**13*(1-0.125), 2**13*(1+0.125))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf1.D_contains(testdata1[i], 2**13*(1-0.125), 2**13*(1+0.125))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf1_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf1.D_contains(testdata2[i], 2**13*(1-0.125), 2**13*(1+0.125))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf1_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf2 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf2.D_insert(testdata1[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf2.D_contains(testdata1[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf2_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf2.D_contains(testdata2[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf2_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf3 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf3.D_insert(testdata1[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf3.D_contains(testdata1[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf3_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf3.D_contains(testdata2[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf3_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf4 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf4.D_insert(testdata1[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf4.D_contains(testdata1[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf4_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf4.D_contains(testdata2[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf4_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf5 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf5.D_insert(testdata1[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf5.D_contains(testdata1[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf5_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf5.D_contains(testdata2[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf5_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf6 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf6.D_insert(testdata1[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf6.D_contains(testdata1[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf6_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf6.D_contains(testdata2[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf6_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf7.D_insert(testdata1[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf7.D_contains(testdata1[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf7_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf7.D_contains(testdata2[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf7_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])


        D_vcf8 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf8.D_insert(testdata1[i], 0, 2 ** 14)

        # 进行100%existed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf8.D_contains(testdata1[i], 0, 2 ** 14)
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf8_time_overhead_100.append((time2 + time1 / 10 ** 6) / capacity1[j])

        # 进行50%mixed的对象查询实验
        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf8.D_contains(testdata2[i], 0, 2 ** 14)
        end = datetime.datetime.now()  # 结束时间
        time1 = (end - start).microseconds
        time2 = (end - start).seconds
        D_vcf8_time_overhead_50.append((time2 + time1 / 10 ** 6) / capacity1[j])



    cf_time_result_100.append(np.mean(cf_time_overhead_100))
    cf_time_result_50.append(np.mean(cf_time_overhead_50))

    vcf7_time_result_100.append(np.mean(vcf7_time_overhead_100))
    vcf7_time_result_50.append(np.mean(vcf7_time_overhead_50))

    vcf6_time_result_100.append(np.mean(vcf6_time_overhead_100))
    vcf6_time_result_50.append(np.mean(vcf6_time_overhead_50))

    vcf5_time_result_100.append(np.mean(vcf5_time_overhead_100))
    vcf5_time_result_50.append(np.mean(vcf5_time_overhead_50))

    vcf4_time_result_100.append(np.mean(vcf4_time_overhead_100))
    vcf4_time_result_50.append(np.mean(vcf4_time_overhead_50))

    vcf3_time_result_100.append(np.mean(vcf3_time_overhead_100))
    vcf3_time_result_50.append(np.mean(vcf3_time_overhead_50))

    vcf2_time_result_100.append(np.mean(vcf2_time_overhead_100))
    vcf2_time_result_50.append(np.mean(vcf2_time_overhead_50))

    vcf1_time_result_100.append(np.mean(vcf1_time_overhead_100))
    vcf1_time_result_50.append(np.mean(vcf1_time_overhead_50))

    D_vcf1_time_result_100.append(np.mean(D_vcf1_time_overhead_100))
    D_vcf1_time_result_50.append(np.mean(D_vcf1_time_overhead_50))

    D_vcf2_time_result_100.append(np.mean(D_vcf2_time_overhead_100))
    D_vcf2_time_result_50.append(np.mean(D_vcf2_time_overhead_50))

    D_vcf3_time_result_100.append(np.mean(D_vcf3_time_overhead_100))
    D_vcf3_time_result_50.append(np.mean(D_vcf3_time_overhead_50))

    D_vcf4_time_result_100.append(np.mean(D_vcf4_time_overhead_100))
    D_vcf4_time_result_50.append(np.mean(D_vcf4_time_overhead_50))

    D_vcf5_time_result_100.append(np.mean(D_vcf5_time_overhead_100))
    D_vcf5_time_result_50.append(np.mean(D_vcf5_time_overhead_50))

    D_vcf6_time_result_100.append(np.mean(D_vcf6_time_overhead_100))
    D_vcf6_time_result_50.append(np.mean(D_vcf6_time_overhead_50))

    D_vcf7_time_result_100.append(np.mean(D_vcf7_time_overhead_100))
    D_vcf7_time_result_50.append(np.mean(D_vcf7_time_overhead_50))

    D_vcf8_time_result_100.append(np.mean(D_vcf8_time_overhead_100))
    D_vcf8_time_result_50.append(np.mean(D_vcf8_time_overhead_50))

print("cf")
print("100%查询结果")
print(cf_time_result_100)
print("50%mixed查询结果")
print(cf_time_result_50)
print("   ")
print("   ")

print("Vcf7")
print("100%查询结果")
print(vcf7_time_result_100)
print("50%mixed查询结果")
print(vcf7_time_result_50)
print("   ")
print("   ")

print("Vcf6")
print("100%查询结果")
print(vcf6_time_result_100)
print("50%mixed查询结果")
print(vcf6_time_result_50)
print("   ")
print("   ")

print("Vcf5")
print("100%查询结果")
print(vcf5_time_result_100)
print("50%mixed查询结果")
print(vcf5_time_result_50)
print("   ")
print("   ")

print("Vcf4")
print("100%查询结果")
print(vcf4_time_result_100)
print("50%mixed查询结果")
print(vcf4_time_result_50)
print("   ")
print("   ")

print("Vcf3")
print("100%查询结果")
print(vcf3_time_result_100)
print("50%mixed查询结果")
print(vcf3_time_result_50)
print("   ")
print("   ")

print("Vcf2")
print("100%查询结果")
print(vcf2_time_result_100)
print("50%mixed查询结果")
print(vcf2_time_result_50)
print("   ")
print("   ")

print("Vcf1")
print("100%查询结果")
print(vcf1_time_result_100)
print("50%mixed查询结果")
print(vcf1_time_result_50)
print("   ")
print("   ")

print("D_vcf1")
print("100%查询结果")
print(D_vcf1_time_result_100)
print("50%mixed查询结果")
print(D_vcf1_time_result_50)
print("   ")
print("   ")

print("D_vcf2")
print("100%查询结果")
print(D_vcf2_time_result_100)
print("50%mixed查询结果")
print(D_vcf2_time_result_50)
print("   ")
print("   ")

print("D_vcf3")
print("100%查询结果")
print(D_vcf3_time_result_100)
print("50%mixed查询结果")
print(D_vcf3_time_result_50)
print("   ")
print("   ")

print("D_vcf4")
print("100%查询结果")
print(D_vcf4_time_result_100)
print("50%mixed查询结果")
print(D_vcf4_time_result_50)
print("   ")
print("   ")

print("D_vcf5")
print("100%查询结果")
print(D_vcf5_time_result_100)
print("50%mixed查询结果")
print(D_vcf5_time_result_50)
print("   ")
print("   ")

print("D_vcf6")
print("100%查询结果")
print(D_vcf6_time_result_100)
print("50%mixed查询结果")
print(D_vcf6_time_result_50)
print("   ")
print("   ")

print("D_vcf7")
print("100%查询结果")
print(D_vcf7_time_result_100)
print("50%mixed查询结果")
print(D_vcf7_time_result_50)
print("   ")
print("   ")

print("D_vcf8")
print("100%查询结果")
print(D_vcf8_time_result_100)
print("50%mixed查询结果")
print(D_vcf8_time_result_50)
print("   ")
print("   ")
