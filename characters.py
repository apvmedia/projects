import random

class Thief:
	sneaky = True
	#methods operate on an instance of the class not the class, that's why we must pass in an object
	def pickpocket(self):
		print("Called by {}".format(self))
		if self.sneaky:
			return bool(random.randint(0,1))
		return False


kenneth = Thief()
print(kenneth.pickpocket())
print(Thief.pickpocket(kenneth))
kenneth.sneaky = False
print(kenneth.pickpocket())
print(Thief.pickpocket(kenneth))





