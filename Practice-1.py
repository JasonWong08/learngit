#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

"""
Author: wangjf
date: 2019/5/31 16:14
desc:
"""

i = 200
f = 99.88
print(i)
print(type(i))
print(f)
print(type(f))

hex_value1 = 0x16
hex_value2 = 0XbC
print("hexValue1的值为：", hex_value1)
print("hexValue2的值为：", hex_value2)
# 以0b或0B开头的整数数值是二进制的整数
bin_val = 0b111
print('bin_val的值为：', bin_val)
bin_val = 0B101
print('bin_val的值为:', bin_val)
# 以0o或0O开头的整数数值是八进制的整数
oct_val = 0o56
print('oct_val的值为:', oct_val)
oct_val = 0O11
print('oct_val的值为:', oct_val)

af1 = 6.1234566
# 输出af1的值
print("af1的值为:", af1)
af2 = 26.3456
print("af2的类型为:", type(af2))
f1 = 6.12e2
print("f1的值为;", f1)
f2 = 5e2
print("f2的类型为:", type(f2))    # 看到类型为float

ac1 = 3 + 0.3j
print(ac1)
print(type(ac1))
ac2 = 5 - 0.2j
print(ac2)
# 复数运算
print(ac1 + ac2)  # 输出 （8 + 0.1j）

