def Cloning(li1):
	li_copy = li1[:]
	return li_copy

li1 = [2, 15, 9, 18, 25, 21, 16, 7, 31]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
