import random
import math

def estimation(a, correct):
	guess = int(raw_input("I'm thinking of a number between " + str(0) + " and " + str(100) + ".\n" + "What do you think it is?: "))
	if guess == a:
		print "You guessed incorrectly " + str(correct) + " times."
	elif guess == a:
		print "Good guess."
	elif guess > a:
		print "Try again. Your guess is too large."
		estimation(a, correct + 1)
	else:
		print "Try again. Your guess is too small."
		correct + 1
		estimation(a, correct + 1)
estimation(random.randint(0, 100), 0)

