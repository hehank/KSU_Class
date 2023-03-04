#! /usr/bin/env python3
# -*- coding: utf-8 -*-

num_list = ['1', '2', '3', '4', '5', '6']
str_list = []
total = 0

for i in range(0, 6):
    for j in range(0, 6):
        for k in range(0, 6):
            if (num_list[i] == num_list[j]) or (num_list[j] == num_list[k]) or (num_list[i] == num_list[k]):
                continue
            else:
                total += int(num_list[i] + num_list[j] + num_list[k])

print(total)
