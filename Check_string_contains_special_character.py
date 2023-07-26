import re


def run(string):

	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	
	if(regex.search(string) == None):
		print("String does not contains special so it is accepted")
		
	else:
		print("String contains special so it is not accepted.")
	
if __name__ == '__main__' :
	
	string = "Python & Programming"
	
	run(string)
