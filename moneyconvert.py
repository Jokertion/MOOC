#货币转换 I 
money = input()
#美元转人民币
if money[0:3] in ['USD']:
	result_RMB = eval(money[3:]) * 6.78
	print ("RMB{:.2f}".format(result_RMB))
#人民币转美元
elif money[0:3] in ['RMB']:
	result_USD = eval(money[3:]) / 6.78
	print ("USD{:.2f}".format(result_USD))
