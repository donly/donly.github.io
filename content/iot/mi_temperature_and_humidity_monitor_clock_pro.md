Title: 小米温湿度计 PRO 使用
Slug: mi_temperature_and_humidity_monitor_clock_pro
Tags: iot, mi, 小米, 米家, 蓝牙, ble
Date: 2022-03-08 15:00

这个产品购于 2020 年底，价格 68 元仅供参考。

![小米温湿度计PRO版](images/iot/mi_temperature_and_humidity_monitor_clock_pro.jpg)

## 主要特点
* 型号： LYWSD02MMC
* 电池规格：CR2032 x2，于 2022 年 3 月换了电池，可见原机电池可以使用 2 年；
* 无线连接：蓝牙 BLE 4.0/5.0，不占用无线路由器资源，需米家蓝牙网关配网；
* 屏幕：电子墨水大屏，全部显示内容如下：

![小米温湿度计PRO屏幕，图片来源见水印](images/iot/1098-mi-pro-01.png)


## 方案
* 温湿度传感器：SHTC3（精度：±2 %RH and ±0.2 °C），[数据手册下载](https://www.mouser.com/datasheet/2/682/Sensirion_Humidity_Sensors_SHTC3_Datasheet-1386761.pdf)
* 无线模块：低功耗蓝牙5.0/MCU DA14585
* RTC时钟芯片：BM8563，广告说高精度时钟芯片，经使用发现半年左右有3分钟左右误差
 
## 使用
TBD

## 参考资料
1. [电子温湿度计Pro立即购买-小米商城](https://www.mi.com/buy/detail?product_id=9542)
2. ["高精度"米家电子温湿度计Pro拆解-Arduino中文社区](https://www.arduino.cn/thread-91956-1-1.html)
3. [米家电子温湿度计 Pro 拆机 | 垃圾站](https://cyhour.com/1098/)
