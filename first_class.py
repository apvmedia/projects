
class Student:
    name = "Wayne"
	
	def praise(self):
		print("{} is the best!".format(self.name))
		return "{} is the best!".format(self.name)

me = Student()

print("My name is {}".format(me.name()))


