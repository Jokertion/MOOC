#MatchAnalysis.py
#体育竞技分析--自顶向下设计（系统思维的体现）
"""
比赛规则：
		1.双人击球比赛：A&B，回合制，5局3胜 
		2.开始时一方先发球，直至判分，接下来胜者发球
		3.球员只能在发球局得分，15分胜一局
"""

from random import random

def printIntro():
	print ("这个程序模拟两个选手A和B的某种竞技比赛")
	print ("程序运行需要A和B的能力值（以0到1之间的小数表示）")
	
def getInputs():
	a = eval(input("请输入选手A的能力值(0-1): "))
	b = eval(input("请输入选手B的能力值(0-1): "))
	c = eval(input("请输入比赛的场次: "))
	return a, b, c
	
def simNGames(n, probA, probB):
	winsA,winsB = 0, 0 
	for i in range(n):
		scoreA, scoreB =simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA += 1
		else:
			winsB += 1
	return winsA, winsB
	
def gameOver(a,b):		#返回True/False。A或B的分数是15分，一局就结束了。
	return a == 15 or b == 15
	
def simOneGame(probA, probB):
	scoreA, scoreB = 0,0
	serving = "A"  #发球人
	while not gameOver(scoreA ,scoreB):
		if serving == "A":
			#核心算法：A能力 与 A获得分数 之间的关系
			if random() < probA:  #生成一个随机变量，如果这个变量在A能力范围内（即小于A），A获得一分
				scoreA += 1
			else:
				serving = "B"
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = "A"
	return scoreA,scoreB
	
def printSummary(winsA,winsB):
	n = winsA + winsB
	print("竞技分析开始，共模拟{}场比赛".format(n))
	print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
	print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))


def main():
	printIntro()							   #STEP1.打印程序的介绍信息
	probA, probB, n = getInputs()			   #STEP2.获得程序运行参数（A，B能力值，模拟场次数）
	winsA, winsB = simNGames(n, probA, probB)  #STEP3.调用函数，将获得的参数作为参数输入到函数中，获得A B获胜场次
	printSummary(winsA, winsB)				   #STEP4.打印球员A和B获胜比赛的场次和概率
	
main()
		
		
