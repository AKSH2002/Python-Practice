def Cumulative(lists):
	cu_list = []
	length = len(lists)
	cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
	return cu_list[1:]

lists = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print (Cumulative(lists))
