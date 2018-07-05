#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#读取数据
datals = []
f= open("data.txt")
for line in f:
     line =  line.replace("\n","")
     datals.append(list(map(eval, line.split(","))))
f.close()

#自动绘制
for i in range(len(datals)):
     t.pencolor(datals[i][3],datals[i][4],datals[i][5])
     t.fd(datals[i][0])
     if datals[i][1]:
          t.right(datals[i][2])
     else:
          t.left(datals[i][2])
		
"""经验教训：
接口的信息(data.txt)不能复制粘贴，必须一个数字一个字的敲进去，
不然程序读不出来。会一直报错SyntaxError: unexpected EOF while parsing
测试了好长时间，原来复制粘贴文本里也有记录 T_T
"""	
'''
解决办法：
显示缩进，用tab填充·
'''
