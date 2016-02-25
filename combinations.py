import math

def factorial(x):
	return math.factorial(x)

def output(name, animal, nationality, x, y):
	out = """
Greetings {}.
I have been enlightened previously with the knowledge that a(n) {} is your favorite animal.
You happen to be from {}, correct?
Well, remember that the factorial of {} is {}.
Farewell.
""".format(name, animal, nationality, x, y)
	return out

def main():
	name = raw_input("What do you call yourself, stranger? \n")
	animal = raw_input("Enlighten me, what is your favorite animal? \n")
	nationality = raw_input("Where do you originate from? \n")
	x = int(raw_input("Type a positive integer, please. \n"))
	y = math.factorial(x)
	out = output(name, animal, nationality, x, y)
	print out

main()
