from cuckoofilter import CuckooFilter
from extendcuckoofiltertwosize2 import extendCuckooFilter
#cf = extendCuckooFilter(capacity=100000, bucket_size=1, fingerprint_size=2)
from hashutils import fingerprint
from hashutils import hash_code
from hashutils import _fnv64
from hashutils import _int_to_bytes
from hashutils import _bytes_to_int
from bucket import Bucket

"""
cf.insert("fpt")
print("fpt" in cf)
print(cf.size)
print(len(cf))

cf.insert("love")
print("love" in cf)
print(cf.size)

cf.insert("jy")
print("jy" in cf)
print(cf.size)

deletejyy = cf.delete("jyy")
print("删除jyy结果：", deletejyy)

deletfpt = cf.delete("fpt")
print("删除fpt结果", deletfpt)

print("jy4" in cf)

print("测试下桶的长度是多少：", len(cf.buckets))
print("测试下buckets是啥:", cf.buckets)

## jy1的存储桶的索引值以及其指纹值的哈希值
jy1index = cf._get_index("sxy")
print("sxy的存储桶的索引值是：", jy1index)
print("sxy的存储桶的索引值转换成二进制是：", bin(jy1index))

ss = fingerprint("sxy", 1)
fps = hash_code(ss)
print("sxy的指纹值的哈希值是：", fps)
print("sxy的指纹值的哈希值转换成二进制是：", bin(fps))

jyy_alter_bucket = cf._get_alternate1_index(jy1index, ss)
print("sxy的候选桶1的索引值是：", jyy_alter_bucket)

jyy_alter_bucket = cf._get_alternate2_index(jy1index, ss)
print("sxy的候选桶2的索引值是：", jyy_alter_bucket)

jyy_alter_bucket = cf._get_alternate3_index(jy1index, ss)
print("sxy的候选桶3的索引值是：", jyy_alter_bucket)

## fpt的存储桶和候选桶的索引值以及其指纹值的哈希值
fptindex = cf._get_index("ff")
print("fpt的存储桶的索引值是：", fptindex)
print("fpt的存储桶的索引值转换成二进制是：", bin(fptindex))

sss = fingerprint("ff", 1)
fpfpt = hash_code(sss)
print("fpt的指纹值的哈希值是：", fpfpt)
print("fpt的指纹值的哈希值转换成二进制是：", bin(fpfpt))

fpt_alter_bucket1 = cf._get_alternate1_index(fptindex, sss)
print("fpt的候选桶1的索引值是：", fpt_alter_bucket1)

fpt_alter_bucket2 = cf._get_alternate2_index(fptindex, sss)
print("fpt的候选桶2的索引值是：", fpt_alter_bucket2)

fpt_alter_bucket3 = cf._get_alternate3_index(fptindex, sss)
print("fpt的候选桶3的索引值是：", fpt_alter_bucket3)

#由候选桶反推原来的桶的索引值
fpt_initial_bucket = cf._get_alternate1_index(fpt_alter_bucket1, sss)
print("fpt由候选桶1推其他桶的索引值是：", fpt_initial_bucket)

fpt_initial_bucket = cf._get_alternate2_index(fpt_alter_bucket1, sss)
print("fpt由候选桶1推其他桶的索引值是：", fpt_initial_bucket)

fpt_initial_bucket = cf._get_alternate3_index(fpt_alter_bucket1, sss)
print("fpt由候选桶1推其他桶的索引值是：", fpt_initial_bucket)


print(type("fptt"))

a = "fptt"
print(a.encode())

print(type("jyyy"))
b = "jyyy"
print(b.encode())

# 测试英文字符串的指纹值生成过程怎么一样
FNV64_OFFSET_BASIS = 0xcbf29ce484222325
FNV64_PRIME = 0x100000001b3
MAX_64_INT = 2 ** 64
MAX_32_INT = 2 ** 32

data = "jyy"
h = FNV64_OFFSET_BASIS
for byte in data.encode():  # 字符串通过调用encode函数转换成bytes
    h = (h * FNV64_PRIME) % MAX_64_INT
    print("jyy一开始：", h)
    h ^= byte
    print("jyy后面：", abs(h))
print("jyy最终的h是：", h)
jyyh = h

data = "fpt"
h = FNV64_OFFSET_BASIS
for byte in data.encode():  # 字符串通过调用encode函数转换成bytes
    h = (h * FNV64_PRIME) % MAX_64_INT
    print("fpt一开始：", h)
    h ^= byte
    print("fpt后面：", abs(h))
print("fpt最终的h是：", h)
fpth = h
#   xx = _fnv64("fpt")
#   print(xx)

#_int_to_bytes函数这一步，看是否在此出问题

xx = _int_to_bytes(jyyh)
print("jyy的int_to_bytes这一步为：", xx)

yy = _int_to_bytes(fpth)
print("fpt的int_to_bytes这一步为：", yy)

#_bytes_to_int函数这一步，看是否在此出问题
xxx = _bytes_to_int(xx[:2])
print("jyy的_bytes_to_int这一步为：", xxx)

yyy = _bytes_to_int(yy[:2])
print("jyy的_bytes_to_int这一步为：", yyy)

print("xd8转10进制是：", int("0xd8", 16))


ssss = fingerprint("zzzzzzzzzzzzzzzzz", 1)
print(ssss)
fpfpt = hash_code(ssss)
print("fpt的指纹值的哈希值是：", fpfpt)

print(int("0b11110111", 2))
print(int("0b01101011", 2))

xy = 0b10011100 ^ 0b00000111
print(xy)

x1 = 247 & 15
print(bin(x1))
x2 = 0b10011100 ^ x1
print(x2)
print(bin(x2))
"""


