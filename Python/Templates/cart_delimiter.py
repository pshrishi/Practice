from string import Template

class HashTemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(name="Coke", price=10, qty=3))
	cart.append(dict(name="Pepsi", price=5, qty=2))
	cart.append(dict(name="Sierra", price=15, qty=4))

	template = HashTemplate("#qty x #name = #price")

	total = 0
	for item in cart:
		print(template.safe_substitute(item))
		total += item["price"]

	print("Total: " + str(total))

if __name__ == '__main__':
	Main()
