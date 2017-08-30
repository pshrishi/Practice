def Reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

def Main():
	rev = Reverse(input("Please enter a string to reverse: "))
	for char in rev:
		print(char)

if __name__ == '__main__':
	Main()
