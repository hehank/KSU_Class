#! /usr/bin/env python3
# -*- coding: utf-8 -*-

annual_performance = 2245678
bonus = 0

if annual_performance <= 1000000:
    bonus = round(annual_performance * 0.1, 0)
elif annual_performance < 2000000:
    bonus = round((annual_performance - 1000000) * 0.07, 0)
elif annual_performance < 4000000:
    bonus = round((annual_performance - 2000000) * 0.05, 0)
elif annual_performance < 6000000:
    bonus = round((annual_performance - 4000000) * 0.04, 0)
elif annual_performance < 10000000:
    bonus = round((annual_performance - 6000000) * 0.02, 0)
else:
    bonus = round((annual_performance - 10000000) * 0.01, 0)

print(bonus)
