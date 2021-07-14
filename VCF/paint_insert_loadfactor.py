# encoding=utf-8
import matplotlib
import math

matplotlib.rcParams["backend"] = "SVG"
import numpy as np
import matplotlib.pyplot as plt

# ###比较vcf在不同空间利用率下的插入吞吐量
# ##输入因变量
#
# cf = [54419.935063479665, 59118.5178397484, 57246.7029402551, 58029.41853014445, 57675.18941224692, 55465.64604481958,
#       56455.855495624, 56604.96082324161, 58166.03968890563, 54286.88260408172, 54879.77338885876, 54895.92790179512,
#       54760.56205097609, 53816.65069316987, 53447.27093968393, 50302.42391386761, 45886.89014043471, 39455.380444003815,
#       25658.23427812588, 1853.901702213189]
# vcf7 = [51525.679154042075, 53667.02982646011, 54829.25948531239, 54573.14541002003, 54730.6845591732, 53753.6270775879,
#         53955.469834270036, 54384.43309821044, 54948.5685181775, 51495.858536573265, 52181.520902277225,
#         52060.86488153894, 52336.37700017938, 52110.42762978176, 52865.51191682547, 49149.08020285993,
#         47704.801608021015, 44385.80202168925, 39196.49970578581, 19694.928395090454]
# vcf6 = [51508.93175245275, 54218.729256641695, 54372.68132650559, 54942.91554818769, 53578.87493267602,
#         54503.990453090955, 53181.38933435595, 54368.31872773397, 56049.307980028396, 53326.73273135713,
#         53299.71330833366, 51113.64176164484, 52871.430261373025, 51828.03818321936, 52656.158167574984,
#         49908.05211743587, 47382.09169683781, 44378.79250893256, 38594.87229276806, 19704.37324044935]
# vcf5 = [53237.60605938856, 55985.410368052435, 53894.084676486156, 55369.494390303116, 55071.34085335093,
#         53716.123107144515, 54171.4464028002, 54508.87141242565, 55326.814715414206, 52041.64767724969,
#         52741.593194329565, 52000.47631164472, 52202.06777677758, 50954.63198382761, 53115.85012290348,
#         50726.87056923057, 48498.85626221719, 43993.16609546887, 38384.77423204744, 19545.429864429163]
# vcf4 = [53068.696135587976, 53923.968042426044, 53231.72963210822, 54081.892864215355, 55358.4271158488,
#         53255.269520098824, 53585.96267765648, 54380.77707155138, 55489.050879936076, 53787.48895621967,
#         54690.04985286507, 53212.55108472551, 52389.52648228161, 52467.85599220242, 53226.67526001937,
#         50973.60283645988, 48302.28788585721, 44616.204184184615, 37963.618748927875, 18788.69503923641]
# vcf3 = [51132.359969280864, 52538.57298161485, 51819.47155680104, 54066.55481982329, 54574.90937959994,
#         53104.50340544323, 54480.259237116836, 54252.88694209365, 54280.507352234665, 52390.95128462226,
#         52903.26566013413, 52903.07858975275, 51813.006441728554, 51716.30011548327, 52009.72917445057,
#         49149.36762407504, 48449.335061573045, 43800.81428757058, 36974.51757346131, 17253.542522780543]
# vcf2 = [52962.001474448225, 52443.333191050966, 52245.298669909316, 52489.809651388416, 53912.30360571207,
#         51083.97993324019, 53982.42349244399, 53032.35888864422, 55089.87960374315, 53060.91390618613,
#         53037.256972057665, 52678.779329034245, 53132.49060169495, 51426.28973163703, 51833.45217820799,
#         50120.59408112198, 47213.883176343035, 42766.821328831706, 34521.585874882156, 13765.77285209202]
# vcf1 = [52381.755337663126, 54065.91741953231, 55279.38657841105, 53073.747317457506, 55250.12309687806,
#         51913.581844195214, 53541.60248550567, 53809.21151888401, 53221.525758223914, 52878.301140607175,
#         52009.149982877636, 53467.46714369328, 51675.31944143208, 51466.8939870092, 49298.6935885629,
#         47383.767022883745, 44313.302168861774, 38159.50106956065, 28509.883080632288, 7701.024237907972]
#
# y1 = np.array(cf)
# y2 = np.array(vcf1)
# y3 = np.array(vcf2)
# y4 = np.array(vcf3)
# y5 = np.array(vcf4)
# y6 = np.array(vcf5)
# y7 = np.array(vcf6)
# y8 = np.array(vcf7)
#
# for i in range(len(y1)):
#     y1[i] = y1[i] / 10 ** 4
#     y2[i] = y2[i] / 10 ** 4
#     y3[i] = y3[i] / 10 ** 4
#     y4[i] = y4[i] / 10 ** 4
#     y5[i] = y5[i] / 10 ** 4
#     y6[i] = y6[i] / 10 ** 4
#     y7[i] = y7[i] / 10 ** 4
#     y8[i] = y8[i] / 10 ** 4
#
# # assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
# fig, ax = plt.subplots(figsize=(6.4, 4.2), dpi=100)
# # ax2 = ax.twinx()
# # 设置自变量的范围和个数
# x = np.linspace(0.025, 0.975, y3.shape[0])
# # 画图
# s1 = ax.plot(x, y1, label='CF', linestyle='-', marker='^', markersize='8')
# s2 = ax.plot(x, y2, label='IVCF1', linestyle='--', marker='D', markersize='8')
# # s3 = ax.plot(x, y3, label='IVCF2', linestyle=':', marker='v', markersize='8')
# # s4 = ax.plot(x, y4, label='IVCF3', linestyle='-.', marker='x', markersize='8')
# # s5 = ax.plot(x, y5, label='IVCF4', linestyle='-', marker='<', markersize='8')
# # s6 = ax.plot(x, y6, label='IVCF5', linestyle='--', marker='o', markersize='8')
# # s7 = ax.plot(x, y7, label='IVCF6', linestyle=':', marker='>', markersize='8')
# s8 = ax.plot(x, y8, label='VCF', linestyle='-.', marker='*', markersize='8')
#
# # 设置坐标轴
#
# ax.set_xlabel('table occupancy',
#               fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
# ax.set_ylabel('insert tput ($×$10$^4$)', fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
#
# # 设置刻度
# ax.tick_params(labelsize=16)
# labels = ax.get_xticklabels() + ax.get_yticklabels()
# [label.set_fontname('Times New Roman') for label in labels]
#
# # 显示网格
# # ax.grid(True, linestyle='-.')
# ax.yaxis.grid(True, linestyle='-.')
# # 添加图例,图例控制,将图例放在一起
# # ss = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
# ss = s1 + s2 +  s8
# labs = [l.get_label() for l in ss]
# ax.legend(ss, labs, loc="best", prop={'family': 'Times New Roman', "size": 20})
# # legend = ax.legend(loc=2)
# # legend2 = ax2.legend(loc="best")
#
# # plt.legend()
# plt.show()
# fig.savefig('C:/Users/fptjy/Desktop/tu/IVCF_insertthp_load.svg', dpi=600, format='svg')
# # # fig.savefig('1.png')


