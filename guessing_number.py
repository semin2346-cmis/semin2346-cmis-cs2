import random
import math

def sub(a, b):
	return float(a) - float(b)
def add(c, d):
	return float(c) + float(d)

def guessing(chosen_number, estimation, difference):
	guess_small = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(chosen_number, estimation, difference)
	return guess_small

def guessing(chosen_number, estimation, difference):
	guess_big = """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(chosen_number, estimation, difference)
	return guess_big

def guessing(chosen_number, estimation):
	guess_correct = """
The target was {}.
Your guess was {}.
That's correct.
""".format(chosen_number, estimation)
	return guess_correct

def main():
	#Input
	minimum = float(raw_input("What is the minimum number? "))
	maximum = float(raw_input("What is the maximum number? "))
	estimation = raw_input("I'm thinking of a number between " + str(minimum) + " and " + str(maximum) + ".\n" + "What do you think it is?: ")
	#Processing
	chosen_number = float(random.randint(minimum, maximum))
	difference = sub(float(estimation), chosen_number)	
	#Output
	if chosen_number > str(float(estimation)):	
		guess_small = guessing(chosen_number, estimation, difference)
		print guess_small
	elif chosen_number < str(float(estimation)):
		guess_big = guessing(chosen_number, estimation, difference)
		print guess_big
	elif chosen_number == str(float(estimation)):
		guess_correct = guessing(chosen_number, estimation, difference)
		print guess_correct
main()
