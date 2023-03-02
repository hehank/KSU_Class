def scytale_decrypt(ciphertext, key):
    # 計算每個帶子的字符數
    num_cols = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        num_cols += 1

    # 將密文分成 num_cols 列
    matrix = [''] * num_cols
    col = 0
    for c in ciphertext:
        matrix[col] += c
        col = (col + 1) % num_cols

    # 按列讀取字符
    plaintext = ''
    for row in range(num_cols):
        plaintext += matrix[row]

    return plaintext


if __main__ == '__main__':
    ciphertext = 'SDNOLEAEERTRCROACNDFMTNIEOOAE__'
    key = 5

    plaintext = scytale_decrypt(ciphertext, key)
    print(plaintext)