# ###比较dvcf在不同空间利用率下的插入吞吐量
# ##输入因变量
#
# cf = [54419.935063479665, 59118.5178397484, 57246.7029402551, 58029.41853014445, 57675.18941224692, 55465.64604481958,
#       56455.855495624, 56604.96082324161, 58166.03968890563, 54286.88260408172, 54879.77338885876, 54895.92790179512,
#       54760.56205097609, 53816.65069316987, 53447.27093968393, 50302.42391386761, 45886.89014043471, 39455.380444003815,
#       25658.23427812588, 1853.901702213189]
# dvcf8 = [53052.638137862945, 54349.931823027386, 53237.03820217963, 53212.39336132521, 53698.703414747455,
#          51738.28576808287, 50773.28128554877, 52502.04976360454, 52499.44623770395, 53694.01261668793,
#          54884.104456082925, 52701.90421981992, 53112.38350339763, 52994.184888920856, 52737.86061130733,
#          50635.40910475547, 48776.0327332345, 45581.97045008139, 39122.46893383461, 20831.62934076193]
# dvcf7 = [52156.228632060614, 53967.14051633894, 51822.262510145825, 53051.113129404825, 52821.35960637391,
#          52105.40705110959, 52410.0114453915, 52083.01982100873, 54022.58855794872, 53430.641947619646,
#          53055.43254960733, 51388.0740875938, 54655.01991538019, 52063.13757047387, 52319.28060872597, 49592.904713927,
#          47520.02695371676, 45795.578931350006, 38477.49866923947, 19809.847224511366]
# dvcf6 = [54960.849895144034, 54813.11962140535, 55810.09738789477, 54184.45687133569, 55245.85122206625,
#          53349.25606421118, 51602.841483586104, 52070.81237857745, 54390.91324609598, 53494.714547761,
#          53125.344773542354, 52454.47190559676, 53389.47987613745, 51930.186930902644, 50761.78558679919,
#          50799.864640405285, 47929.287506113134, 44756.64761736115, 38222.26023587761, 18710.438226347684]
# dvcf5 = [54278.560234543, 54608.36210964086, 53342.22499739272, 54342.954717754896, 56397.726143243126,
#          54070.435059150346, 52525.82550068975, 51990.79765694744, 52754.429370905964, 54172.086980799926,
#          52037.11453538637, 51942.488744339316, 52028.70981761296, 51951.3807167122, 52489.882604540886,
#          51606.598237194456, 48025.11159978494, 43282.73516280898, 37125.343489003026, 17365.66192004484]
# dvcf4 = [54601.017023324755, 53966.98115052457, 52800.92107936305, 55670.895051743, 54821.70560547416,
#          55784.656616689506, 52563.1485725698, 53054.20155685032, 54679.27210499301, 55226.7062203954,
#          55331.86268188102, 52095.90371429077, 53713.74664053832, 51910.22544687094, 52777.11407320162,
#          49891.335424958655, 47858.908786804874, 43518.77519888731, 34900.28656381473, 15496.033081536503]
# dvcf3 = [55254.887072000965, 55744.04172098956, 55815.919870405145, 54609.47061895349, 57274.28453387618,
#          55614.16930551453, 53891.96697190762, 54473.84976881905, 53043.99084882364, 54772.7805493268,
#          53895.65615926944, 52122.383046176496, 52211.388783395705, 51921.32489165362, 50779.653560291204,
#          49867.50883627335, 48173.31815726468, 42672.04948704421, 33689.35082560065, 13007.904534792406]
# dvcf2 = [57126.961848671934, 54459.092089838254, 55044.47273249207, 54612.11179769547, 55834.52254040744,
#          56228.86912604249, 52716.11386918172, 56167.470341984335, 53978.39064664214, 55449.715548463944,
#          54562.46901876283, 52122.64866476266, 53484.322185678204, 52834.63495767863, 52404.199801674964,
#          49624.4118656231, 47173.939528466406, 41783.52357879879, 31844.646141273806, 9928.371911639184]
# dvcf1 = [56247.85584542954, 54342.241640742446, 54774.91699882371, 55164.35298640381, 56119.893894707944,
#          53917.30089478687, 53041.55105875563, 55232.700385986485, 52872.28357151576, 53581.18179962938,
#          56409.55038347938, 52299.68237540145, 54287.653475543804, 52252.23565568039, 51568.83142141127,
#          49364.164173430894, 46869.11708882287, 41010.39850638589, 28996.804621908304, 5577.997541831404]
#
# y1 = np.array(cf)
# y2 = np.array(dvcf1)
# y3 = np.array(dvcf2)
# y4 = np.array(dvcf3)
# y5 = np.array(dvcf4)
# y6 = np.array(dvcf5)
# y7 = np.array(dvcf6)
# y8 = np.array(dvcf7)
# y9 = np.array(dvcf8)
#
# for i in range(len(y1)):
#     y1[i] = y1[i] / 10 ** 4
#     y2[i] = y2[i] / 10 ** 4
#     y3[i] = y3[i] / 10 ** 4
#     y4[i] = y4[i] / 10 ** 4
#     y5[i] = y5[i] / 10 ** 4
#     y6[i] = y6[i] / 10 ** 4
#     y7[i] = y7[i] / 10 ** 4
#     y8[i] = y8[i] / 10 ** 4
#     y9[i] = y9[i] / 10 ** 4
#
# # assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
# fig, ax = plt.subplots(figsize=(6.4, 4.2), dpi=100)
# # ax2 = ax.twinx()
# # 设置自变量的范围和个数
# x = np.linspace(0.025, 0.975, y3.shape[0])
# # 画图
# s1 = ax.plot(x, y1, label='CF', linestyle='-', marker='^', markersize='8')
# # s2 = ax.plot(x, y2, label='DVCF1', linestyle='--', marker='D', markersize='8')
# # s3 = ax.plot(x, y3, label='DVCF2', linestyle=':', marker='v', markersize='8')
# # s4 = ax.plot(x, y4, label='DVCF3', linestyle='-.', marker='x', markersize='8')
# s5 = ax.plot(x, y5, label='DVCF4', linestyle='--', marker='D', markersize='8')
# # s6 = ax.plot(x, y6, label='DVCF5', linestyle='--', marker='o', markersize='8')
# # s7 = ax.plot(x, y7, label='DVCF6', linestyle=':', marker='>', markersize='8')
# # s8 = ax.plot(x, y8, label='DVCF7', linestyle='-.', marker='*', markersize='8')
# s9 = ax.plot(x, y9, label='DVCF8', linestyle='-.', marker='o', markersize='8')
#
#
# # 设置坐标轴
#
# ax.set_xlabel('table occupancy',
#               fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
# ax.set_ylabel('insert tput ($×$10$^4$)', fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
# # 设置刻度
# ax.tick_params(labelsize=16)
# labels = ax.get_xticklabels() + ax.get_yticklabels()
# [label.set_fontname('Times New Roman') for label in labels]
#
# # 显示网格
# # ax.grid(True, linestyle='-.')
# ax.yaxis.grid(True, linestyle='-.')
# # 添加图例,图例控制,将图例放在一起
# # ss = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
# ss = s1 + s5 + s9
# labs = [l.get_label() for l in ss]
# ax.legend(ss, labs, loc="best", prop={'family': 'Times New Roman', "size": 20})
#
# # plt.legend()
# plt.show()
# fig.savefig('C:/Users/fptjy/Desktop/tu/DVCF_insertthp_load.svg', dpi=600, format='svg')


