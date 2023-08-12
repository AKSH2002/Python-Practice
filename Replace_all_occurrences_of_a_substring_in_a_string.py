test_str="Java Programming Java"
s1="Java"
s2="Python"

s=test_str.split(s1)
new_str=""

for i in s:
	if(i==""):
		new_str+=s2
	else:
		new_str+=i

print(new_str)
