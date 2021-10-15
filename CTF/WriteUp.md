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
- 題目：
    ![](https://i.imgur.com/76pJRY5.png)

- 可以使用 Linux 查看 Process 的指令
    ```shell
    ps aux => 查閱所有系統運作的程序
    ```
    - 各欄位的意義
        | 名稱    | 意義                                                                                                                                                        |
        | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | USER    | 該 process 屬於那個使用者帳號                                                                                                                               |
        | PID     | 該 process 的程序識別碼                                                                                                                                     |
        | %CPU    | 該 process 使用掉的 CPU 資源百分比                                                                                                                          |
        | %MEM    | 該 process 所佔用的實體記憶體百分比                                                                                                                         |
        | VSZ     | 該 process 使用掉的虛擬記憶體量 (Kbytes)                                                                                                                    |
        | RSS     | 該 process 佔用的固定的記憶體量 (Kbytes)                                                                                                                    |
        | TTY     | 該 process 是在那個終端機上面運作，若與終端機無關則顯示『?』 ，另外， tty1-tty6 是本機上面的登入者程序，若為 pts/0 等等的，則表示為由網路連接進主機的程序。 |
        | STAT    | 該程序目前的狀態，狀態顯示與 ps -l 的 S 旗標相同 (R/S/T/Z)                                                                                                  |
        | TIME    | 該 process 實際使用 CPU 運作的時間。                                                                                                                        |
        | COMMAND | 該程序的實際指令為何？                                                                                                                                      |
    - [Reference_Link](http://linux.vbird.org/linux_basic/0440processcontrol.php#ps)
- 會看到一個在 COMMAND 欄位的開頭是 socat 的，可以看的出來是使用 socat 指令在監聽 2111 port(TCP-LISTEN:2111)，那後面還有一個 fork EXEC:/bin/flag ，也就是說當你連過去 2111 port 就可以接收到它想傳給你的 flag 了
    ![](https://i.imgur.com/981LnaB.png)

- 可以直接用 nc 連過去 2111 port，因為那行指令是在同一個伺服器執行的，所以 IP 可以直接用 localhost(127.0.0.1)，就會得到 Flag 了
    ```shell
    nc localhost(or 127.0.0.1) 2111
    ```

## Linux CTF 7
- 題目：
    ![](https://i.imgur.com/1Y44dTw.png)

- 

## Linux CTF 8
- 題目：
    ![](https://i.imgur.com/R2gm3Ij.png)

- Linux 下載鏈結檔案
    ```shell
    wget http://120.114.62.217/ForYou.tar.gz
    ```
    ![](https://i.imgur.com/rB5gkxz.png)

- 解開 .tar.gz 的 Linux 指令
    ```shell
    tar [Option] [File]
    tar -zxvf ForYou.tar.gz
    ```
    ![](https://i.imgur.com/v742EmU.png)

    > -z(--gzip) => 解開 .gz
    > -x(--extract) => 解開 .tar
    > -v(--verbose) => 列出解開的檔案中的東西
    > -f(--file=ARCHIVE) => 指定要解開的檔案

- 查看解開的檔案的檔案類型
    ```shell
    file [Option] [File]
    file ForYou
    ```
    ![](https://i.imgur.com/YKkfjdm.png)

- 發現是文字檔，就直接輸出檔案內容就好了
    ```shell
    cat ForYou
    ```

## Linux CTF 9
- 題目：
    ![](https://i.imgur.com/YfWI86r.png)

- Linux 下載鏈結檔案
    ```shell
    wget http://120.114.62.217/TobeExe
    ```
    ![](https://i.imgur.com/LzPGtYc.png)

- 用 ls 看起來是一般的檔案，就先用 file 看看是哪種類型的檔案
    ```shell
    file TobeExe
    ```
    ![](https://i.imgur.com/91edjXa.png)

- 原來是一個 ELF 的執行檔，那就用 ls -l 去看檔案的權限
    - 檔案屬性
        ![](https://i.imgur.com/EpKH5ME.png)

- 發現沒有執行的權限，這時候就需要讓 TobeExe 有執行的權限，有了之後會看到檔名變綠色的
    ```shell
    chmod +x TobeExe
    ```
    ![](https://i.imgur.com/oZY3aRp.png)

    > +x => execute
    
- 再用 ls -l 看一次，就會發現 TobeExe 有了執行權限，就可以直接執行 TobeExe
    - 執行 TobeExe
        ```shell
        ./TobeExe
        ```
        > 『.』 => 當前目錄
        
## Linux CTF 10
- 題目：
    ![](https://i.imgur.com/1dc9PJo.png)
    
- Linux 下載鏈結檔案
    ```shell
    wget http://120.114.62.217/reverse
    ```
    
- 一樣先用 file 查看檔案類型，再使用 ls -l， 一樣發現沒有執行權限
    - 加權限
        ```shell
        chmod +x reverse
        ```
    ![](https://i.imgur.com/cbDsliB.png)

- 執行 reverse 之後會看到
    ![](https://i.imgur.com/V1NSAi1.png)

- Linux 有一個叫 strings 的工具，會把檔案中可顯示的字串顯示出來，就可以找到 flag 了
    ```shell
    strings [option(s)] [file(s)]
    strings reverse
    ```