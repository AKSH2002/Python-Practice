list1 = [25, 64, 54, 15, 83, 35, 86,23]

for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)

print("New list after removing all even numbers: ", list1)
