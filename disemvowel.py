def disemvowel(word):
	newword = ""
	for letter in word:
		if letter.upper() == 'A':
			continue
		elif letter.upper() == 'E':
			continue
		elif letter.upper() == 'I':
			continue
		elif letter.upper() == 'O':
			continue
		elif letter.upper() == 'U':
			continue
		else:
			newword += letter
	
		word = newword	
	return word

print(disemvowel("Wayne"))


names = ["Ken", "Alena", "Sam", "Wayne"]
name_1 = names.pop()
print(name_1)
print("List: {}".format(names))