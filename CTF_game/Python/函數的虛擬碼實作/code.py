#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def xxx(m, n):
    while m != 0:
        if n == 0:
            n = 1
        else:
            n = xxx(m, n-1)

        m -= 1
    return n + 1


num = xxx(2, 2)
print(num)
