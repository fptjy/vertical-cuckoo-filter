### Generate murmurhash

import ctypes

def int_overflow(val):
    # 实现溢出能力
    # maxint = 2147483647
    maxint = 2**14
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val

# 逻辑右移，给出r默认值24，这里没用到
def unsigned_right_shitf(n, r = 24):
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if r < 0:
        return -int_overflow(n << abs(r))
    return int_overflow(n >> r)

# 大数乘法，m = 0x5bd13995 = 1540483477
def int_overflow_multiplication(a, m = 1540483477):
    result = a * m
    result = int_overflow(result)
    return result

# seed 可以改自己的
def fingerprint(origin_string, seed = 111111):
    origin_bytes = origin_string.encode()

    length = len(origin_bytes)
    h = seed ^ length
    i = 0
    r = 24
    const = 0xff

    while (length >= 4):

        k = (origin_bytes[i] & const) + ((origin_bytes[i + 1] & const) << 8) + ((origin_bytes[i + 2] & const) << 16) + ((origin_bytes[i + 3] & const) << 24)
        k = int_overflow_multiplication(k)
        k ^= k >> r
        k = int_overflow_multiplication(k)
        h = int_overflow_multiplication(h)
        h ^= k
        length -= 4
        i += 4

    if (length == 3):
        h ^= (origin_bytes[i + 2] & const) << 16
        h ^= (origin_bytes[i + 1] & const) << 8
        h ^= (origin_bytes[i] & const)
        h = int_overflow_multiplication(h)

    if (length == 2):
        h ^= (origin_bytes[i + 1] & const) << 8
        h ^= (origin_bytes[i] & const)
        h = int_overflow_multiplication(h)

    if (length == 1):
        h ^= (origin_bytes[i] & const)
        h = int_overflow_multiplication(h)

    h ^= h >> 13
    h = int_overflow_multiplication(h)
    h ^= h >> 15

    return h


def hash_code(data):
    """Generate hash code using builtin hash() function.

    :param data: Data to generate hash code for
    """
    # h = 0
    # for c in data:
    #     h = (ord(c) + (31 * h)) % MAX_32_INT
    # return h
    return abs(hash(data))


