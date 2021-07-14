"""
Hash utilities for cuckoo filters to generate fingerprints.

Generate FNV64 hash based on http://isthe.com/chongo/tech/comp/fnv/
"""

FNV64_OFFSET_BASIS = 0xcbf29ce484222325
FNV64_PRIME = 0x100000001b3
MAX_64_INT = 2 ** 64
MAX_32_INT = 2 ** 32


def _fnv64(data):
    """
    Generate FNV64 hash for data in bytes

    :param data: Data to generate FNV hash for
    """
    assert isinstance(data, str)

    h = FNV64_OFFSET_BASIS
    for byte in data.encode():          # 字符串通过调用encode函数转换成bytes
        h = (h * FNV64_PRIME) % MAX_64_INT
        h ^= byte
    return abs(h)


def _int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, byteorder='big')   # x.bit_length()是返回x二进制的位数，//运算是先做除法，然后向下取整


def _bytes_to_int(x):
    return int.from_bytes(x, byteorder='big')  # 将bytes类型的变量x，转换成10进制整数，并返回


# def fingerprint(data, size):
#     """
#     Get fingerprint of a string using FNV 64-bit hash and truncate it to
#     'size' bytes.
#
#     :param data: Data to get fingerprint for
#     :param size: Size in bytes to truncate the fingerprint
#     :return: fingerprint of 'size' bytes
#     """
#     fp = _int_to_bytes(_fnv64(data))
#     return _bytes_to_int(fp[:size])

def fingerprint(data, size):
    """
    Get fingerprint of a string using FNV 64-bit hash and truncate it to
    'size' bytes.

    :param data: Data to get fingerprint for
    :param size: Size in bytes to truncate the fingerprint
    :return: fingerprint of 'size' bytes
    """
    fp = _int_to_bytes(_fnv64(data))
    if size <= 8:
        return _bytes_to_int(fp[:1]) % 2 ** size
    elif size > 8 and size <= 16:
        return _bytes_to_int(fp[:2]) % 2 ** size
    elif size > 16 and size <= 24:
        return _bytes_to_int(fp[:3]) % 2 ** size
    elif size > 24 and size <= 32:
        return _bytes_to_int(fp[:4]) % 2 ** size
    elif size > 32 and size <= 40:
        return _bytes_to_int(fp[:5]) % 2 ** size
    elif size > 48 and size <= 56:
        return _bytes_to_int(fp[:6]) % 2 ** size
    elif size > 56 and size <= 64:
        return _bytes_to_int(fp[:7]) % 2 ** size


def hash_code(data):
    """Generate hash code using builtin hash() function.

    :param data: Data to generate hash code for
    """
    # h = 0
    # for c in data:
    #     h = (ord(c) + (31 * h)) % MAX_32_INT
    # return h
    return abs(hash(data))


