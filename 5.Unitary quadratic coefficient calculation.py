# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:28:10 2020

@author: hy
"""

import matplotlib.pyplot as plt
from pylab import mpl
import math
#全国除湖北外累计确诊
x = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
y= [558,923,1321,1801,2420,3125,3886,4638,5306,6028,6916,7646,8353,9049,9593,10098,10540,10910,11287,11598,11865,12086,12251,12366,12447,12503]

"""完成拟合曲线参数计算前相应变量的计算"""
#窗口长度
def polynomial_fitting(data_x,data_y):
    size=len(data_x)
    i=0
    sum_x = 0
    sum_sqare_x =0
    sum_third_power_x = 0
    sum_four_power_x = 0
    average_x = 0
    average_y = 0
    sum_y = 0
    sum_xy = 0
    sum_sqare_xy = 0
    while i<size:
        sum_x += data_x[i]
        sum_y += data_y[i]
        sum_sqare_x += math.pow(data_x[i],2)
        sum_third_power_x +=math.pow(data_x[i],3)
        sum_four_power_x +=math.pow(data_x[i],4)
        sum_xy +=data_x[i]*data_y[i]
        sum_sqare_xy +=math.pow(data_x[i],2)*data_y[i]
        i += 1;
    average_x=sum_x/size
    average_y=sum_y/size
    return [[size, sum_x, sum_sqare_x, sum_y]
        , [sum_x, sum_sqare_x, sum_third_power_x, sum_xy]
        , [sum_sqare_x,sum_third_power_x,sum_four_power_x,sum_sqare_xy]]
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

#函数绘制
def draw(data_x,data_y_new,data_y_old):
    plt.plot(data_x,data_y_new,label="拟合曲线",color="black")
    plt.scatter(data_x,data_y_old,label="累计患者数量")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.xlabel('统计天数')
    plt.ylabel('人数')
    plt.title("一元二项式拟合数据")
    plt.legend(loc=4)
    plt.show()
data=polynomial_fitting(x,y)
parameters=calculate_parameter(data)
for w in parameters:
    print(w)
newData=calculate(x,parameters)
draw(x,newData,y)
    