def count(str1 ,str2) :
	
	set_string1 = set(str1)
	set_string2 = set(str2)


	matched_characters = set_string1 & set_string2

	print("No. of matching characters are : " + str(len(matched_characters)) )


if __name__ == "__main__" :

	str1 = 'k$kl#sv5*53@df' 
	str2 = 'hj&r3f$kr@8g7v'	

	count( str1 , str2 )
	
