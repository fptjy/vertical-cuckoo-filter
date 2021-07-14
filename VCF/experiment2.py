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

number = 10

#存储结果

cf_alpha_result = []
cf_time_result = []
kcf = []

vcf7_alpha_result = []
vcf7_time_result = []
kvcf7 = []

vcf6_alpha_result = []
vcf6_time_result = []
kvcf6 = []

vcf5_alpha_result = []
vcf5_time_result = []
kvcf5 = []

vcf4_alpha_result = []
vcf4_time_result = []
kvcf4 = []

vcf3_alpha_result = []
vcf3_time_result = []
kvcf3 = []

vcf2_alpha_result = []
vcf2_time_result = []
kvcf2 = []

vcf1_alpha_result = []
vcf1_time_result = []
kvcf1 = []

D_vcf1_alpha_result = []
D_vcf1_time_result = []
kD_vcf1_result_mean = []

D_vcf2_alpha_result = []
D_vcf2_time_result = []
kD_vcf2_result_mean = []

D_vcf3_alpha_result = []
D_vcf3_time_result = []
kD_vcf3_result_mean = []

D_vcf4_alpha_result = []
D_vcf4_time_result = []
kD_vcf4_result_mean = []

D_vcf5_alpha_result = []
D_vcf5_time_result = []
kD_vcf5_result_mean = []

D_vcf6_alpha_result = []
D_vcf6_time_result = []
kD_vcf6_result_mean = []

D_vcf7_alpha_result = []
D_vcf7_time_result = []
kD_vcf7_result_mean = []

D_vcf8_alpha_result = []
D_vcf8_time_result = []
kD_vcf8_result_mean = []

fingersize = 14
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = [2 ** 10, 2 ** 11, 2 ** 12, 2 ** 13, 2 ** 14, 2 ** 15, 2 ** 16, 2 ** 17, 2 ** 18, 2 ** 19, 2 ** 20, 2 ** 21,
             2 ** 22, 2 ** 23]

##CF进行十次实验取均值
cf_space_overhead = []
cf_time_overhead = []
kcf_mean = []

vcf7_space_overhead = []
vcf7_time_overhead = []
kvcf7_mean = []

vcf6_space_overhead = []
vcf6_time_overhead = []
kvcf6_mean = []

vcf5_space_overhead = []
vcf5_time_overhead = []
kvcf5_mean = []

vcf4_space_overhead = []
vcf4_time_overhead = []
kvcf4_mean = []

vcf3_space_overhead = []
vcf3_time_overhead = []
kvcf3_mean = []

vcf2_space_overhead = []
vcf2_time_overhead = []
kvcf2_mean = []

vcf1_space_overhead = []
vcf1_time_overhead = []
kvcf1_mean = []

D_vcf1_space_overhead = []
D_vcf1_time_overhead = []
kD_vcf1 = []

D_vcf2_space_overhead = []
D_vcf2_time_overhead = []
kD_vcf2 = []

D_vcf3_space_overhead = []
D_vcf3_time_overhead = []
kD_vcf3 = []

D_vcf4_space_overhead = []
D_vcf4_time_overhead = []
kD_vcf4 = []

D_vcf5_space_overhead = []
D_vcf5_time_overhead = []
kD_vcf5 = []

D_vcf6_space_overhead = []
D_vcf6_time_overhead = []
kD_vcf6 = []

D_vcf7_space_overhead = []
D_vcf7_time_overhead = []
kD_vcf7 = []

D_vcf8_space_overhead = []
D_vcf8_time_overhead = []
kD_vcf8 = []


