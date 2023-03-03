#! /usr/bin/env python3
# -*- coding: utf-8 -*-

num_list = [0, 1]
i = 2

while i <= 41:
    num_list.append((num_list[i-1] + num_list[i-2]))
    i += 1

print(num_list[-1])
