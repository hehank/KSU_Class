#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ? 結果沒用到
# ? 小寫字母集
# low_alpha = [chr(x) for x in range(97, 123)]
# ? 大寫字母集
# up_alpha = [chr(x) for x in range(65, 91)]

# ? 密文
# cipher = '7SJ-IGHM-742Q3W4T'
cipher = 'xyzqc\{t3_qelrdeq_t3_k33a3a_lk3_lc_qe3p3\}'
cipher = 'ERTKSOOTCMCHYRAFYLIPL'

# ? 明文
plain = ''

# ? 預設解 key = 1 - 100
for i in range(1, 101):
    for j in cipher:
        # ? 判斷是否為英文字母
        if (not (j.isalpha())):
            plain += j
            continue
        # ? 判斷大寫字母
        elif j.isupper():
            plain += chr(((ord(j) + i) % 65 % 26) + 65)
        # ? 小寫字母
        else:
            plain += chr(((ord(j) + i) % 97 % 26) + 97)
    # ? 輸出 => Shift key : plaintext
    print(f"Shift {i} : {plain}")
    # ? 重置 plain
    plain = ''
