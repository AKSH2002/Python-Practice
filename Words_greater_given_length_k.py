def string_k(k, str):

	string = []

	text = str.split(" ")

	for x in text:

		if len(x) > k:
			string.append(x)

	return string


k = 4
str = "Programming with the Python language"
print(string_k(k, str))
