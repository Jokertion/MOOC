#Cal_J_convert.py
#卡路里转换
num = input()
if num[-3:] == "cal":
	convert_joule = 4.186 * eval(num[:-3])
	print("{:.3f}J".format(convert_joule))
if num[-1] == "J":
	convert_cal = eval(num[:-1]) / 4.186 
	print("{:.3f}cal".format(convert_cal))