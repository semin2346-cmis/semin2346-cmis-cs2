import random
import math

def estimation(a, correct):
	guess = raw_input("I'm thinking of a number between " + str(0) + " and " + str(100) + ".\n" + "What do you think it is?: ") 
	if int(guess) == int(correct):
		print "Good guess."
	else:
		if int(guess) < int(correct):
			print "Try again. Your guess is too small."
			print correct
			return estimation(0, correct) 
		elif int(guess) > int(correct):
			print "Try again. Your guess is too large."
			print correct
			return estimation(0, correct) 
		else:
			print "How. HOW could you get that wrong?"
estimation(0, random.randint(0, 100))

#def sub(a, b):
#	return int(a) - int(b)
#def add(c, d):
#	return int(c) + int(d)

#def guessing_small(chosen_number, estimation, difference):
#	guess_small = """
#The target was {}.
#Your guess was {}.
#That's under by {}.
#""".format(chosen_number, estimation, difference)
#	return guess_small

#def guessing_big(chosen_number, estimation, difference):
#	guess_big = """
#The target was {}.
#Your guess was {}.
#That's over by {}.
#""".format(chosen_number, estimation, difference)
#	return guess_big

#def guessing_correct(chosen_number, estimation):
#	guess_correct = """
#The target was {}.
#Your guess was {}.
#That's correct.
#""".format(chosen_number, estimation)
#	return guess_correct

#def main():
	#Input
#	minimum = int(raw_input("What is the minimum number? "))
#	maximum = int(raw_input("What is the maximum number? "))
#	estimation = raw_input("I'm thinking of a number between " + str(minimum) + " and " + str(maximum) + ".\n" + "What do you think it is?: ")
	#Processing
#	chosen_number = int(random.randint(minimum, maximum))
#	difference = abs(sub(int(estimation), chosen_number))	
	#Output
#	if chosen_number < abs(int(estimation)):	
#		guess_small = guessing_small(chosen_number, estimation, difference)
#		print guess_small
#	elif chosen_number > abs(int(estimation)):
#		guess_big = guessing_big(chosen_number, estimation, difference)
#		print guess_big
#	elif chosen_number == abs(int(estimation)):
#		guess_correct = guessing_correct(chosen_number, estimation)
#		print guess_correct
# main()

import random
import math

def stage(correct, times_recursed, response):
	guess = raw_input("I'm thinking of a number between " + str(0) + " and " + str(100) + ".\n" + "What do you think it is?: ")
	if correct == int(guess):
		print "Good guess!"
		return response + 1
	elif times_recursed == 0:
		return response
	elif correct < int(guess):
		print "Try again. Your guess is too small."
		return stage(correct, times_recursed - 1, response)
	elif correct > int(guess):
		print "Try again. Your guess is too small."
		return stage(correct, times_recursed - 1, response)
	else:
		print "How. HOW could you get that wrong?"

def round_number(n, response, computers_correct):	
	if n == 0:
		print """
{} {}
""".format(str(response), str(computers_correct))
	else:
		correct = random.randint(1, 100)
		print "\nYou have {} rounds left".format(n)
		response = stage(correct, 4, response)
		highest_number = 100
		lowest_number = 0
		number = 50
		round_number(n - 1, uc, computers_correct)

def main():
	round_number(3, 0, 0)


















def bonus(highest_number, lowest_number, number, computers_correct, number_recursed):
	print "\nI guess {}".format(number)
	your_number = raw_input("too (h)igh, too (l)ow, (c)orrect: ")
	if your_number == "c":
		return computers_correct + 1
	elif number_recursed == 0:
		return computers_correct
	elif your_number == "h":
		bonus(number, lowest_number, ((number - highest_number) / 2) + number, computers_correct, number_recursed - 1)
	else:
		bonus(highest_number, number, ((highest_number - number) / 2) + number, computers_correct, number_recursed - 1)


