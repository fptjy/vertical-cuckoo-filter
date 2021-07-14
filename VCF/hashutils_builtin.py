import hashlib
MAX_32_INT = 2 ** 32
#
# ### Generate hash code using builtin hash() function
# def hash_code1(data):
#     """Generate hash code using builtin hash() function.
#
#     :param data: Data to generate hash code for
#     """
#     h = 0
#     for c in data:
#         h = (ord(c) + (31 * h)) % MAX_32_INT
#     return h
#     # return abs(hash(data))
#
# def fingerprint(data, size):
#     fp = hash_code1(data)
#     fp = fp % size
#
#     return fp
#
# def hash_code(data):
#     """Generate hash code using builtin hash() function.
#
#     :param data: Data to generate hash code for
#     """
#     # h = 0
#     # for c in data:
#     #     h = (ord(c) + (31 * h)) % MAX_32_INT
#     # return h
#     return abs(hash(data))


# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

def md5(data):
    m = hashlib.md5()
    b = data.encode(encoding='utf-8')
    m.update(b)
    data_md5 = m.hexdigest()
    return data_md5

def hash_code1(data):
    """Generate hash code using builtin hash() function.

    :param data: Data to generate hash code for
    """
    h = 0
    for c in md5(data):
        h = (ord(c) + (31 * h)) % MAX_32_INT
    return h
    # return abs(hash(data))

def fingerprint(data, size):
    fp = hash_code1(data)
    fp = fp % size

    return fp

def hash_code(data):
    """Generate hash code using builtin hash() function.

    :param data: Data to generate hash code for
    """
    # h = 0
    # for c in data:
    #     h = (ord(c) + (31 * h)) % MAX_32_INT
    # return h
    return abs(hash(data))

