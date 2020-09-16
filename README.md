# Covid-19-data-fitting-and-prediction
新冠疫情数据拟合及预测

新冠疫情期间，运用 python，基于疫情相关数据设计了几款疫情预测模型，结果曲线能够很好地与国内疫情发展情况拟合并能较好地预测病例增长的拐点时间。
由于湖北疑似数据较多，确诊数据准确性较差，我选择了全国除湖北外确诊人数的数据进行拟合，数据来自@人民日报 微博每日发布，把1月21日作为统计第一天，进行数据收集。
首先，根据国除湖北外确诊人数数据画出了散点图和折线图。

![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/1.png)

初期利用python的curve_fit进行指数函数的拟合，拟合程度较高。

![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/2-1.png)

但是后期随着数据增加，拟合次数达到上限, 而结果还没拟合出来，需要传入maxfev参数, 修改上限，而拟合程度也较差。

![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/2-2.png)

然后，分别利用python的np.polyfit 和 np.polyld分别进行一元二次式拟合和一元三次式拟合，发现一元三次式拟合程度更高。

![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/3.png)
![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/4.png)

通过求解系数矩阵，分别计算出一元二次式系数和一元三次式系数。
在钟南山院士提出拐点后，尝试预测拐点。选择了高斯函数模型，利用python的curve_fit对每日增长的确诊数量进行拟合，预测拐点。

![image](https://github.com/Yunbamboo/Covid-19-data-fitting-and-prediction/blob/master/7.png)
