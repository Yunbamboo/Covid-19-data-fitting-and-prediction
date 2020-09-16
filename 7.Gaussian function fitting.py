
"""
Created on Mon Feb 10 10:35:43 2020

@author: hy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


#自定义高斯函数
def func(x, a,u, sig):
    return  a*(np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig))


#定义x、y散点坐标
x = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
x=np.array(x)
print('x is :\n',x)
num = [365,398,480,619,705,761,752,668,722,888,730,707,696,544,505,442,370,377,311,267,221,165,115,81,56]
y = np.array(num)
print('y is :\n',y)

popt, pcov = curve_fit(func, x, y,p0=[0,1,2])
#获取popt拟合系数
a = popt[0]
u = popt[1]
sig = popt[2]

yvals = func(x,a,u,sig) #拟合y值
print('系数a:', a)
print('系数u:', u)
print('系数sig:', sig)
#绘图
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('统计天数')
plt.ylabel('人数')
plot1 = plt.plot(x, y, 's',label='每日增加确诊患者人数',color='blue')
x = np.linspace(u - 3*sig, u + 3*sig, 50)
x_01 = np.linspace(u - 6 * sig, u + 6 * sig, 50)
y_sig = a* ( np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig) )
plt.plot(x, y_sig, "r-", linewidth=2)
# plt.plot(x, y, 'r-', x, y, 'go', linewidth=2,markersize=8)
plt.grid(True)
plt.legend(loc=2)
plt.title('每日增长高斯曲线')
plt.show()