import random
import string

"""
# 测试插入16位的随机字符串
alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
testdata = [0 for i in range(40000)]
for num in range(40000):
    sa = []
    for i in range(16):
        sa.append(random.choice(alphabet))
    testdata[num] = "".join(sa)
# print(testdata)
# print(testdata[0])


# seek_count = 0
for i in range(len(testdata)):
    cf.insert(testdata[i])
#    if cf.contains(testdata[i]):
#  seek_count += 1
no0 = 0
no1 = 0
no2 = 0
no3 = 0
for i in range(10000):
    if len(cf.buckets[i]) == 0:
        no0 += 1
    if len(cf.buckets[i]) == 1:
        no1 += 1
    if len(cf.buckets[i]) == 2:
        no2 += 1
    if len(cf.buckets[i]) == 3:
        no3 += 1
number_empty_slots = no0 * 4 + no1 * 3 + no2 * 2 + no3 * 1
print("空的槽的数量为：", number_empty_slots)
print("空间利用率为：", 1 - number_empty_slots / 40000.0)
print("空的桶的数量：", no0)
print("cf插入后的size是:", cf.size)

x = 0
y = 0
for i in range(len(testdata)):
    if cf.contains(testdata[i]):
        x += 1
    if not testdata[i] in cf:
        y += 1
    #if not str(testdata1[i]) in cf:
     #   print(str(testdata1[i]))
print(x)
print(y)
"""

"""
# 插入0到40000的固定字符型数据，与原代码比较
testdata1 = list(range(40000))
test_occupancy_rate = list(range(100))
sum = 0
for j in range(100):
    cf0 = extendCuckooFilter(capacity=10000, bucket_size=4, fingerprint_size=1)
    for i in range(len(testdata1)):
        cf0.insert(str(testdata1[i]))
    test_occupancy_rate[j] = cf0.size / 40000.0
for i in test_occupancy_rate:
    sum = sum + i
print("改进后的extend cuckoo filter的空间利用率为：", sum / 100.0)
"""



