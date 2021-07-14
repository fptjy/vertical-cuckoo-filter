#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:19:12 2016
@author: ys-budakyan
"""
import numpy as np


# Peter J. Weinberger hash function
def PJWHash(key, N):
    # BI, TQ, OE, HB constants
    BitsInUnsignedInt = 4 * 8
    ThreeQuarters = int((BitsInUnsignedInt * 3) / 4)
    OneEighth = int(BitsInUnsignedInt / 8)
    HighBits = (0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth)

    hashPJW = 0
    hashHB = 0
    for s in key:
        hashPJW = (hashPJW << OneEighth) + ord(s)
        hashHB = hashPJW & HighBits
        if hashHB != 0:
            hashPJW = ((hashPJW ^ (hashHB > ThreeQuarters)) & (~HighBits))
    return (hashPJW & 0x7FFFFFFF) % N

def fingerprint(data, size):
    fp = PJWHash(data, 2**size)
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
