#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:19:12 2016
@author: ys-budakyan
"""
import numpy as np



# Daniel J. Bernstein hash function
def DJBHash(key, N):
    hashDJB = 0
    for s in key:
        hashDJB = ((hashDJB << 5) + hashDJB) + ord(s)
    return (hashDJB & 0x7FFFFFFF) % N

def fingerprint(data, size):
    fp = DJBHash(data, 2**size)
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

