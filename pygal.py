##pygal 画廊
import pygal
from random import randint
class Die():
    def __init__(self,side=6):
        self.side = 6
    def roll(self):
        return randint(1,self.side)

#执行2次？？？
#执行2次就2次吧，不知道哪里出了问题
die = Die()
#投骰子，把结果存入列表
result=[]
#投100次
for i in range(5):
    num = die.roll()
    result.append(num)
    print(result)
frequency=[]

#计算频率
for value in range(1,die.side+1):
    #点用列表.count功能
    num = result.count(value)
    frequency.append(num)

#绘制直方图
hist=pygal.Bar()
#pygal没有Bar模块？？？
#pygal的官方网站：www.pygal.org
#有啊，是怎么回事？？
#hist.title="投骰子，6个面 100次各个面的频率"
#hist.x_labels=['1','2','3','4','5','6']
#hist.x_title="结果"
#hist.y_title="频率"
#hist.add("表的名字",frequency)
#hist.render_to_file("储存图片的名字和路径.svg")
