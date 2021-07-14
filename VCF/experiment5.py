import random
from random import randint
import datetime
import numpy as np


from Vcuckoofilter14_7_builtin import VCuckooFilter14_7_builtin
from Vcuckoofilter14_7_murmurhash import VCuckooFilter14_7_murmurhash
from Vcuckoofilter14_7_DJBhash import VCuckooFilter14_7_DJBhash
from Vcuckoofilter14_7_PJWhash import VCuckooFilter14_7_PJWhash
from Vcuckoofilter14_7 import VCuckooFilter14_7


raw_data = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
    for line in fin:
        raw_data.append(line.replace(",\n", ""))
fin.close()

number = 10

#存储结果


fingersize = 14
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = [2 ** 20]

##CF进行十次实验取均值
cf7_time_result = []
cf7_time_overhead = []
vcf7_time_result = []
vcf7_time_overhead = []
Dvcf7_time_result = []
Dvcf7_time_overhead = []

h1cf7_time_result = []
h1cf7_time_overhead = []
h1vcf7_time_result = []
h1vcf7_time_overhead = []
h1Dvcf7_time_result = []
h1Dvcf7_time_overhead = []

h2cf7_time_result = []
h2cf7_time_overhead = []
h2vcf7_time_result = []
h2vcf7_time_overhead = []
h2Dvcf7_time_result = []
h2Dvcf7_time_overhead = []

h3cf7_time_result = [] #对应DJBhash
h3cf7_time_overhead = []
h3vcf7_time_result = []
h3vcf7_time_overhead = []
h3Dvcf7_time_result = []
h3Dvcf7_time_overhead = []

h4cf7_time_result = [] #对应PJWhash
h4cf7_time_overhead = []
h4vcf7_time_result = []
h4vcf7_time_overhead = []
h4Dvcf7_time_result = []
h4Dvcf7_time_overhead = []


for j in range(len(capacity1)):
    for num in range(number):
        testdata1 = random.sample(raw_data, capacity1[j])

        cf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            cf7.I_insert0(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        cf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        Dvcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            Dvcf7.D_insert(testdata1[i], 0, 2**14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        Dvcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)


        h1cf7 = VCuckooFilter14_7_builtin(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h1cf7.I_insert0(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h1cf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h1vcf7 = VCuckooFilter14_7_builtin(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h1vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h1vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h1Dvcf7 = VCuckooFilter14_7_builtin(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h1Dvcf7.D_insert(testdata1[i], 0, 2**14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h1Dvcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)


        h2cf7 = VCuckooFilter14_7_murmurhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h2cf7.I_insert0(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h2cf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h2vcf7 = VCuckooFilter14_7_murmurhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h2vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h2vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h2Dvcf7 = VCuckooFilter14_7_murmurhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h2Dvcf7.D_insert(testdata1[i], 0, 2**14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h2Dvcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)


        h3cf7 = VCuckooFilter14_7_DJBhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h3cf7.I_insert0(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h3cf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h3vcf7 = VCuckooFilter14_7_DJBhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h3vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h3vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h3Dvcf7 = VCuckooFilter14_7_DJBhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h3Dvcf7.D_insert(testdata1[i], 0, 2 ** 14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h3Dvcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)


        h4cf7 = VCuckooFilter14_7_PJWhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h4cf7.I_insert0(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h4cf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h4vcf7 = VCuckooFilter14_7_PJWhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h4vcf7.I_insert7(testdata1[i])
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h4vcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)

        h4Dvcf7 = VCuckooFilter14_7_PJWhash(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        vstart = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            h4Dvcf7.D_insert(testdata1[i], 0, 2 ** 14)
        vend = datetime.datetime.now()  # 结束时间
        timev_ms = (vend - vstart).microseconds
        timev_s = (vend - vstart).seconds
        h4Dvcf7_time_overhead.append(timev_s + timev_ms / 10 ** 6)




    cf7_time_result.append(np.mean(cf7_time_overhead))
    vcf7_time_result.append(np.mean(vcf7_time_overhead))
    Dvcf7_time_result.append(np.mean(Dvcf7_time_overhead))

    h1cf7_time_result.append(np.mean(h1cf7_time_overhead))
    h1vcf7_time_result.append(np.mean(h1vcf7_time_overhead))
    h1Dvcf7_time_result.append(np.mean(h1Dvcf7_time_overhead))

    h2cf7_time_result.append(np.mean(h2cf7_time_overhead))
    h2vcf7_time_result.append(np.mean(h2vcf7_time_overhead))
    h2Dvcf7_time_result.append(np.mean(h2Dvcf7_time_overhead))

    h3cf7_time_result.append(np.mean(h3cf7_time_overhead))
    h3vcf7_time_result.append(np.mean(h3vcf7_time_overhead))
    h3Dvcf7_time_result.append(np.mean(h3Dvcf7_time_overhead))

    h4cf7_time_result.append(np.mean(h4cf7_time_overhead))
    h4vcf7_time_result.append(np.mean(h4vcf7_time_overhead))
    h4Dvcf7_time_result.append(np.mean(h4Dvcf7_time_overhead))


print("NFV_64_vcf")
print(cf7_time_result)
print(vcf7_time_result)
print(Dvcf7_time_result)
print("   ")
print("   ")

print("builtin_md5_vcf")
print(h1cf7_time_result)
print(h1vcf7_time_result)
print(h1Dvcf7_time_result)
print("   ")
print("   ")

print("murmurhash_vcf")
print(h2cf7_time_result)
print(h2vcf7_time_result)
print(h2Dvcf7_time_result)
print("   ")
print("   ")

print("DJBhash_vcf")
print(h3cf7_time_result)
print(h3vcf7_time_result)
print(h3Dvcf7_time_result)
print("   ")
print("   ")

print("PJWhash_vcf")
print(h4cf7_time_result)
print(h4vcf7_time_result)
print(h4Dvcf7_time_result)
print("   ")
print("   ")