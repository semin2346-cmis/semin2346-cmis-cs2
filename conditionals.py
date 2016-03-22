#This game will give you 5 mental maths questions pertaining to the category you pick-addition, subtraction, multiplication, division.
#At the end of the quiz, it will give you a score out of 5.

import math
import random

def add(a, b):
	return int(a) + int(b)

def sum_questions():
	#Boundaries for equation.	
	minimum_sum = int(raw_input("Please type a minimum number for your questions. "))
	maximum_sum = int(raw_input("Please type a maximum number for your questions. "))
	#Variables for equation.
	a1 = random.randint(minimum_sum, maximum_sum)
	a2 = random.randint(minimum_sum, maximum_sum)
	b1 = random.randint(minimum_sum, maximum_sum)
	b2 = random.randint(minimum_sum, maximum_sum)
	c1 = random.randint(minimum_sum, maximum_sum)
	c2 = random.randint(minimum_sum, maximum_sum)
	d1 = random.randint(minimum_sum, maximum_sum)
	d2 = random.randint(minimum_sum, maximum_sum)
	e1 = random.randint(minimum_sum, maximum_sum)
	e2 = random.randint(minimum_sum, maximum_sum)
	#Answers for equation.
	sum_answer1 = add(a1, a2)
	sum_answer2 = add(b1, b2)
	sum_answer3 = add(c1, c2)
	sum_answer4 = add(d1, d2)
	sum_answer5 = add(e1, e2)
	print "None of the numbers used in the questions will exceed the set extremes."
	#Question 1.
	sum1 = str(a1) + "+" + str(a2)
	print sum1	
	estimation_sum1 = raw_input("Answer to question 1: ")	
	if int(estimation_sum1) == int(sum_answer1):
		print "Correct."
	else:
		print "Incorrect."
	#Question 2.
	sum2 = str(b1) + "+" + str(b2)
	print sum2
	estimation_sum2 = raw_input("Answer to question 2: ")	
	if int(estimation_sum2) == int(sum_answer2):
		print "Correct."
	else:
		print "Incorrect."
	#Question 3.
	sum3 = str(c1) + "+" + str(c2)
	print sum3
	estimation_sum3 = raw_input("Answer to question 3: ")	
	if int(estimation_sum3) == int(sum_answer3):
		print "Correct."
	else:
		print "Incorrect."
	#Question 4.	
	sum4 = str(d1) + "+" + str(d2)
	print sum4	
	estimation_sum4 = raw_input("Answer to question 4: ")
	if int(estimation_sum4) == int(sum_answer4):
		print "Correct."
	else:
		print "Incorrect."	
	#Question 5.
	sum5 = str(e1) + "+" + str(e1)
	print sum5	
	estimation_sum5 = raw_input("Answer to question 5: ")
	if int(estimation_sum5) == int(sum_answer5):
		print "Correct."
	else:
		print "Incorrect."
	#Scoring.
	numbercorrect = 0
	if int(estimation_sum1) == int(sum_answer1):
		numbercorrect = numbercorrect + 1
	elif int(estimation_sum2) == int(sum_answer2):
		numbercorrect = numbercorrect + 1
	elif int(estimation_sum3) == int(sum_answer3):
		numbercorrect = numbercorrect + 1
	elif int(estimation_sum4) == int(sum_answer4):
		numbercorrect = numbercorrect + 1
	elif int(estimation_sum5) == int(sum_answer5):
		numbercorrect = numbercorrect + 1
	elif numbercorrect >= 3:
		print "You passed."
	else:
		print "You failed."
sum_questions()
def main():
	print "Welcome to the conditionals mental maths game.\n"
	print raw_input("Choose a category: addition, subtraction, multiplication, division.")
