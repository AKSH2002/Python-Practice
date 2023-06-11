def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result

list1 = [4, 3, 6]
list2 = [5, 8, 2]
print(multiplyList(list1))
print(multiplyList(list2))
