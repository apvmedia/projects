# key and value pair, mutable, not sortable, like hashes and associated arrarys
# keys can be strings, numbers and tuples
# keys are assigned in order
#literal contruction method
course = {"title": "Python Collections"}
print(course)
print(course["title"])
#dict is another way to create dictionaries but not as friendly
anotherway = dict([["title", "Python Collections"]])
print(anotherway)
# use , to add multiple key value pairs
course = {"title": "Python Collections", "teacher": "Kenneth Love", "videos": 22}
print(course["videos"])
print(course["title"])
#KeyError if you ask for a key that doesn't exist
#print(course["runtime"])

# can nest dictionaries

course = {"title": "Python Collections", "teacher": {"first_name": "Kenneth", "last_name": "Love"}}
print(course)
print(course["teacher"])
print(course["teacher"]["first_name"])

#mutable but not indexable, no append, directly add by key value pair, value can be anything
player = {"name": "Wayne", "remaining_lives": 3}
print(player)
player["levels"] = [1, 2, 3, 4]
player["items"] = {"items": "knife"}
print(player)

wayne = {"first_name": "Wayne", "job": "Python Programmer"}
print(wayne)
wayne["last_name"] = "Wallace"
print(wayne)
#update lets us add or change multiple keys at one time
wayne.update({"job": "Master Python Programmer", "editor": "Sublime"})
print(wayne)
wayne["editor"] = "Atom"
print(wayne)
del wayne["job"]
print(wayne)

#packing and unpacking is powerful for creating and storing varaible values

def packer(**kwargs):
	print(kwargs)

packer(name="Wayne", num=42, kids=None)


def packer2(name=None, **kwargs):
	print(kwargs)

packer2(name="Wayne", num=42, kids=None)


def unpacker(first_name=None, last_name=None):
	if first_name and last_name:
		print("Hi {} {}".format(first_name, last_name))
	else:
		print("Hi No Name!")
# order doesn't matter because the ** upacks the key pair value and makes variables
#** has to be last argument in func
unpacker(**{"last_name": "Wallace", "first_name": "Wayne"})

#"Hi, I'm {name} and I love to eat {food}!".format(name="Kenneth", food="tacos")
# Returns "Hi, I'm Kenneth and I love to eat tacos!"

#dictionaries don't have a specific order, use keys

def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)

print(favorite_food({"name": "Wallace", "food": "Burgers"}))


course_minutes = {"Python Basics": 232, "Django": 237, "Flask Basics": 	189, "Java Basics": 133}

for course in course_minutes:
	print(course)

#only gives the keys

for course in course_minutes:
	print(course_minutes[course])

# use key and values, optimized for large dicts
for key in course_minutes.keys():
	print(key)

for value in course_minutes.values():
	print(value)

#use item to get tuples of key value pairs
for item in course_minutes.items():
	print("The course {} is {} minutes long.".format(item[0], item[1]))


# Alright, this one might be a bit challenging but you've been doing great so far, so I'm sure you can manage it.

# I need you to make a function named word_count. It should accept a single argument which will be a string.
# The function needs to return a dictionary. The keys in the dictionary will be each of the words in the string,
# lowercased. The values will be how many times that particular word appears in the string.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(words):
	word_dict = {}
	lowered_words = words.lower()
	word_list = lowered_words.split()
	for word in word_list:
		count = word_list.count(word)
		if word in word_dict:
			continue
		else:
			word_dict.update({word: count})
	return word_dict

print(word_count("This is a test of a word count fuction"))


# This challenge has several steps so take your time, read the instructions carefully, 
# and feel free to experiment in Workspaces or on your own computer.

# For this first task, create a function named num_teachers that takes a single argument, 
# which will be a dictionary of Treehouse teachers and their courses.

# The num_teachers function should return an integer for how many teachers are in the dict.

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.



def num_teachers(courses):
# dictionary of Treehouse teachers and their courses
	# return integer for how many teachers are in the dict
	teacher_count = 0
	for item in courses.items():
		teacher_count += 1
	#	print("The course {} is {} minutes long.".format(item[0], item[1]))
		
	return int(teacher_count)


courses =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

num_of_teachers = str(num_teachers(courses))
print("There are {} teachers.".format(num_of_teachers))


# That one wasn't too bad, right? Let's try something a bit more challenging.

# Create a new function named num_courses that will receive the same dictionary as its only argument.

# The function should return the total number of courses for all of the teachers.

def num_courses(courses):
	course_count = 0

	for item in courses.items():
		#print(item[1])
		#print("The course {} is {} minutes long.".format(item[0], item[1]))
		#for course in courses.items([0])
		course_count += len(item[1])

	return int(course_count)


courses =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', "c"], 'Kenneth Love': ['Java', 'Python Basics', 'Python Collections']}

num_of_courses = num_courses(courses)
print("The total number of courses is {}".format(num_of_courses))


# Great work! OK, you're doing great so I'll keep increasing the difficulty.

# For this step, make another new function named courses that will, again, 
# take the dictionary of teachers and courses.

# courses, though, should return a single list of all of the available courses 
# in the dictionary. No teachers, just course names!

def courses(courses):

	course_list = []

	for item in courses.items():
		#print(item[1])
		#course_list.append(item[1])
		#print("The course {} is {} minutes long.".format(item[0], item[1]))
		#for x in item[1]
		for x in item[1]:
			course_list.append(x)

	return course_list


available_courses =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', "c"], 'Kenneth Love': ['Java', 'Python Basics', 'Python Collections']}


list = courses(available_courses)
print(list)


def most_courses2(courses):
	max_count = 0
	course_count = 0
	teacher_with_most = ""

	for item in courses.items():
		course_count = len(item[1])
	 	if course_count > max_count:
	 		max_count = course_count
	 		teacher_with_most = item[0]
	 	else:
	 		course_count = 0

	return str(teacher_with_most)

def most_courses(teachers):
    max_count = 0
    teach = " " 
    for teacher,courses in teachers.items():
        if len(courses) > (max_count):
            teacher = teacher
            max_count = len(courses)
    return teacher

available_courses =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', "c", "d", "d","ass"], 'Kenneth Love': ['a', 'b', 'Java', 'Python Basics', 'Python Collections']}

teacher = most_courses2(available_courses)
print(teacher)


teacher = most_courses(available_courses)
print(teacher)


# It's official: you're awesome at Python dictionaries! One last task and then you can take a well-deserved break!

# In this last challenge, I want you to create a function named stats and it'll take our teacher 
# dictionary as its only argument.

# stats should return a list of lists where the first item in each inner list is the teacher's 
# name and the second item is the number of courses that teacher has. For example, 
# it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]



def stats(courses):
	course_count = 0
	stats_list = []

	for item in courses.items():
		course_count = len(item[1])

		stats_list.append([item[0], course_count])


	return stats_list


courses =  {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', "c"], 'Kenneth Love': ['Java', 'Python Basics', 'Python Collections']}

stats = stats(courses)
print(stats)