#! /usr/bin/env python3
# -*- coding: utf-8 -*-

profit = int(input("清輸入利潤 : "))

pro_level = [10000000, 6000000, 4000000, 2000000, 1000000, 0]
get = [0.01, 0.02, 0.04, 0.05, 0.07, 0.1]
total = 0

for i in range(0, 6):
    if profit > pro_level[i]:
        total += (profit - pro_level[i]) * get[i]
        profit = pro_level[i]
print(total)
