#lengthconvert.py

length = input()
if length[-1] in ['m']:
	inch = (eval(length[:-1]))*39.37
	print ('{:.3f}in'.format(inch))
elif length[-2:] in ['in']:
	meter = (eval(length[:-2]))/39.37
	print ('{:.3f}m'.format(meter))
"""	
长度转换
I
描述:
请编写程序，完成米和英寸之间的长度转换，基本需求如下：

输入英寸，转换成米；输入米，转换成英寸。

英寸采用in标记，放在数值结尾；米采用m标记，放在数值结尾。

1 米 = 39.37 英寸

输入参数请使用input()，不要增加提示字符串信息。

 
输入格式:
例1: 10m
例2: 20in

输出格式:
与输入格式相同，输出结果保留小数点后3位。


输入输出示例:

 输入	输出
10m       393.700in
20in       0.508m
"""
