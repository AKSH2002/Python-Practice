test_str = 'Programming with python is best way to Start with Learning Programming'

print("The original string is : " + str(test_str))

word_list = ["is", 'to', 'Learning']

repl_wrd = 'that'

res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])

print("String after multiple replace : " + str(res))