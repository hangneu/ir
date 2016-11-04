file = open("logo.txt","r")
result = []
for item in file:
	result.append(item.split("\n")[0])
file.close()
title = result[0]+".txt"
file = open(title,"r")
dic = {}
for item in file:
	aew = item.split(" ")
	for ter in aew[:len(aew)-1]:
		if ter in dic:
			dic[ter] += 1
		else:
			dic[ter] = 1
print(dic)