#蒙特卡罗法计算圆周率
from random import random  		#调用random库中的random  
from time import perf_counter 		#调用计时
DARTS = 1000*1000			#抛洒点总数量
hits = 0.0 				#目前圆内的数量
start = perf_counter()			#当前系统时间

for i in range(1, DARTS+1): 		#对所有点进行抛洒
	x, y = random(), random()	#生成两个随机数的坐标值
	dist = pow(x**2+y**2, 0.5)	#每个点到圆心的距离（即圆心距）
	if dist <=1.0:			#判断是否在圆内
		hits = hits +1		#在园内，圆内数量计数加1
pi = 4 * (hits/DARTS)			#1/4pi*4=pi
print ("圆周率的值是：{}".format(pi))
print ("运行时间是：{:.5f}s".format(perf_counter()-start))

