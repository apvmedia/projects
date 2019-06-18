
def stringcases_old(string):
# ["UPPERCASE", "lowercase", Titled Case, Reversed]
	string_formats = [string.upper()]
	string_formats.append(string.lower())
	string_formats.append(string.title())
	string_formats.append(string[::-1])
	return string_formats


def stringcases(string):
	return string.upper(), string.lower(), string.title(), string[::-1]

print(stringcases("Wayne Is A Bad Ass Python Programmer"))