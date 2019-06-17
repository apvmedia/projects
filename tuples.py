#tuples are more memory efficient

my_tuple = (1, 2, 3)
print(my_tuple)
#don't need the paren
my_tuple2 = 1, 2, 3
print(my_tuple2)
my_tuple3 = ([1, 2, 3])
print(my_tuple3)

tuple_with_a_list = (1, "apple", [3, 4, 5])
print(tuple_with_a_list)
#can't change the tuple, can change the value in the list
tuple_with_a_list[2][1] = 7
print(tuple_with_a_list)
#Like most other collection data types in Python, tuples can hold just about anything you want.
#tuples are not mutable
#tuples can be swapped without a thrid
a = 5
b = 20
print(a, b)
a, b = b, a 
print(a, b)


def add(*nums):
	total = 0
	for num in nums:
		total += num
	return total

add(5, 5)
add(32)



# if using **kwargs it always goes last *args, **kwargs
def add(base, *args):
	total = base
	for num in args:
		total += num
	return total

add(5, 20)
add(32)


# Let's play with the *args pattern.

# Create a function named multiply that takes any number of arguments. 
# Return the product (multiplied value) of all of the supplied arguments. 
# The type of argument shouldn't matter.

# Slices might come in handy for this one.

def multiply(*args):
	value = 0
	for num in args:
		if value == 0:
			value = num
		else:
			value = num * value
	return value

print(multiply(2, 2, 2))