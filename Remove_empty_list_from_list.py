test_list = [23, 45, 56, [], 6, 32, [], 28, [], 76, [], 51, 35]

print("The original list is : " + str(test_list))

res = [ele for ele in test_list if ele != []]

print("List after empty list removal : " + str(res))
