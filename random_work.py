##随机漫步 随机散点图
##
##
from random import choice
import matplotlib.pyplot as plt

class random_walk():
    #""" 默认5000个点 """
    def __init__(self,num=5000):
        self.num = num
        self.xvalue = [0]
        self.yvalue = [0]

    def fill_work(self):
        while len(self.xvalue) < self.num:
            xdirection = choice([1,-1]) #x轴选择方向 x轴前进或者后退
            xdistance = choice([0,1,2,3,4])
            xstep = xdirection * xdistance

            ydirection = choice([1,-1]) #y轴前进或者后退
            ydistance = choice([0,1,2,3,4])
            ystep = ydirection * ydistance
            # """如果原地踏步 """ 
            if xstep == 0 and ystep == 0:
                continue ##重新建立
            nextx = self.xvalue[-1] + xstep #前一个的X轴坐标与新坐标相加
            nexty = self.yvalue[-1] + ystep #前一个的Y轴坐标与新坐标相加
            self.xvalue.append(nextx) #插入记录坐标点数的列表
            self.yvalue.append(nexty)

while True:
    rw = random_walk(20000)
    rw.fill_work()
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num))
    plt.scatter(rw.xvalue,rw.yvalue,s=1,c=point_numbers,cmap = plt.cm.Blues,
            edgecolor = 'none')
    plt.axes().get_xaxis().set_visible(False) #隐藏坐标轴
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    continues=input("continue?")
    if continues == 'n':
        break