# ###比较vcf在不同空间利用率下的踢出重放次数
# ##输入因变量
#
# cf = [0.9666666666666667, 6.333333333333333, 27.5, 97.36666666666666, 280.6,
#       707.5333333333333, 1599.4, 3335.0, 6496.966666666666, 12064.6, 21727.766666666666, 38344.86666666667, 67482.8,
#       120961.83333333333, 229126.23333333334, 512983.7, 3591931.8]
# vcf7 = [0.03333333333333333, 0.1, 0.5333333333333333, 1.5333333333333334, 5.1, 14.433333333333334, 37.0,
#         94.96666666666667, 233.9, 559.5333333333333, 1299.3333333333333, 2906.4333333333334, 6314.1, 13479.333333333334,
#         29199.366666666665, 67517.7, 208792.46666666667]
# vcf6 = [0.03333333333333333, 0.16666666666666666, 0.7333333333333333, 2.0, 6.2, 16.9, 43.03333333333333,
#         106.53333333333333, 254.16666666666666, 591.8666666666667, 1354.5, 2982.733333333333, 6459.933333333333,
#         13734.6, 29593.533333333333, 68476.66666666667, 211090.9]
# vcf5 = [0.06666666666666667, 0.3333333333333333, 1.1, 4.166666666666667, 10.7, 26.333333333333332,
#         61.333333333333336, 143.56666666666666, 324.1, 725.9333333333333, 1569.9333333333334, 3333.6666666666665,
#         7001.266666666666, 14599.8, 31078.033333333333, 71052.26666666666, 218507.93333333332]
# vcf4 = [0.06666666666666667, 0.4666666666666667, 1.5, 6.766666666666667, 18.433333333333334,
#         46.03333333333333, 106.96666666666667, 232.66666666666666, 484.43333333333334, 1006.2333333333333, 2024.6,
#         4079.0, 8202.833333333334, 16561.6, 34453.53333333333, 77540.63333333333, 235312.5]
# vcf3 = [0.13333333333333333, 0.8333333333333334, 3.2666666666666666, 12.933333333333334, 35.8,
#         85.96666666666667, 193.23333333333332, 405.1333333333333, 806.5, 1567.7333333333333, 2983.4333333333334,
#         5659.866666666667, 10754.466666666667, 20795.166666666668, 41659.833333333336, 91325.26666666666, 274709.3]
# vcf2 = [0.26666666666666666, 1.7333333333333334, 7.066666666666666, 25.766666666666666,
#         70.56666666666666, 169.13333333333333, 375.8333333333333, 775.9, 1496.8666666666666, 2774.5666666666666,
#         5039.433333333333, 9092.433333333332, 16420.266666666666, 30230.666666666668, 58115.53333333333,
#         123650.16666666667, 371848.5]
# vcf1 = [0.5, 3.1, 13.666666666666666, 49.9, 139.03333333333333, 343.6, 765.2333333333333,
#         1568.2333333333333, 2996.0333333333333, 5502.966666666666, 9795.2, 17138.866666666665, 30023.5,
#         53667.13333333333, 100421.7, 211467.8, 688957.6]
#
# y1 = np.array(cf)
# y2 = np.array(vcf1)
# y3 = np.array(vcf2)
# y4 = np.array(vcf3)
# y5 = np.array(vcf4)
# y6 = np.array(vcf5)
# y7 = np.array(vcf6)
# y8 = np.array(vcf7)
#
# for i in range(len(y1)):
#     y1[i] = math.log(y1[i], 10)
#     y2[i] = math.log(y2[i], 10)
#     y3[i] = math.log(y3[i], 10)
#     y4[i] = math.log(y4[i], 10)
#     y5[i] = math.log(y5[i], 10)
#     y6[i] = math.log(y6[i], 10)
#     y7[i] = math.log(y7[i], 10)
#     y8[i] = math.log(y8[i], 10)
#
# # assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
# fig, ax = plt.subplots(figsize=(6.4, 4.2), dpi=100)
# # ax2 = ax.twinx()
# # 设置自变量的范围和个数
# x = np.linspace(0.01, 0.975, y3.shape[0])
# # 画图
# s1 = ax.plot(x, y1, label='CF', linestyle='-', marker='^', markersize='8')
# s2 = ax.plot(x, y2, label='IVCF1', linestyle='--', marker='D', markersize='8')
# # s3 = ax.plot(x, y3, label='IVCF2', linestyle=':', marker='v', markersize='8')
# # s4 = ax.plot(x, y4, label='IVCF3', linestyle='-.', marker='x', markersize='8')
# # s5 = ax.plot(x, y5, label='IVCF4', linestyle='-', marker='<', markersize='8')
# # s6 = ax.plot(x, y6, label='IVCF5', linestyle='--', marker='o', markersize='8')
# # s7 = ax.plot(x, y7, label='IVCF6', linestyle=':', marker='>', markersize='8')
# s8 = ax.plot(x, y8, label='VCF', linestyle='-.', marker='*', markersize='8')
#
# # 设置坐标轴
# ax.set_xlabel('table occupancy',
#               fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
# ax.set_ylabel('number of evictions (log$_{10}$)', fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
#
# # 设置刻度
# ax.tick_params(labelsize=16)
# labels = ax.get_xticklabels() + ax.get_yticklabels()
# [label.set_fontname('Times New Roman') for label in labels]
#
# # 显示网格
# ax.yaxis.grid(True, linestyle='-.')
# # 添加图例,图例控制,将图例放在一起
# # ss = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
# ss = s1 + s2 +  s8
# labs = [l.get_label() for l in ss]
# ax.legend(ss, labs, loc="best", prop={'family': 'Times New Roman', "size": 20})
#
# plt.show()
# fig.savefig('C:/Users/fptjy/Desktop/tu/IVCF_kicks_load.svg', dpi=600, format='svg')


