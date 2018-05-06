#CalHamletV1.py
def getText():
	txt = open("hamlet.txt","r").read()
	txt = txt.lower()
	for ch in '!"#$%&()*+,-./<=>?@[\\]^_’{|}~':
		txt = txt.replace(ch, " ")
	return txt
	
hamletTxt = getText()
words = hamletTxt.split()
counts = {}

#(仅两行)遍历列表中的每个元素，并且用字典记录每一个元素出现的次数
for word in words:
	#.get()方法:用来从字典中获得某一个键对应的值。如果这个键不在字典中，给出默认值
	"""用当前的某一个英文单词作为键，索引字典，如果它在里面，那就返回他的次数，
	+1 说明这个单词又出现了一次，如果这个单词不在字典中，那我们就把它加到字典中，
	并且赋给当前的值为0
	"""
	counts[word] = counts.get(word, 0) + 1 

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)  #对列表的第二个元素进行排序，排序方式是：从大到小的倒排
#将出现次数最多的元素前十名打印出来
for i in range(10):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word,count))
	
