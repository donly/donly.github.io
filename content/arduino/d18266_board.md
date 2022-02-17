Title: D1 Arduino 8266EX 兼容板的使用
Slug: d1_arduino_8266_compatible_board
Date: 2019-05-29

## 介绍
[D1](https://wiki.wemos.cc/products:d1:d1#technical_specs)，是一款替代 Arduino UNO 8266 的廉价解决方案，在淘宝上买到的一般长这样：

![D1](images/arduino/d1.jpg)


## 安装
这是一款 Arduino 兼容的开发板，可以使用 Arduino IDE 进行开发，参考 [installing-with-boards-manager](https://github.com/esp8266/Arduino#installing-with-boards-manager)

## 使用
![在 macOS Arduino 上的使用参数](images/arduino/d1_arduino_setup.png)

## 测试
使用 `WiFiScan` 例程测试，运行后我的串口输出结果：
```
22:03:29.798 -> scan start
22:03:31.952 -> scan done
22:03:31.952 -> 8 networks found
22:03:31.952 -> 1: long (-74)*
22:03:31.985 -> 2: Home_2018 (-91)*
22:03:31.985 -> 3: Home_2018 (-86)*
22:03:31.985 -> 4: TP-LINK_2F1A (-81)*
22:03:32.018 -> 5: ChinaNet-ZQRK (-90)*
22:03:32.018 -> 6: 2503 (-92)*
22:03:32.018 -> 7: OpenWrt (-70)*
22:03:32.018 -> 8: ChinaNet-qwtx (-83)*
```