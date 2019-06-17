favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']

slice1 = favorite_things[1:4]
print(slice1)
slice2 = favorite_things[5:]
print(slice2)

sorted_things = sorted(favorite_things[:])
print(sorted_things)

numbers = list(range(20))
print(numbers)
# start:stop:increment
even_numbers = numbers[2::2]
print(even_numbers)
#works with any iterable
print("Alabama"[::2])
print(numbers[-2:])
#use negative number to walk back from end of list
print(numbers[-2:-5:-1])
#reverse the list
print(numbers[::-1])
#doesn't change the list
print(numbers)

def first_4(items):
	return items[:4]

print(first_4(numbers))

def first_and_last_4(items):
	return items[:4] + items[-4:]

print(first_and_last_4(numbers))

def odds(items):
	return items[1:len(items):2]

print("Odd numbers")
print(odds(numbers))

def reverse_evens(items):
	return items[::2][::-1]

print("Even indexes")
print(reverse_evens(numbers))

rainbow = ["red", "orange", "green", "yellow", "blue", "black", "white", "auqua", "purple", "pink"]
print(rainbow)
del rainbow[5]
print(rainbow)

rainbow = ["red", "orange", "green", "yellow", "blue", "black", "white", "auqua", "purple", "pink"]
print(rainbow)
del rainbow[5:8]
print(rainbow)
#reverse order of yellow and green
rainbow[2:4] = ["yellow", "green"]
print(rainbow)
#replace and add an item
rainbow[4:5] = ["blue", "indigo"]
print(rainbow)


#remove last 2 and add a string
rainbow[-2:] = "violet"
print(rainbow)
#join the last 6 items in the list
rainbow[-6:] = ["".join(rainbow[-6:])]
print(rainbow)


def sillycase(word):
	#use int for indexes or // for int division
	first_half = word[:len(word)//2:]
	last_half = word[-len(word)//2:]
	return first_half.lower() + last_half.upper()

print(sillycase("MailBomb"))
print(sillycase("treehouses"))
print(sillycase("Alphabet"))



