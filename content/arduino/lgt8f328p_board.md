Title: LGT8F328P Arduino Nano3 兼容板的使用
Slug: lgt8f328p_nano3_compatible_board
Tags: arduino, nano
Date: 2019-05-19
Modified: 2022-02-16 17:40

## 介绍
LGT8F328P LQFP32，是一款替代 NANO V3.0 的廉价解决方案，在淘宝上买到的一般长这样：
![LGT8F328P](images/arduino/LGT8F328P.png)

[ALPHA 8F328P-U](http://www.ocrobot.com/doku.php?id=ocrobot:alpha:8f328p-u:main) 所使用的 MCU 为LGT8F328P，是一款 Atmel MEGA328P 兼容芯片。USB 芯片使用的是合泰 HT42B534-1，WIN10和MAC OS X免驱。由 [OCROBOT](http://www.ocrobot.com/doku.php?id=start) 设计，板载USB 至 UART。

## 安装
<del>ALPHA 8F328P-U是一款Arduino兼容的开发板。可以使用Arduino IDE进行开发（需要自己安装支持），参考 https://github.com/donly/Larduino_HSP#installation. </del>

目前版本 Arduino IDE 是 `1.8.19` 已经自带支持。


## 使用
![Arduino Nano](images/arduino/nano_8f328p_setup.png)

## 测试
使用 `Blink` 例程