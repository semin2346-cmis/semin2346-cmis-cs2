import math

def factorial(a):
	return math.factorial(a)
def sub(b, c):
	return int(b) - int (c)
def combination(d, e):
	return factorial(d) / (factorial(e) * factorial(sub(d, e)))
def output(name, animal, nationality, x, y, z):
	out = """
Greetings {}.
I have been enlightened previously with the knowledge that a(n) {} is your favorite animal.
You call your home country {}, correct?
Well, remember that the combination between {} and {} is {}.
Farewell.
""".format(name, animal, nationality, x, y, z)
	return out

def main():
	#Input
	name = raw_input("What do you call yourself, stranger? \n")
	animal = raw_input("Enlighten me, what is your favorite animal? \n")
	nationality = raw_input("Where do you originate from? \n")
	x = int(raw_input("Type a positive integer, please. \n"))
	y = int(raw_input("Type another positive integer that is of less value than the previous, please. \n"))
	#Processing
	z = combination(x, y)
	#Output
	out = output(name, animal, nationality, x, y, z)
	print out
main()