import datetime
import time
"""
# 插入0到100000的固定字符型数据，与原代码比较
testdata1 = list(range(400000))
test_occupancy_rate = list(range(2))
test_time_consume = list(range(2))
sum = 0
for j in range(2):
    cf0 = extendCuckooFilter(capacity=100000, bucket_size=4, fingerprint_size=2)
    start = datetime.datetime.now()  # 开始时间
    for i in range(len(testdata1)):
        cf0.insert(str(testdata1[i]))
    end = datetime.datetime.now()  # 结束时间
    test_occupancy_rate[j] = cf0.size / 400000.0
    test_time_consume[j] = end - start

for i in test_occupancy_rate:
    sum = sum + i

time = test_time_consume[0]
for i in range(1):
    time = time + test_time_consume[i + 1]

print("传统cuckoo filter的空间利用率为：", sum / 2.0)
print("程序运行时间为：", time / 2.0)
#print(cf.buckets)
"""

"""
testdata1 = list(range(100000))
testdata2 = list(range(100000, 200000))
cf0 = extendCuckooFilter(capacity=50000, bucket_size=4, fingerprint_size=2)
start = datetime.datetime.now()  # 开始时间
for i in range(len(testdata1)):
    cf0.insert1(str(testdata1[i]))
for i in range(len(testdata2)):
    cf0.insert2(str(testdata2[i]))
end = datetime.datetime.now()  # 结束时间
time = end - start
print("传统cuckoo filter的空间利用率为：", cf0.size / 200000.0)
print("程序运行时间为：", time)


testdata1 = list(range(200000))
cf1 = extendCuckooFilter(capacity=50000, bucket_size=4, fingerprint_size=2)
start = datetime.datetime.now()  # 开始时间
for i in range(len(testdata1)):
    cf1.insert2(str(testdata1[i]))
end = datetime.datetime.now()  # 结束时间
time = end - start
print("传统cuckoo filter的空间利用率为：", cf1.size / 200000.0)
print("程序运行时间为：", time)


testdata1 = list(range(200000))
cf2 = extendCuckooFilter(capacity=50000, bucket_size=4, fingerprint_size=2)
start = datetime.datetime.now()  # 开始时间
for i in range(len(testdata1)):
    cf2.insert1(str(testdata1[i]))
end = datetime.datetime.now()  # 结束时间
time = end - start
print("传统cuckoo filter的空间利用率为：", cf2.size / 200000.0)
print("程序运行时间为：", time)

"""


"""
# 传统两个桶和改进后四桶交替存储数据的测试
print("传统两个桶和改进后四桶交替存储数据的测试,容量260000")
size = [0 for i in range(100)]
time = [0 for i in range(100)]
data_capacity = 260000
for xx in range(0, data_capacity + 1, 10000):
    for ii in range(100):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
        testdata = [0 for i in range(data_capacity)]
        for num in range(data_capacity):
            sa = []
            for i in range(16):
                sa.append(random.choice(alphabet))
            testdata[num] = "".join(sa)

        cf = extendCuckooFilter(capacity=65000, bucket_size=4, fingerprint_size=2)

        start = datetime.datetime.now()  # 开始时间
        for j in range(xx):
            cf.insert1(testdata[j])
        for j in range(xx, data_capacity):
            cf.insert2(testdata[j])
        end = datetime.datetime.now()  # 结束时间

        size[ii] = cf.size / data_capacity
        time[ii] = end - start
    print("传统两桶存储的数据量为：", xx)
    x = 0
    for i in size:
        x = x + i
    print(x / 100.0)
    x = time[0]
    for i in range(99):
        x = x + time[i + 1]
    print(x / 100.0)



# 传统两个桶和改进后四桶交替存储数据的测试
print("传统两个桶和改进后四桶交替存储数据的测试,容量260000，探索250000到260000之间的交替存储")
size = [0 for i in range(100)]
time = [0 for i in range(100)]
data_capacity = 260000
for xx in range(250000, data_capacity + 1, 1000):
    for ii in range(100):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
        testdata = [0 for i in range(data_capacity)]
        for num in range(data_capacity):
            sa = []
            for i in range(16):
                sa.append(random.choice(alphabet))
            testdata[num] = "".join(sa)

        cf = extendCuckooFilter(capacity=65000, bucket_size=4, fingerprint_size=2)

        start = datetime.datetime.now()  # 开始时间
        for j in range(xx):
            cf.insert1(testdata[j])
        for j in range(xx, data_capacity):
            cf.insert2(testdata[j])
        end = datetime.datetime.now()  # 结束时间

        size[ii] = cf.size / data_capacity
        time[ii] = end - start
    print("传统两桶存储的数据量为：", xx)
    x = 0
    for i in size:
        x = x + i
    print(x / 100.0)
    x = time[0]
    for i in range(99):
        x = x + time[i + 1]
    print(x / 100.0)

"""


