test_list = [25, 52, 42, 16, 38, 61, 93, 82, 29, 58]

print("The original list is : " + str(test_list))

res = []
for ele in test_list:
	sum = 0
	for digit in str(ele):
		sum += int(digit)
	res.append(sum)

print ("List Integer Summation : " + str(res))
