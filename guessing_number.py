import random
import math

def sub(a, b):
	return int(a) - int(b)
def add(c, d):
	return int(c) + int(d)

def guessing_small(chosen_number, estimation, difference):
	guess_small = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(chosen_number, estimation, difference)
	return guess_small

def guessing_big(chosen_number, estimation, difference):
	guess_big = """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(chosen_number, estimation, difference)
	return guess_big

def guessing_correct(chosen_number, estimation):
	guess_correct = """
The target was {}.
Your guess was {}.
That's correct.
""".format(chosen_number, estimation)
	return guess_correct

def main():
	#Input
	minimum = int(raw_input("What is the minimum number? "))
	maximum = int(raw_input("What is the maximum number? "))
	estimation = raw_input("I'm thinking of a number between " + str(minimum) + " and " + str(maximum) + ".\n" + "What do you think it is?: ")
	#Processing
	chosen_number = int(random.randint(minimum, maximum))
	difference = sub(int(estimation), chosen_number)	
	#Output
	if chosen_number > str(abs(int(estimation))):	
		guess_small = guessing_small(chosen_number, estimation, difference)
		print guess_small
	elif chosen_number < str(abs(int(estimation))):
		guess_big = guessing_big(chosen_number, estimation, difference)
		print guess_big
	elif chosen_number == abs(int(estimation)):
		guess_correct = guessing_correct(chosen_number, estimation)
		print guess_correct
main()
