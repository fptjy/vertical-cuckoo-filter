import random
from Vcuckoofilter import VCuckooFilter
from random import randint
from cuckoofilter import CuckooFilter
import datetime
import numpy as np

raw_data = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
    for line in fin:
        raw_data.append(line.replace(",\n", ""))
fin.close()

number = 10

#存储结果

cf_alpha_result = []
cf_time_result = []

vcf_alpha_result = []
vcf_time_result = []


cf_space_overhead = []
cf_time_overhead = []

vcf_space_overhead = []
vcf_time_overhead = []

fingersize = 16
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 20
##设置参数
capacity1 = [2 ** 20]


for j in range(len(capacity1)):
    for num in range(number):
        testdata1 = random.sample(raw_data, capacity1[j])

        cf = VCuckooFilter(capacity=capacity1[j] // 1, bucket_size=1, fingerprint_size=fingersize)

        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            cf.insert1(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time_ms = (end - start).microseconds
        time_s = (end - start).seconds
        load_factor = cf.size / capacity1[j]

        cf_space_overhead.append(load_factor)
        cf_time_overhead.append(time_s + time_ms / 10 ** 6)


        vcf = VCuckooFilter(capacity=capacity1[j] // 1, bucket_size=1, fingerprint_size=fingersize)

        start = datetime.datetime.now()  # 开始时间
        for i in range(capacity1[j]):
            vcf.insert2(testdata1[i])
        end = datetime.datetime.now()  # 结束时间
        time_ms = (end - start).microseconds
        time_s = (end - start).seconds
        load_factor = vcf.size / capacity1[j]

        vcf_space_overhead.append(load_factor)
        vcf_time_overhead.append(time_s + time_ms / 10 ** 6)

    cf_alpha_result.append(np.mean(cf_space_overhead))
    cf_time_result.append(np.mean(cf_time_overhead))

    vcf_alpha_result.append(np.mean(vcf_space_overhead))
    vcf_time_result.append(np.mean(vcf_time_overhead))


print("cf")
print(cf_alpha_result)
print(cf_time_result)
print("   ")
print("   ")

print("vcf")
print(vcf_alpha_result)
print(vcf_time_result)
print("   ")
print("   ")