###比较dvcf在不同空间利用率下的踢出重放次数
##输入因变量

cf = [0.9666666666666667, 6.333333333333333, 27.5, 97.36666666666666, 280.6,
      707.5333333333333, 1599.4, 3335.0, 6496.966666666666, 12064.6, 21727.766666666666, 38344.86666666667, 67482.8,
      120961.83333333333, 229126.23333333334, 512983.7, 3591931.8]
dvcf8 = [0.03333333333333333, 0.1, 0.5333333333333333, 1.5333333333333334, 5.1, 14.466666666666667,
         36.93333333333333, 94.86666666666666, 234.66666666666666, 559.8666666666667, 1302.2666666666667,
         2903.5666666666666, 6317.0, 13477.433333333332, 29155.066666666666, 67445.0, 208736.23333333334]
dvcf7 = [0.16666666666666666, 0.8333333333333334, 3.433333333333333, 12.033333333333333,
         34.833333333333336, 90.43333333333334, 204.4, 423.3333333333333, 838.5666666666667, 1614.7, 3036.5666666666666,
         5692.166666666667, 10675.8, 20175.166666666668, 39693.933333333334, 85111.8, 248799.06666666668]
dvcf6 = [0.36666666666666664, 1.5666666666666667, 6.933333333333334, 24.466666666666665,
         69.1, 174.36666666666667, 385.6333333333333, 784.0333333333333, 1510.2666666666667, 2787.1, 5017.333333333333,
         8906.3, 15725.033333333333, 28112.133333333335, 52471.5, 106962.46666666666, 300217.73333333334]
