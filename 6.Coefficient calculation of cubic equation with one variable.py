# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:32:08 2020

@author: hy
"""

import matplotlib.pyplot as plt
from pylab import mpl
import math
import numpy as np
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
y = [258,440,571,830,1287,1975,2744,4515,5974,7711,9692,11791,14380,17205]

#完成拟合曲线参数的计算
def calculate_parameter(data):
    #i用来控制列元素，line是一行元素,j用来控制循环次数,datas用来存储局部变量。保存修改后的值
    i = 0;
    j = 0;
    line_size = len(data)  
    
    #将行列式变换为上三角行列式
    while j < line_size-1:
        line = data[j]
        temp = line[j]
        templete=[]
        for x in line:
            x=x/temp
            templete.append(x)
        data[j]=templete   
        
        #flag标志应该进行消元的行数
        flag = j+1
        while flag < line_size:
            templete1 = []
            temp1=data[flag][j]
            i = 0
            for x1 in data[flag]:
                if x1!=0:
                   x1 = x1-(temp1*templete[i])
                   templete1.append(x1)
                else:
                   templete1.append(0)
                i += 1
            data[flag] = templete1
            flag +=1
        j += 1
        
#求相应的参数值
    parameters=[]
    i=line_size-1
    flag_j=0
    rol_size=len(data[0])
    flag_rol=rol_size-2
    
#获得解的个数
    while i>=0:
        operate_line = data[i]
        if i==line_size-1:
            parameter=operate_line[rol_size-1]/operate_line[flag_rol]
            parameters.append(parameter)
        else:
            flag_j=(rol_size-flag_rol-2)
            temp2=operate_line[rol_size-1]
            result_flag=0
            while flag_j>0:
                temp2-=operate_line[flag_rol+flag_j]*parameters[result_flag]
                result_flag+=1
                flag_j-=1
            parameter=temp2/operate_line[flag_rol]
            parameters.append(parameter)
        flag_rol-=1
        i-=1
    return parameters

#计算拟合曲线的值
def calculate(data_x,parameters):
    datay=[]
    for x in data_x:
        datay.append(parameters[2]+parameters[1]*x+parameters[0]*x*x)
    return datay
for w in parameters:
    print(w)

f1 = np.poly1d([a,b,c])   
print('f1 is :\n',f1)

#函数绘制
def draw(data_x,data_y_new,data_y_old):
    plt.plot(data_x,data_y_new,label="拟合曲线",color="red")
    plt.scatter(data_x,data_y_old,label="每日确诊人数")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('统计天数')
    plt.ylabel('人数')
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("确诊曲线")
    plt.legend(loc=4)
    plt.show()
data=polynomial_fitting(x,y)
parameters=calculate_parameter(data)
newData=calculate(x,parameters)
draw(x,newData,y)