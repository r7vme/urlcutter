#!/usr/bin/env python

ALPHABET = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
BASE = 58

def base_encode(num):
    string = ""
    while num > 0:
        remainder = num % BASE
        string = ALPHABET[remainder] + string
        num //= BASE
    return string

def base_decode(string):
    num = 0
    i = 0
    for ch in reversed(string):
        num += ALPHABET.index(ch) * BASE ** i
        i += 1
    return num
