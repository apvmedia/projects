#combo.py



# Alright, this one can be tricky but I'm sure you can do it.

# Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever.

# Your function should return a list of tuples. Each tuple should hold the first item in each iterable, 
# then the second set, then the third, and so on. Assume the iterables will be the same length.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

# a = [(1,1,1)]
# for i in range (2,10):
#     a.append((i,i,i))
# a = tuple(a)   

def combo(iter_thing1, iter_thing2):
	my_tuple = []
	for counter, value in enumerate(iter_thing1):
		my_tuple.append((value, iter_thing2[counter]))
	return my_tuple


print(combo([1, 2, 3], 'abc'))
