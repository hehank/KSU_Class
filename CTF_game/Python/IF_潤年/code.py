#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

date_str = "20001023"
dt_str = datetime.datetime.strptime(date_str, "%Y%m%d")

date_init = date_str[:4] + "0101"
dt_init = datetime.datetime.strptime(date_init, "%Y%m%d")

days = int((dt_str - dt_init).days) + 1
print(days)
