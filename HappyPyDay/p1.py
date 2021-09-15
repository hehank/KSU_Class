#! /usr/bin/env python3
# -*- coding: utf-8 -*-

count = 0

for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            continue
        for k in range(1, 5):
            if (i != k) and (j != k):
                count += 1
                num = str(i) + str(j) + str(k)
                print(num)
print(f"total : {count}")