dvcf5 = [0.4666666666666667, 2.2333333333333334, 9.933333333333334, 35.733333333333334,
         103.33333333333333, 261.26666666666665, 575.1333333333333, 1167.9333333333334, 2227.3, 4057.633333333333,
         7162.833333333333, 12396.0, 21420.766666666666, 37377.433333333334, 67476.2, 133699.0, 368111.0]
dvcf4 = [0.6, 2.933333333333333, 13.466666666666667, 47.03333333333333, 139.2,
         349.46666666666664, 772.0, 1567.5, 2989.5666666666666, 5430.733333333334, 9556.9, 16421.833333333332,
         28011.366666666665, 48172.0, 85936.63333333333, 167632.56666666668, 463644.0333333333]
dvcf3 = [0.7333333333333333, 3.7333333333333334, 17.1, 60.36666666666667,
         176.16666666666666, 437.2, 972.2666666666667, 1978.8333333333333, 3800.4333333333334, 6909.566666666667,
         12162.7, 20874.133333333335, 35547.5, 60916.63333333333, 108232.63333333333, 211484.23333333334,
         603663.9333333333]
dvcf2 = [0.8333333333333334, 4.733333333333333, 20.4, 72.76666666666667,
         209.43333333333334, 523.8, 1167.5, 2400.4666666666667, 4606.133333333333, 8480.6, 14958.266666666666, 25820.9,
         44170.76666666667, 76020.76666666666, 136353.63333333333, 270487.13333333336, 838711.2666666667]
