---
title: 第二章 WWW
tags: KSU_exam
lang: zh-tw
---

{%hackmd theme-dark %}

# 第二章 WWW
## [URL](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E5%AE%9A%E4%BD%8D%E7%AC%A6) (see p30-p31)
- Uniform Resource Locator，全球資源定位器。
- 用途：識別網頁儲存在 Internet 何處。
- 標準格式：
    ![](https://i.imgur.com/Iz2Y7cq.png)

## [HTTP](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)
- HyperText Transfer Protocol，超文本傳輸協定。
- 是一種應用層協定。
- 是一個 Client site（User）和 Server site（Website）之間 request 和 response 的標準。
- 通常使用TCP。
- 預設埠(Port)：80。

## [HTTPS](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE)
- HyperText Transfer Protocol Secure，超文本傳輸安全協定。
- 利用 [SSL / TLS](https://zh.wikipedia.org/wiki/%E5%82%B3%E8%BC%B8%E5%B1%A4%E5%AE%89%E5%85%A8%E6%80%A7%E5%8D%94%E5%AE%9A) 來加密封包。
- 是一種應用層協定。
- 開發目的：
    - 提供對網站伺服器的身分認證。
    - 保護交換資料的隱私與完整性。
- 預設埠(Port)：443。

### XAMPP HTTPS
- [XAMPP 設定 HTTPS 開發環境](https://vector.cool/xampp-apache-https-in-localhost/)

## [IP Address](https://zh.wikipedia.org/wiki/IP%E5%9C%B0%E5%9D%80)
- Internet Protocol Address。
- 用途：
    - 辨別 Internet 上的每一台機器(不會出現重複 IP)。
- 組成：
    - [IPv4](https://zh.wikipedia.org/wiki/IPv4)（32bit）
        - 四個 8 bit(0 ~ 255) 的數字組成，每組之間用`.`相隔。
        - 例：8.8.8.8。
    - [IPv6](https://zh.wikipedia.org/wiki/IPv6)(128bit)
        - 八個 4 bit的`十六進制`數字組成，每組之間用`:`相隔。
        - 例：2001:0db8:86a3:08d3:1319:8a2e:0370:7344
- 表達方式：
  - IPv4：dot-decimal notation

## domain name ==> 整個企業
- google.com網域
- ns1.google.com ==> 某一個伺服器
- ns2.google.com ==> 某一個伺服器
- www.google.com ==> 某一個伺服器
- TLD ==> Top level domain
- com ==>  
- edu ==>
- gov ==> 

## web
- web server ==> apache
- web application ==> 你寫的程式

## 資訊`素養`（information `literacy`） 
```
現代人如何能有效率的找到、評估、使用和傳達線上資訊
能做到下列這些事：
  參考多種資訊來源，包括 Internet、線上圖書館和媒體網站
  選擇正確的工具找到需要的資訊
  體認到並非所有資訊都生而平等
  評估資訊是否會使人誤解、偏頗或已經過時
  駕馭資訊成為讓自己成為具備知識的決策者
```

## SEO(Search engine optimization)

## CARS
```
CARS（credibility, accuracy, reasonableness, support）查核清單（checklist）
可信度（credibility）：找出作者，了解他們的身分
正確性（accuracy）：確認它的事實來源和主張，了解它是否有特定立場或偏見
合理性（reasonableness）：要考慮線上來源的內容是否公正且合乎情理
支持度（support）：找找看聲譽良好的來源或機構
```
## 
## Creative Commons（CC）
- 是個`非營利`機構
- 它協助讓`內容創作者`能保有自己創作素材的`版權`
- 同時還能讓`他人使用、複製或散布`他們的作品