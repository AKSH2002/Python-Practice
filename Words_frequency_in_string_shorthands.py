test_str = 'Hi there Will, how are you Will, Will you say Hi to'

print("The original string is : " + str(test_str))

res = {key: test_str.count(key) for key in test_str.split()}

print("The words frequency : " + str(res))