"""
# 三种方案的针对不同数据容量的测试
# 测试插入16位的随机字符串

print("三种方案的针对不同数据容量的测试")
number = [200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000]
bucket_number = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]

for numm in range(len(number)):
    size1 = [0 for i in range(100)]
    time1 = [0 for i in range(100)]
    size2 = [0 for i in range(100)]
    time2 = [0 for i in range(100)]
    size3 = [0 for i in range(100)]
    time3 = [0 for i in range(100)]
    for ii in range(100):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
        testdata = [0 for i in range(number[numm])]
        for num in range(number[numm]):
            sa = []
            for i in range(16):
                sa.append(random.choice(alphabet))
            testdata[num] = "".join(sa)

        cf = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start = datetime.datetime.now()  # 开始时间
        for j in range(int(0.65*number[numm])):
            cf.insert1(testdata[j])
        for j in range(int(0.65*number[numm]), number[numm]):
            cf.insert2(testdata[j])
        end = datetime.datetime.now()  # 结束时间
        size1[ii] = cf.size / number[numm]
        time1[ii] = end - start

        cf1 = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start1 = datetime.datetime.now()  # 开始时间
        for j in range(number[numm]):
            cf1.insert2(testdata[j])
        end1 = datetime.datetime.now()  # 结束时间
        size2[ii] = cf1.size / number[numm]
        time2[ii] = end1 - start1

        cf2 = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start2 = datetime.datetime.now()  # 开始时间
        for j in range(number[numm]):
            cf2.insert1(testdata[j])
        end2 = datetime.datetime.now()  # 结束时间
        size3[ii] = cf2.size / number[numm]
        time3[ii] = end2 - start2

    print("数据容量为：", number[numm])
    x = 0
    for i in size1:
        x = x + i
    print(x / 100.0)
    x = time1[0]
    for i in range(99):
        x = x + time1[i + 1]
    print(x / 100.0)

    x = 0
    for i in size2:
        x = x + i
    print(x / 100.0)
    x = time2[0]
    for i in range(99):
        x = x + time2[i + 1]
    print(x / 100.0)

    x = 0
    for i in size3:
        x = x + i
    print(x / 100.0)
    x = time3[0]
    for i in range(99):
        x = x + time3[i + 1]
    print(x / 100.0)
"""


import math
# 三种方案的针对不同数据容量的测试，踢出重放次数为100，100次平均值
# 测试插入16位的随机字符串

print("指纹哈希值长度为2个字节,三种方案的针对不同数据容量(2**15到2**22)的测试，踢出重放次数为500，10次平均值")
#number = range(200000, 1000001, 50000)
#bucket_number = range(50000, 250001, 12500)

#number = list()
#for i in range(2, 33, 1):
 #   number.append(i*2**15)

#bucket_number = list()
#for i in range(2, 33, 1):
 #   bucket_number.append(i*2**13)

number = [2**13, 2**14, 2**15, 2**16, 2**17, 2**18, 2**19, 2**20, 2**21]
bucket_number = [2**11, 2**12, 2**13, 2**14, 2**15, 2**16, 2**17, 2**18, 2**19]
scheme1_space = list()
scheme2_space = list()
scheme3_space = list()
scheme1_time = list()
scheme2_time = list()
scheme3_time = list()

