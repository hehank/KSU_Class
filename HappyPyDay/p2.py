#! /usr/bin/env python3
# -*- coding: utf-8 -*-

profit = int(input("清輸入利潤 : "))

pro_level = [1000000, 600000, 400000, 200000, 100000, 0]
get = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
total = 0

for i in range(0, 6):
    if profit > pro_level[i]:
        total += (profit - pro_level[i]) * get[i]
        profit = pro_level[i]
print(total)
