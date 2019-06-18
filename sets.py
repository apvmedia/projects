#sets.py

# a unique set of items that below together for some reason
# only one item in a set, no duplicates
# not sorted
# no index use .add() .remove() .update() 
# iterable collections
# old python method set([1, 3, 5])
# new python method {1, 2, 3} 
# net method must have someting in it when created otherwise use set([])

low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17)
print(low_primes)
low_primes.update({19,23},{2, 29})
print(low_primes)
low_primes.add(15)
low_primes.remove(15)
#low_primes.remove(15)
low_primes.discard(15) #no error calling .remove again would give an error
print(low_primes)

# common use of set is to make other itterable unique
# list of page numbers where terms appear in a book
# pages = list(set(pages))

pages = [1, 1, 1, 1, 2, 3, 5, 6, 7, 5, 5, 3, 3, 4, 4, 4,4 ]
print(pages)
pages = list(set(pages))
print(pages)


songs = {"Rock You Like A Huricane", "My Girl", "Diver Down"}
songs.add("Treehouse Hula")
songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})

#union - two or more sets
#difference - find everthing in the first but not in the second 
#symmetric difference - everything that is unique to either set, no shared 
#intersection - all items that are in both sets
#can me used as both methods or operators
#for union and symmetric difference the order doesn't matter because the resulting set is combined

# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
# (also: notice how those are using *others? That's a tuple of other sets. See, I told you that pattern was everywhere!)

set1 = set(range(10))
print(set1)
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
print(set2)
print(set1.union(set2)) #doesn't change set1 or set2
print(set1)
print(set1 | set2) #union operand
print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2) #difference operand
print(set2 - set1) #difference operand
print(set1.symmetric_difference(set2)) #symetric difference
print(set2.symmetric_difference(set1)) #symetric difference
print(set1 ^ set2) #symetric difference operand
print(set2 ^ set1) #symetric difference operand
print(set1.intersection(set2)) #intersection
print(set2.intersection(set1)) #intersection
print(set1 & set2) #intersection operand
print(set2 & set1) #intersection operand



# Let's write some functions to explore set math a bit more. We're going to be using this 
# COURSES dict in all of the examples. Don't change it, though!

# So, first, write a function named covers that accepts a single parameter, a set of topics. 
# Have the function return a list of courses from COURSES where the supplied set and the course's
#  value (also a set) overlap.

# For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(topics): 
	course_set = []
	for key, value in COURSES.items():
		if topics.intersection(value):
			course_set.append(key)

	return course_set


set1 = covers({"Python"}) 
print(set1)


# OK, let's create something a bit more refined. Create a new function named covers_all that takes a single
# set as an argument. Return the names of all of the courses, in a list, where all of the topics in the supplied
# set are covered.

# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. 
# Java Basics and PHP Basics would be excluded because they don't include both of those topics.

def covers_all(topics): 
	course_set = []
	for key, value in COURSES.items():
		if topics.intersection(value):
			if topics.issubset(value):
				course_set.append(key)

	return course_set

set2 = covers_all({"conditions", "input"})
print(set2)

