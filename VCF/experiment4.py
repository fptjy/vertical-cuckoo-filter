import random
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

number = 1

#存储结果

cf_fp_result = []

vcf7_fp_result = []
vcf6_fp_result = []
vcf5_fp_result = []
vcf4_fp_result = []
vcf3_fp_result = []
vcf2_fp_result = []
vcf1_fp_result = []

D_vcf8_fp_result = []
D_vcf7_fp_result = []
D_vcf6_fp_result = []
D_vcf5_fp_result = []
D_vcf4_fp_result = []
D_vcf3_fp_result = []
D_vcf2_fp_result = []
D_vcf1_fp_result = []


fingersize = 14
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 20
##设置参数
capacity1 = [2 ** 20]

for j in range(len(capacity1)):
    for num in range(number):

        # 局部变量存储查询返回True的结果数量
        cf_fp = 0
        vcf7_fp = 0
        vcf6_fp = 0
        vcf5_fp = 0
        vcf4_fp = 0
        vcf3_fp = 0
        vcf2_fp = 0
        vcf1_fp = 0
        D_vcf1_fp = 0
        D_vcf2_fp = 0
        D_vcf3_fp = 0
        D_vcf4_fp = 0
        D_vcf5_fp = 0
        D_vcf6_fp = 0
        D_vcf7_fp = 0
        D_vcf8_fp = 0

        #构造100% none existed 的数据
        testdata1 = random.sample(raw_data, capacity1[j])
        list1 = list(set(raw_data) - set(testdata1))
        testdata2 = random.sample(list1, capacity1[j])


        cf = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            cf.I_insert0(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if cf.I_contains0(testdata1[i]):
                cf_fp += 1
        cf_fp_result.append((cf_fp) / cf.size)


        Vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf7.I_insert7(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf7.I_contains7(testdata1[i]):
                vcf7_fp += 1
        vcf7_fp_result.append((vcf7_fp) / Vcf7.size)


        Vcf6 = VCuckooFilter14_6(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf6.I_insert6(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf6.I_contains6(testdata1[i]):
                vcf6_fp += 1
        vcf6_fp_result.append((vcf6_fp) / Vcf6.size)


        Vcf5 = VCuckooFilter14_5(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf5.I_insert5(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf5.I_contains5(testdata1[i]):
                vcf5_fp += 1
        vcf5_fp_result.append((vcf5_fp) / Vcf5.size)


        Vcf4 = VCuckooFilter14_4(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf4.I_insert4(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf4.I_contains4(testdata1[i]):
                vcf4_fp += 1
        vcf4_fp_result.append((vcf4_fp) / Vcf4.size)


        Vcf3 = VCuckooFilter14_3(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf3.I_insert3(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf3.I_contains3(testdata1[i]):
                vcf3_fp += 1
        vcf3_fp_result.append((vcf3_fp) / Vcf3.size)


        Vcf2 = VCuckooFilter14_2(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf2.I_insert2(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf2.I_contains2(testdata1[i]):
                vcf2_fp += 1
        vcf2_fp_result.append((vcf2_fp) / Vcf2.size)


        Vcf1 = VCuckooFilter14_1(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            Vcf1.I_insert1(testdata1[i])

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if Vcf1.I_contains1(testdata1[i]):
                vcf1_fp += 1
        vcf1_fp_result.append((vcf1_fp) / Vcf1.size)


        D_vcf1 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf1.D_insert(testdata1[i], 2**13*(1-0.125), 2**13*(1+0.125))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf1.D_contains(testdata1[i], 2**13*(1-0.125), 2**13*(1+0.125)):
                D_vcf1_fp += 1
        D_vcf1_fp_result.append((D_vcf1_fp) / D_vcf1.size)


        D_vcf2 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf2.D_insert(testdata1[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf2.D_contains(testdata1[i], 2 ** 13 * (1 - 0.25), 2 ** 13 * (1 + 0.25)):
                D_vcf2_fp += 1
        D_vcf2_fp_result.append((D_vcf2_fp) / D_vcf2.size)


        D_vcf3 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf3.D_insert(testdata1[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf3.D_contains(testdata1[i], 2 ** 13 * (1 - 0.375), 2 ** 13 * (1 + 0.375)):
                D_vcf3_fp += 1
        D_vcf3_fp_result.append((D_vcf3_fp) / D_vcf3.size)


        D_vcf4 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf4.D_insert(testdata1[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf4.D_contains(testdata1[i], 2 ** 13 * (1 - 0.5), 2 ** 13 * (1 + 0.5)):
                D_vcf4_fp += 1
        D_vcf4_fp_result.append((D_vcf4_fp) / D_vcf4.size)


        D_vcf5 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf5.D_insert(testdata1[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf5.D_contains(testdata1[i], 2 ** 13 * (1 - 0.625), 2 ** 13 * (1 + 0.625)):
                D_vcf5_fp += 1
        D_vcf5_fp_result.append((D_vcf5_fp) / D_vcf5.size)


        D_vcf6 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf6.D_insert(testdata1[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf6.D_contains(testdata1[i], 2 ** 13 * (1 - 0.75), 2 ** 13 * (1 + 0.75)):
                D_vcf6_fp += 1
        D_vcf6_fp_result.append((D_vcf6_fp) / D_vcf6.size)


        D_vcf7 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf7.D_insert(testdata1[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875))

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf7.D_contains(testdata1[i], 2 ** 13 * (1 - 0.875), 2 ** 13 * (1 + 0.875)):
                D_vcf7_fp += 1
        D_vcf7_fp_result.append((D_vcf7_fp) / D_vcf7.size)


        D_vcf8 = VCuckooFilter14_7(capacity=capacity1[j] // 4, bucket_size=4, fingerprint_size=fingersize)
        for i in range(capacity1[j]):
            D_vcf8.D_insert(testdata1[i], 0, 2 ** 14)

        #  进行100% none existed的对象查询实验，以测试假阳性
        for i in range(capacity1[j]):
            if D_vcf8.D_contains(testdata1[i], 0, 2 ** 14):
                D_vcf8_fp += 1
        D_vcf8_fp_result.append((D_vcf8_fp) / D_vcf8.size)


print("cf")
print(np.mean(cf_fp_result))
print("   ")
print("   ")

print("Vcf7")
print(np.mean(vcf7_fp_result))
print("   ")
print("   ")

print("Vcf6")
print(np.mean(vcf6_fp_result))
print("   ")
print("   ")

print("Vcf5")
print(np.mean(vcf5_fp_result))
print("   ")
print("   ")

print("Vcf4")
print(np.mean(vcf4_fp_result))
print("   ")
print("   ")

print("Vcf3")
print(np.mean(vcf3_fp_result))
print("   ")
print("   ")

print("Vcf2")
print(np.mean(vcf2_fp_result))
print("   ")
print("   ")

print("Vcf1")
print(np.mean(vcf1_fp_result))
print("   ")
print("   ")

print("D_vcf1")
print(np.mean(D_vcf1_fp_result))
print("   ")
print("   ")

print("D_vcf2")
print(np.mean(D_vcf2_fp_result))
print("   ")
print("   ")

print("D_vcf3")
print(np.mean(D_vcf3_fp_result))
print("   ")
print("   ")

print("D_vcf4")
print(np.mean(D_vcf4_fp_result))
print("   ")
print("   ")

print("D_vcf5")
print(np.mean(D_vcf5_fp_result))
print("   ")
print("   ")

print("D_vcf6")
print(np.mean(D_vcf6_fp_result))
print("   ")
print("   ")

print("D_vcf7")
print(np.mean(D_vcf7_fp_result))
print("   ")
print("   ")

print("D_vcf8")
print(np.mean(D_vcf8_fp_result))
print("   ")
print("   ")
