import re

def Find(string):

	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex, string)
	return [x[0] for x in url]

string = 'My Profile: https://github.com/AKSH2002/Python-Practice in the portal of https://github.com/AKSH2002'
print("Urls: ", Find(string))
