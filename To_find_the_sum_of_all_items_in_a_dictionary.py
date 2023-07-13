def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final

dict = {'a': 150, 'b': 50, 'c': 250}
print("Sum :", returnSum(dict))