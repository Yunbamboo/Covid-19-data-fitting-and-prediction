# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

#全国除湖北外累计确诊
x = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
y1 = [558,923,1321,1801,2420,3125,3886,4638,5306,6028,6916,7646,8353,9049,9593,10098,10540,10910,11287,11598,11865,12086,12251,12366,12447,12503]
f1 = np.polyfit(x, y1, 2)
f2 = np.poly1d(f1)
print('f2 is :\n',f2)
yvals1 = f2(x)  #拟合y值

#全国除湖北外现有确诊
#绘图
plt.rcParams['font.sans-serif']=['SimHei']
plot1 = plt.plot(x, y1, 's',label="累计患者数量",color='blue')
plot2 = plt.plot(x, yvals1, 'r',label="拟合曲线",color='red')
plt.xlabel('统计天数')
plt.ylabel('人数')
plt.legend(loc=2) #指定legend的位置右下角
plt.title("二次拟合")
plt.show()