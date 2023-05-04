def sumArray(arr):
	sum = 0
	for i in arr:
		sum = sum + i

	return(sum)

	
arr = [12, 3, 4, 15, 12, 4]
n = len(arr)
ans = sumArray(arr)
print('Sum of the array is ', ans)
