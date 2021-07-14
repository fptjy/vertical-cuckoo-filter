import random
# from Vcuckoofilter import VCuckooFilter
from random import randint
from cuckoofilter import CuckooFilter
import datetime
import numpy as np

# capacity1 = 2**20
# alphabet = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()+=_-"
# testdata1 = [0 for i in range(capacity1)]
# for num in range(capacity1):
#     sa = []
#     for i in range(randint(1, 33)):
#         sa.append(random.choice(alphabet))
#     testdata1[num] = "".join(sa)
#
#
# cf = VCuckooFilter(capacity=2**18, bucket_size=4, fingerprint_size=5)
#
# for i in range(capacity1):
#     cf.insert1(testdata1[i])
#
# print(cf.size / capacity1)
#
#
# cf1 = CuckooFilter(capacity=2**18, bucket_size=4, fingerprint_size=5)
# for i in range(capacity1):
#     cf1.insert(testdata1[i])
# print(cf1.size / capacity1)
#
#
# cf2 = VCuckooFilter(capacity=2**18, bucket_size=4, fingerprint_size=5)
# for i in range(capacity1):
#     cf2.insert2(testdata1[i])
# print(cf2.size / capacity1)
#
# for i in range(100):
#     print(cf2.buckets[i])


# cf = VCuckooFilter(capacity=2**18, bucket_size=4, fingerprint_size=5)
# cf.insert2("fptlovejy")
# print(cf.contains2("fptlovejy"))
# print(cf.contains2("ss"))


raw_data = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data200wan.csv', 'r') as fin:
    for line in fin:
        raw_data.append(line)
fin.close()

number = 10


from Vcuckoofilter7 import VCuckooFilter7
fingersize = 7
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = 2 ** 15

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter7(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的15次方时空间利用率为：", x)
print("CF时间：", y)

##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter7(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的15次方时空间利用率为：", x)
print("4-VCF时间：", y)



###filter size取2 ** 20
##设置参数
capacity1 = 2 ** 20

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter7(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的20次方时空间利用率为：", x)
print("CF时间：", y)


##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter7(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的20次方时空间利用率为：", x)
print("4-VCF时间：", y)
print("    ")
print("    ")



from Vcuckoofilter17 import VCuckooFilter17
fingersize = 17
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = 2 ** 15

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter17(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的15次方时空间利用率为：", x)
print("CF时间：", y)

##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter17(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的15次方时空间利用率为：", x)
print("4-VCF时间：", y)



###filter size取2 ** 20
##设置参数
capacity1 = 2 ** 20

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter17(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的20次方时空间利用率为：", x)
print("CF时间：", y)


##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter17(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的20次方时空间利用率为：", x)
print("4-VCF时间：", y)
print("    ")
print("    ")





from Vcuckoofilter18 import VCuckooFilter18
fingersize = 18
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = 2 ** 15

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter18(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的15次方时空间利用率为：", x)
print("CF时间：", y)

##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter18(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的15次方时空间利用率为：", x)
print("4-VCF时间：", y)



###filter size取2 ** 20
##设置参数
capacity1 = 2 ** 20

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter18(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的20次方时空间利用率为：", x)
print("CF时间：", y)


##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter18(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的20次方时空间利用率为：", x)
print("4-VCF时间：", y)
print("    ")
print("    ")




from Vcuckoofilter19 import VCuckooFilter19
fingersize = 19
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = 2 ** 15

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter19(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的15次方时空间利用率为：", x)
print("CF时间：", y)

##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter19(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的15次方时空间利用率为：", x)
print("4-VCF时间：", y)



###filter size取2 ** 20
##设置参数
capacity1 = 2 ** 20

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter19(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的20次方时空间利用率为：", x)
print("CF时间：", y)


##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter19(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的20次方时空间利用率为：", x)
print("4-VCF时间：", y)
print("    ")
print("    ")





from Vcuckoofilter20 import VCuckooFilter20
fingersize = 20
print("实验中指纹值长度为：", fingersize)

###filter size取2 ** 15
##设置参数
capacity1 = 2 ** 15

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter20(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的15次方时空间利用率为：", x)
print("CF时间：", y)

##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter20(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的15次方时空间利用率为：", x)
print("4-VCF时间：", y)



###filter size取2 ** 20
##设置参数
capacity1 = 2 ** 20

##CF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter20(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert1(testdata1[i])
    end = datetime.datetime.now()  # 结束时间
    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("CF在2的20次方时空间利用率为：", x)
print("CF时间：", y)


##4-VCF进行十次实验取均值
space_overhead = []
time_overhead = []
for num in range(number):

    testdata1 = random.sample(raw_data, capacity1)
    cf = VCuckooFilter20(capacity=capacity1 // 4, bucket_size=4, fingerprint_size=fingersize)
    start = datetime.datetime.now()  # 开始时间
    for i in range(capacity1):
        cf.insert2(testdata1[i])
    end = datetime.datetime.now()  # 结束时间

    time = (end - start).microseconds
    load_factor = cf.size / capacity1
    space_overhead.append(load_factor)
    time_overhead.append(time)

x = np.mean(space_overhead)
y = np.mean(time_overhead)

print("4-VCF在2的20次方时空间利用率为：", x)
print("4-VCF时间：", y)
print("    ")
print("    ")

