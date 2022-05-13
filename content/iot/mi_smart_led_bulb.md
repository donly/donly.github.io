Title: 米家 LED 灯泡蓝牙 MESH 版使用
Slug: mi_smart_led_bulb
Tags: iot, mi, 小米, 米家, 蓝牙, ble, mesh
Date: 2022-03-08 15:00

这个智能灯泡购于2022年03月，PDD卖18元。

![米家LED灯泡蓝牙mesh版，图片来源www.xdea.xyz](images/iot/mi_smart_led_pcb.jpg)

## 主要特点
* 灯泡型号：MJDP09YL
* 灯头规格：E27
* 功率：5W，16x1W/LED
* 无线连接：蓝牙 BLE 5.0，不占用无线路由器资源，需米家蓝牙网关配网
* 其它：支持凌动开关

## 方案
* 驱动：由一枚晶丰明源的 BP5778 线性恒流芯片驱动16颗灯珠，暖色冷色各8颗
* 无线模块：小米推出的 6 元 BLE Mesh 模组，MHCB05P 是基于 Realtek 的 RTL8762CMF 高性能的 BLE 模组， 内置 ARM Cortex-M4F 核， 高发射功率 7.5dbm，相关开发资料参考：https://www.shenzhenware.com/articles/13630.
* 其它主要元件：
  - BT10S 整流桥，将交流电转换成直流；
  - 一颗晶丰明源的 BP8519C，用于 3.3v 稳压；
  - 有一路火线用于灵动模式的相位检测；
 
## 使用
下载米家App，先将蓝牙打开再添加设备。这种方式只能近距离遥控，如果需要远程遥控需要搭配米家的蓝牙网关使用。

## 参考资料
1. [Mi Smart LED Bulb (Warm White)](https://www.mi.com/global/mi-smart-led-bulb-warm-white/)
2. [米家LED灯泡蓝牙MESH版拆解 – Xdea](https://www.xdea.xyz/2021/06/%E7%B1%B3%E5%AE%B6led%E7%81%AF%E6%B3%A1%E8%93%9D%E7%89%99mesh%E7%89%88%E6%8B%86%E8%A7%A3/)
3. [米家LED灯泡蓝牙mesh版拆解 - 拆机乐园 数码之家](https://www.mydigit.cn/thread-219664-1-1.html)