for j in range(len(capacity1)):
    for num in range(number):
        testdata1 = random.sample(raw_data, capacity1[j])

        cf = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            cf.I_insert0(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time_ms = (end - start).microseconds
        time_s = (end - start).seconds
        load_factor = cf.size / capacity1[j]
        k = cf.kicks / capacity1[j]

        cf_space_overhead.append(load_factor)
        cf_time_overhead.append(time_s + time_ms / 10 ** 6)
        kcf.append(k)


        vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv7 = vcf7.size / capacity1[j]
        k7 = vcf7.kicks / capacity1[j]
        vcf7_space_overhead.append(load_factorv7)
        vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf7.append(k7)


        vcf6 = VCuckooFilter14_6(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf6.I_insert6(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv6 = vcf6.size / capacity1[j]
        k6 = vcf6.kicks / capacity1[j]
        vcf6_space_overhead.append(load_factorv6)
        vcf6_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf6.append(k6)


        vcf5 = VCuckooFilter14_5(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf5.I_insert5(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv5 = vcf5.size / capacity1[j]
        k5 = vcf5.kicks / capacity1[j]
        vcf5_space_overhead.append(load_factorv5)
        vcf5_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf5.append(k5)


        vcf4 = VCuckooFilter14_4(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf4.I_insert4(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv4 = vcf4.size / capacity1[j]
        k4 = vcf4.kicks / capacity1[j]
        vcf4_space_overhead.append(load_factorv4)
        vcf4_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf4.append(k4)


        vcf3 = VCuckooFilter14_3(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf3.I_insert3(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv3 = vcf3.size / capacity1[j]
        k3 = vcf3.kicks / capacity1[j]
        vcf3_space_overhead.append(load_factorv3)
        vcf3_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf3.append(k3)


        vcf2 = VCuckooFilter14_2(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf2.I_insert2(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv2 = vcf2.size / capacity1[j]
        k2 = vcf2.kicks / capacity1[j]
        vcf2_space_overhead.append(load_factorv2)
        vcf2_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf2.append(k2)


        vcf1 = VCuckooFilter14_1(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf1.I_insert1(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factorv1 = vcf1.size / capacity1[j]
        k1 = vcf1.kicks / capacity1[j]
        vcf1_space_overhead.append(load_factorv1)
        vcf1_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kvcf1.append(k1)


        D_vcf1 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf1.D_insert(testdata1[i], 2**13*(1-0.125), 2**13*(1+0.125))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf1 = D_vcf1.size / capacity1[j]
        k = D_vcf1.kicks / capacity1[j]
        D_vcf1_space_overhead.append(load_factor_D_vcf1)
        D_vcf1_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf1.append(k)


        D_vcf2 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf2.D_insert(testdata1[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf2 = D_vcf2.size / capacity1[j]
        k = D_vcf2.kicks / capacity1[j]
        D_vcf2_space_overhead.append(load_factor_D_vcf2)
        D_vcf2_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf2.append(k)


        D_vcf3 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf3.D_insert(testdata1[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf3 = D_vcf3.size / capacity1[j]
        k = D_vcf3.kicks / capacity1[j]
        D_vcf3_space_overhead.append(load_factor_D_vcf3)
        D_vcf3_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf3.append(k)


        D_vcf4 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf4.D_insert(testdata1[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf4 = D_vcf4.size / capacity1[j]
        k = D_vcf4.kicks / capacity1[j]
        D_vcf4_space_overhead.append(load_factor_D_vcf4)
        D_vcf4_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf4.append(k)


        D_vcf5 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf5.D_insert(testdata1[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf5 = D_vcf5.size / capacity1[j]
        k = D_vcf5.kicks / capacity1[j]
        D_vcf5_space_overhead.append(load_factor_D_vcf5)
        D_vcf5_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf5.append(k)


        D_vcf6 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf6.D_insert(testdata1[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf6 = D_vcf6.size / capacity1[j]
        k = D_vcf6.kicks / capacity1[j]
        D_vcf6_space_overhead.append(load_factor_D_vcf6)
        D_vcf6_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf6.append(k)


        D_vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf7.D_insert(testdata1[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf7 = D_vcf7.size / capacity1[j]
        k = D_vcf7.kicks / capacity1[j]
        D_vcf7_space_overhead.append(load_factor_D_vcf7)
        D_vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf7.append(k)


        D_vcf8 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)

        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            D_vcf8.D_insert(testdata1[i], 0, 2 ** 14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds

        load_factor_D_vcf8 = D_vcf8.size / capacity1[j]
        k = D_vcf8.kicks / capacity1[j]
        D_vcf8_space_overhead.append(load_factor_D_vcf8)
        D_vcf8_time_overhead.append(timev_s + timev_ms / 10 ** 6)
        kD_vcf8.append(k)

    x1 = np.mean(cf_space_overhead)
    cf_alpha_result.append(x1)
    y1 = np.mean(cf_time_overhead)
    cf_time_result.append(y1)
    kcf_mean.append(np.mean(kcf))

    x2 = np.mean(vcf7_space_overhead)
    vcf7_alpha_result.append(x2)
    y2 = np.mean(vcf7_time_overhead)
    vcf7_time_result.append(y2)
    kvcf7_mean.append(np.mean(kvcf7))

    x2 = np.mean(vcf6_space_overhead)
    vcf6_alpha_result.append(x2)
    y2 = np.mean(vcf6_time_overhead)
    vcf6_time_result.append(y2)
    kvcf6_mean.append(np.mean(kvcf6))

    x2 = np.mean(vcf5_space_overhead)
    vcf5_alpha_result.append(x2)
    y2 = np.mean(vcf5_time_overhead)
    vcf5_time_result.append(y2)
    kvcf5_mean.append(np.mean(kvcf5))

    x2 = np.mean(vcf4_space_overhead)
    vcf4_alpha_result.append(x2)
    y2 = np.mean(vcf4_time_overhead)
    vcf4_time_result.append(y2)
    kvcf4_mean.append(np.mean(kvcf4))

    x2 = np.mean(vcf3_space_overhead)
    vcf3_alpha_result.append(x2)
    y2 = np.mean(vcf3_time_overhead)
    vcf3_time_result.append(y2)
    kvcf3_mean.append(np.mean(kvcf3))

    x2 = np.mean(vcf2_space_overhead)
    vcf2_alpha_result.append(x2)
    y2 = np.mean(vcf2_time_overhead)
    vcf2_time_result.append(y2)
    kvcf2_mean.append(np.mean(kvcf2))

    x2 = np.mean(vcf1_space_overhead)
    vcf1_alpha_result.append(x2)
    y2 = np.mean(vcf1_time_overhead)
    vcf1_time_result.append(y2)
    kvcf1_mean.append(np.mean(kvcf1))

    x2 = np.mean(D_vcf1_space_overhead)
    D_vcf1_alpha_result.append(x2)
    y2 = np.mean(D_vcf1_time_overhead)
    D_vcf1_time_result.append(y2)
    kD_vcf1_result_mean.append(np.mean(kD_vcf1))

    x2 = np.mean(D_vcf2_space_overhead)
    D_vcf2_alpha_result.append(x2)
    y2 = np.mean(D_vcf2_time_overhead)
    D_vcf2_time_result.append(y2)
    kD_vcf2_result_mean.append(np.mean(kD_vcf2))

    x2 = np.mean(D_vcf3_space_overhead)
    D_vcf3_alpha_result.append(x2)
    y2 = np.mean(D_vcf3_time_overhead)
    D_vcf3_time_result.append(y2)
    kD_vcf3_result_mean.append(np.mean(kD_vcf3))

    x2 = np.mean(D_vcf4_space_overhead)
    D_vcf4_alpha_result.append(x2)
    y2 = np.mean(D_vcf4_time_overhead)
    D_vcf4_time_result.append(y2)
    kD_vcf4_result_mean.append(np.mean(kD_vcf4))

    x2 = np.mean(D_vcf5_space_overhead)
    D_vcf5_alpha_result.append(x2)
    y2 = np.mean(D_vcf5_time_overhead)
    D_vcf5_time_result.append(y2)
    kD_vcf5_result_mean.append(np.mean(kD_vcf5))

    x2 = np.mean(D_vcf6_space_overhead)
    D_vcf6_alpha_result.append(x2)
    y2 = np.mean(D_vcf6_time_overhead)
    D_vcf6_time_result.append(y2)
    kD_vcf6_result_mean.append(np.mean(kD_vcf6))

    x2 = np.mean(D_vcf7_space_overhead)
    D_vcf7_alpha_result.append(x2)
    y2 = np.mean(D_vcf7_time_overhead)
    D_vcf7_time_result.append(y2)
    kD_vcf7_result_mean.append(np.mean(kD_vcf7))

    x2 = np.mean(D_vcf8_space_overhead)
    D_vcf8_alpha_result.append(x2)
    y2 = np.mean(D_vcf8_time_overhead)
    D_vcf8_time_result.append(y2)
    kD_vcf8_result_mean.append(np.mean(kD_vcf8))


print("cf")
print(cf_alpha_result)
print(cf_time_result)
print(kcf_mean)
print("   ")
print("   ")

print("vcf7")
print(vcf7_alpha_result)
print(vcf7_time_result)
print(kvcf7_mean)
print("   ")
print("   ")

print("vcf6")
print(vcf6_alpha_result)
print(vcf6_time_result)
print(kvcf6_mean)
print("   ")
print("   ")

print("vcf5")
print(vcf5_alpha_result)
print(vcf5_time_result)
print(kvcf5_mean)
print("   ")
print("   ")

print("vcf4")
print(vcf4_alpha_result)
print(vcf4_time_result)
print(kvcf4_mean)
print("   ")
print("   ")

print("vcf3")
print(vcf3_alpha_result)
print(vcf3_time_result)
print(kvcf3_mean)
print("   ")
print("   ")

print("vcf2")
print(vcf2_alpha_result)
print(vcf2_time_result)
print(kvcf2_mean)
print("   ")
print("   ")

print("vcf1")
print(vcf1_alpha_result)
print(vcf1_time_result)
print(kvcf1_mean)
print("   ")
print("   ")

print("D_vcf1")
print(D_vcf1_alpha_result)
print(D_vcf1_time_result)
print(kD_vcf1_result_mean)
print("   ")
print("   ")

print("D_vcf2")
print(D_vcf2_alpha_result)
print(D_vcf2_time_result)
print(kD_vcf2_result_mean)
print("   ")
print("   ")

print("D_vcf3")
print(D_vcf3_alpha_result)
print(D_vcf3_time_result)
print(kD_vcf3_result_mean)
print("   ")
print("   ")

print("D_vcf4")
print(D_vcf4_alpha_result)
print(D_vcf4_time_result)
print(kD_vcf4_result_mean)
print("   ")
print("   ")

print("D_vcf5")
print(D_vcf5_alpha_result)
print(D_vcf5_time_result)
print(kD_vcf5_result_mean)
print("   ")
print("   ")

print("D_vcf6")
print(D_vcf6_alpha_result)
print(D_vcf6_time_result)
print(kD_vcf6_result_mean)
print("   ")
print("   ")

print("D_vcf7")
print(D_vcf7_alpha_result)
print(D_vcf7_time_result)
print(kD_vcf7_result_mean)
print("   ")
print("   ")

print("D_vcf8")
print(D_vcf8_alpha_result)
print(D_vcf8_time_result)
print(kD_vcf8_result_mean)
print("   ")
print("   ")