---
title: MyFirstSecurity
tags: 崑山科大
lang: zh-tw
---

{%hackmd theme-dark %}

# 連到遠端伺服器
- 一開始先用 ssh 指令連進去伺服器
    ```shell=
    ssh 帳號@IP:Port
    ```
    - 帳號：lab
    - 密碼：lab
    - IP：120.114.62.206
    - Port：2200

# Linux 101
## Linux CTF 1
- 題目：
    ![](https://i.imgur.com/5jK1lgl.png)

- 先查看 lab 這個使用者的目錄下有什麼檔案與目錄
    ![](https://i.imgur.com/QqBzMJA.png)

- 會看到一個叫 flag 的檔案，然後輸出 flag 的內容
    ```shell
    cat flag
    ```

## Linux CTF 2
- 題目：
    ![](https://i.imgur.com/lnAc3P7.png)

- 先查看 lab 這個使用者的目錄下的所有檔案
    ![](https://i.imgur.com/PuoUH0o.png)
    > -l => 列出此目錄下的檔案和目錄的詳細資訊
    > -a(--all) => 列出此目錄下的所有目錄和檔案(包括隱藏檔)

- 會看到一個叫 .hidden 的檔案，直接輸出 .hidden 的內容就有 Flag 了
    ```shell
    cat .hidden
    ```

## Linux CTF 3
- 題目：
    ![](https://i.imgur.com/2lFlewO.png)

- 這題要把 hex.txt 裡的十六進制的內容轉成 ASCII 的字元
    - hex.txt 內容
        ![](https://i.imgur.com/dYTbfK8.png)

- 使用 linux 的 xxd 指令(也可以用線上的 hex to string 的工具)
    - Linux：
    	```shell
    	xxd [選項] [輸入檔案 [輸出檔案]]
    	xxd -r -ps hex.txt
    	```
    	> -r(reverse) => 將十六進制字串轉成二進制
    	> -ps => 直接將轉換完的字串輸出
    - Online：
        - [HexToString_Online_Decode](https://string-functions.com/hex-string.aspx)

## Linux CTF 4
- 題目：
    ![](https://i.imgur.com/WyosBxj.png)

- base64.txt 內容
    ![](https://i.imgur.com/17pxsyq.png)

- 可以用 Linux 的 base64 或線上的工具去 decode
    - Linux：
        ```shell
        base64 [選項] [檔案]
        base64 -d(--decode) base64.txt
        ```
    - Online：
        - [base64_decode](https://www.base64decode.org/)

## Linux CTF 5
- 題目：
    ![](https://i.imgur.com/Pr8FmZ7.png)

- 要用 find 指令找出 secret 檔案
    ```shell
    find / -name secret 2>/dev/null
    ```
    > / => 因為不知道 secret 檔案所在的確切目錄，所以直接用跟目錄尋找
    > -name => 設定要尋找的檔案名稱
    > 2 => 標準錯誤輸出 => [詳細說明連結](https://blog.gtwang.org/linux/linux-io-input-output-redirection-operators/)
    > /dev/null => 類似 Windows 的資源回收桶

- 最後再直接 cat 出 secret 的內容
    ```shell
    cat /所在目錄/secret
    ```

# Linux 102
## Linux CTF 6
## Linux CTF 7
## Linux CTF 8
## Linux CTF 9
## Linux CTF 10