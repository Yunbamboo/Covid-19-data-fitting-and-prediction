# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#自定义指数函数
def func(x, a, b, c):
    return a * np.exp(x * b) + c
#全国除湖北外累计确诊
x = [4,5,6,7,8,9,10,11,12,13,14]
x=np.array(x)
num = [558,923,1321,1801,2420,3125,3886,4638,5306,6028,6916]
y = np.array(num)
popt, pcov = curve_fit(func, x, y, maxfev=5000)
#获取popt拟合系数
a = popt[0]
b = popt[1]
c = popt[2]

yvals =  func(x, a, b, c)#拟合y值
print('系数a:', a)
print('系数b:', b)
print('系数c:', c)


#绘图
plt.rcParams['font.sans-serif']=['SimHei']
plot1 = plt.plot(x, y, 's',label="累计患者数量",color='blue')
plot2 = plt.plot(x, yvals, 'r',label="拟合曲线",color='red')
plt.xlabel('统计天数')
plt.ylabel('人数')
plt.legend(loc=2) #指定legend的位置右下角
plt.title("早期指数拟合")
plt.show()