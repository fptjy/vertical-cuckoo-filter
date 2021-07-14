import pandas
#最终预处理代码，将29个特征视为一个字符串
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/HIGGS.csv', 'r') as fin:
#     with open('data200wan.csv', 'w', newline="") as fout:
#         block = []
#         for line in fin:
#             block.append(line)
#             if len(block) <= 2000000:
#                 fout.write(line.replace(",",""))
#             else:
#                 break
#         #print(block)
#
# print(len(block))

##因为此处用到的哈希函数运行时间跟字符串长度大小有关，因此只能选取两个特征(第3和第4个)最好，重新划分数据集，取到

#
# import csv
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/HIGGS.csv', 'r') as fin:
#     with open('data500w.csv', 'w', newline="") as fout:
#         writer = csv.writer(fout, dialect="excel")
#         block = []
#         for line in fin:
#             block.append(line)
#             if len(block) <= 20000000:
#                 x = line.split(",")[2]+line.split(",")[3]
#                 writer.writerow([x, ""])
#             else:
#                 break
#         #print(block)
#
# print(len(block))

import csv
import random
import datetime
#
# raw_data = []
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data500w.csv', 'r') as fin:
#     for line in fin:
#         raw_data.append(line)
# fin.close()
#
# print(len(raw_data))
# y = list(set(raw_data))
# # y.sort(key=raw_data.index)
# print(len(y))
# print(y[0])
#
# with open('VCF_testdata.csv', 'w', newline="") as fout:
#         writer = csv.writer(fout, dialect="excel")
#         for i in range(len(y)):
#             writer.writerow([y[i],""])
#
# raw_data1 = []
# with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/VCF_testdata.csv', 'r') as fin:
#     for line in fin:
#         raw_data1.append(line)
# fin.close()
#
#
# ss = []
# for i in range(len(raw_data1)):
#     if raw_data1[i] != raw_data1[1]:
#         x = raw_data1[i].replace(",", "")
#         y = x.replace('"', "")
#         z = y.replace("\n", "")
#         ss.append(z)
#
# with open('finaltestdata.csv', 'w', newline="") as fpt:
#         writer = csv.writer(fpt, dialect="excel")
#         for i in range(len(ss)):
#             writer.writerow([ss[i],""])


raw_data2 = []
with open('C:/Users/fptjy/pydaima/cuckoopy-master/cuckoopy/data_test_8676622.csv', 'r') as fin:
    for line in fin:
        raw_data2.append(line.replace(",\n", ""))
fin.close()

start = datetime.datetime.now()
testdata1 = random.sample(raw_data2, 2**10)
end = datetime.datetime.now()
time_s = (end - start).seconds
time_ms = (end - start).microseconds
time = time_s + time_ms / 10 ** 6
print(time)
print(len(testdata1))
print(testdata1[0])