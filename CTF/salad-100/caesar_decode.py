#! /usr/bin/env python3
# -*- coding: utf-8 -*-

low_alpha = [chr(x) for x in range(97, 123)]
up_alpha = [chr(x) for x in range(65, 91)]
# cipher = '7SJ-IGHM-742Q3W4T'
cipher = '7sj-ighm-742q3w4t'
str_out = ''

for i in range(1, 101):
    for j in cipher:
        if (j not in up_alpha) and (j not in low_alpha):
            str_out += j
            continue
        elif j.isupper():
            str_out += chr(((ord(j) + i) % 65 % 26) + 65)
        else:
            str_out += chr(((ord(j) + i) % 97 % 26) + 97)
    print(f"Shift {i} : {str_out}")
    str_out = ''
