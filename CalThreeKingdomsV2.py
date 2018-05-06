#CalThreeKingdomsV2.py
#三国演义词频统计
import jieba
txt = open ("threekingdoms.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts ={}
for word in words:
	if len(word) == 1:
		continue
	else:
		counts[word] = counts.get(word,0) +1

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)  #对列表的第二个元素进行排序，排序方式是：从大到小的倒排
for i in range(15):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word,count))
	