from pet import Pet

class Cat(Pet):
	
	def __init__(self, name, age):
		super().__init__(name, age)
	
	def talk(self):
		print("Purrr")
class Dog(Pet):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		print("Woofff")

def Main():
	pet = Pet("Bruno", 7)
	jess = Cat("Jess", 3)
	bernard = Dog("Bernard", 4)

	print("Is Jess a Cat? " + str(isinstance(jess, Cat))) 
	print("Is Jess a Pet? " + str(isinstance(jess, Pet)))
	print("Is Jess a Dog? " + str(isinstance(jess, Dog)))
	print("Is Bernard a Cat? " + str(isinstance(jess, Cat)))
	print("Is Bernard a Pet? " + str(isinstance(jess, Pet)))
	print("Is Bernard a Dog? " + str(isinstance(jess, Dog)))

	jess.talk()
	bernard.talk()
	
	try:
		pet.talk()
	except:
		print("Something went wrong here!")


if __name__ == '__main__':
	Main()
