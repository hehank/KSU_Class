#! /usr/bin/env python3
# -*- coding: utf-8 -*-

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
up_alpha = [chr(x) for x in range(65, 91)]
low_alpha = [chr(x) for x in range(97, 123)]

for i in number:
    up_alpha.append(i)
    low_alpha.append(i)


def decode(cipher, key):
    plain = ""
    length = -1 * len(up_alpha)

    for i in cipher:
        index = 0
        char = ""
        deter = False

        if ((i not in up_alpha) and (i not in low_alpha)):
            plain += i
            continue

        for j in up_alpha:
            if (i == j):
                index = up_alpha.index(j)
                char = up_alpha[(index - key) % length]
                plain += char
                deter = True
                break

        if deter:
            continue

        # for k in low_alpha:
        #     if (i == k):
        #         index = low_alpha.index(k)
        #         char = low_alpha[(index + key) % length]
        #         break

        for k in low_alpha:
            if (i == k):
                index = low_alpha.index(k)
                char = up_alpha[(index - key) % length]
                plain += char
                break

    return plain


def encode(cipher, key):
    plain = ""
    length = len(up_alpha)

    for i in cipher:
        index = 0
        char = ""
        deter = False

        if ((i not in up_alpha) and (i not in low_alpha)):
            plain += i
            continue

        for j in up_alpha:
            if (i == j):
                index = up_alpha.index(j)
                char = up_alpha[(index + key) % length]
                plain += char
                deter = True
                break

        if deter:
            continue

        for k in low_alpha:
            if (i == k):
                index = low_alpha.index(k)
                char = low_alpha[(index + key) % length]
                break

        # for k in low_alpha:
        #     if (i == k):
        #         index = low_alpha.index(k)
        #         char = up_alpha[(index + key) % length]
        #         plain += char
        #         break

    return plain


# cipher = '7sj-ighm-742q3w4t'
cipher = "7sj-ighm-742q3w4t"
key = 16

# print(encode(cipher, key))
print(decode(cipher, key))
