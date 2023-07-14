string = 'Hello World'
character = 'l'

count = len(string) - len(string.replace(character, ''))
print(count) 
