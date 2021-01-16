###编写四个函数依次实现：4进制转10进制，10进制转4进制，4进制异或运算规则表，4进制异或运算###

# n = int(input('请输入要转换进制的数值：'))
def ten_to_four(n):
    b = []  # 存储余数
    while True:  # 一直循环，商为0时利用break退出循环
        s = n // 4  # 商
        y = n % 4  # 余数
        b = b + [y]  # 每一个余数存储到b中
        if s == 0:
            break  # 余数为0时结束循环
        n = s
    b.reverse()  # 使b中的元素反向排列
    return b


def four_to_ten(n):
    b = 0
    c = len(n) - 1
    for i in range(len(n)):
        b = b + n[i] * 4 ** c
        c = c - 1
    return b


def base_four_xor(a, b):
    s = []
    if len(a) - len(b) >= 0:
        max_one = a
        min_one = b
    else:
        max_one = b
        min_one = a

    l = len(min_one)
    for i in range(len(max_one) - l):
        s.append(max_one[i])
    for i in range(l):
        s.append((max_one[len(max_one) - l + i] + min_one[i]) % 4)
    return s

# x = ten_to_four(12322022)
# y = ten_to_four(932)
# print(x)
# print(y)
#
# s = x
# for i in range(4):
#     s = base_four_xor(s, y)
#     print("s", s)
#
# print(four_to_ten(x))
# print(four_to_ten(s))


# from four_ary_cf14_7 import D_ary_CF14_7
# dcf = D_ary_CF14_7(capacity=8, bucket_size=4, fingerprint_size=14)
#
# y = dcf._get_index("sss")
# print(y)
#
# x = dcf.I_insert0("ddd")
# print(dcf.I_contains0("ddd"))