for numm in range(len(number)):
    size1 = [0 for i in range(10)]
    time1 = [0 for i in range(10)]
    size2 = [0 for i in range(10)]
    time2 = [0 for i in range(10)]
    size3 = [0 for i in range(10)]
    time3 = [0 for i in range(10)]
    for ii in range(10):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
        testdata = [0 for i in range(number[numm])]
        for num in range(number[numm]):
            sa = []
            for i in range(16):
                sa.append(random.choice(alphabet))
            testdata[num] = "".join(sa)

        cf = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start = datetime.datetime.now()  # 开始时间
        for j in range(int(0.65*number[numm])):
            cf.insert1(testdata[j])
        for j in range(int(0.65*number[numm]), number[numm]):
            cf.insert2(testdata[j])
        end = datetime.datetime.now()  # 结束时间
        size1[ii] = cf.size / number[numm]
        time1[ii] = (end - start).seconds      # 相差的妙数，类型为int

        cf1 = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start1 = datetime.datetime.now()  # 开始时间
        for j in range(number[numm]):
            cf1.insert2(testdata[j])
        end1 = datetime.datetime.now()  # 结束时间
        size2[ii] = cf1.size / number[numm]
        time2[ii] = (end1 - start1).seconds

        cf2 = extendCuckooFilter(capacity=bucket_number[numm], bucket_size=4, fingerprint_size=2)
        start2 = datetime.datetime.now()  # 开始时间
        for j in range(number[numm]):
            cf2.insert1(testdata[j])
        end2 = datetime.datetime.now()  # 结束时间
        size3[ii] = cf2.size / number[numm]
        time3[ii] = (end2 - start2).seconds

    # 转换成对数形式再绘图
    x = 0
    for i in size1:
        x = x + i
    scheme1_space.append(x/10.0)
    y = 0
    for i in time1:
        y = y + i
    if y == 0:
        scheme1_time.append(0)
    else:
        scheme1_time.append(math.log2(y / 10.0))     # 转换成对数形式绘图

    x = 0
    for i in size2:
        x = x + i
    scheme2_space.append(x/10.0)
    y = 0
    for i in time2:
        y = y + i
    if y == 0:
        scheme2_time.append(0)
    else:
        scheme2_time.append(math.log2(y / 10.0))

    x = 0
    for i in size3:
        x = x + i
    scheme3_space.append(x/10.0)
    y = 0
    for i in time3:
        y = y + i
    if y == 0:
        scheme3_time.append(0)
    else:
        scheme3_time.append(math.log2(y / 10.0))

print("三种方案的空间利用率为：")
print(scheme1_space)
print(scheme2_space)
print(scheme3_space)
print("三种方案的时间消耗为：")
print(scheme1_time)
print(scheme2_time)
print(scheme3_time)

#   绘制空间利用率的折线图
import matplotlib.pyplot as plt
y1 = scheme1_space
y2 = scheme2_space
y3 = scheme3_space
x = [11, 12, 13, 14, 15, 16, 17, 18, 19]


plt.plot(x, y1, label='Scheme one', linewidth=3, color='r', marker='o',
markerfacecolor = 'blue', markersize=10)
plt.plot(x, y2, label='Scheme two', linewidth=3, color='y', marker='o',
markerfacecolor = 'green', markersize=10)
plt.plot(x, y3, label='Scheme three', linewidth=3, color='c', marker='o',
markerfacecolor = 'pink', markersize=10)

plt.xlabel('Data Capacity')
plt.ylabel('Utility rate of space')
plt.title('Number of kick out = 500')
plt.legend()
plt.show()

#   绘制时间消耗的折线图
import matplotlib.pyplot as plt1
y1 = scheme1_time
y2 = scheme2_time
y3 = scheme3_time
x = [11, 12, 13, 14, 15, 16, 17, 18, 19]

plt1.plot(x, y1, label='Scheme one', linewidth=3, color='r', marker='o',
markerfacecolor = 'blue', markersize=10)
plt1.plot(x, y2, label='Scheme two', linewidth=3, color='y', marker='o',
markerfacecolor = 'green', markersize=10)
plt1.plot(x, y3, label='Scheme three', linewidth=3, color='c', marker='o',
markerfacecolor = 'pink', markersize=10)

plt1.xlabel('Data Capacity')
plt1.ylabel('Time consumption')
plt1.title('Number of kick out = 500')
plt1.legend()
plt1.show()