dvcf1 = [0.8666666666666667, 5.466666666666667, 23.9, 85.4, 244.66666666666666, 612.6,
         1381.2666666666667, 2854.7, 5542.433333333333, 10221.366666666667, 18192.4, 31636.9, 54803.76666666667,
         95718.76666666666, 174669.9, 361383.5333333333, 1388450.9666666666]

y1 = np.array(cf)
y2 = np.array(dvcf1)
y3 = np.array(dvcf2)
y4 = np.array(dvcf3)
y5 = np.array(dvcf4)
y6 = np.array(dvcf5)
y7 = np.array(dvcf6)
y8 = np.array(dvcf7)
y9 = np.array(dvcf8)

for i in range(len(y1)):
    y1[i] = math.log(y1[i], 10)
    y2[i] = math.log(y2[i], 10)
    y3[i] = math.log(y3[i], 10)
    y4[i] = math.log(y4[i], 10)
    y5[i] = math.log(y5[i], 10)
    y6[i] = math.log(y6[i], 10)
    y7[i] = math.log(y7[i], 10)
    y8[i] = math.log(y8[i], 10)
    y9[i] = math.log(y9[i], 10)

fig, ax = plt.subplots(figsize=(6.4, 4.2), dpi=100)
x = np.linspace(0.01, 0.975, y3.shape[0])
# 画图
s1 = ax.plot(x, y1, label='CF', linestyle='-', marker='^', markersize='8')
# s2 = ax.plot(x, y2, label='DVCF1', linestyle='--', marker='D', markersize='8')
# s3 = ax.plot(x, y3, label='DVCF2', linestyle=':', marker='v', markersize='8')
# s4 = ax.plot(x, y4, label='DVCF3', linestyle='-.', marker='x', markersize='8')
s5 = ax.plot(x, y5, label='DVCF4', linestyle='--', marker='D', markersize='8')
# s6 = ax.plot(x, y6, label='DVCF5', linestyle='--', marker='o', markersize='8')
# s7 = ax.plot(x, y7, label='DVCF6', linestyle=':', marker='>', markersize='8')
# s8 = ax.plot(x, y8, label='DVCF7', linestyle='-.', marker='*', markersize='8')
s9 = ax.plot(x, y9, label='DVCF8', linestyle='-.', marker='o', markersize='8')

ax.set_xlabel('table occupancy',
              fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})
ax.set_ylabel('number of evictions (log$_{10}$)', fontdict={"family": "Times New Roman", "weight": "normal", "size": 22})

# 设置刻度
ax.tick_params(labelsize=16)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 显示网格
# ax.grid(True, linestyle='-.')
ax.yaxis.grid(True, linestyle='-.')
# 添加图例,图例控制,将图例放在一起
# ss = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
ss = s1 + s5 +  s9
labs = [l.get_label() for l in ss]
ax.legend(ss, labs, loc="best", prop={'family': 'Times New Roman', "size": 20})

# plt.legend()
plt.show()
fig.savefig('C:/Users/fptjy/Desktop/tu/DVCF_kicks_load.svg', dpi=600, format='svg')
