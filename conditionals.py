#This game will give you 5 mental maths questions pertaining to the category you pick-addition, subtraction, multiplication, division.
#At the end of the quiz, it will give you a score out of 5.

import math
import random

def add(a, b):
	return int(a) + int(b)

def sum_questions():
	minimum_sum = int(raw_input("Please type a minimum number for your questions. "))
	maximum_sum = int(raw_input("Please type a maximum number for your questions. "))
	print "None of the numbers used in the questions will exceed the set extremes."
	sum1 = str(random.randint(minimum_sum, maximum_sum)) + "+" + str(random.randint(minimum_sum, maximum_sum))
	print sum1	
	estimation_sum1 = raw_input("Answer to question 1: ")	
	sum2 = str(random.randint(minimum_sum, maximum_sum)) + "+" + str(random.randint(minimum_sum, maximum_sum))
	print sum2
	estimation_sum2 = raw_input("Answer to question 2: ")	
	sum3 = str(random.randint(minimum_sum, maximum_sum)) + "+" + str(random.randint(minimum_sum, maximum_sum))
	print sum3
	estimation_sum3 = raw_input("Answer to question 3: ")	
	sum4 = str(random.randint(minimum_sum, maximum_sum)) + "+" + str(random.randint(minimum_sum, maximum_sum))
	print sum4	
	estimation_sum4 = raw_input("Answer to question 4: ")
	sum5 = str(random.randint(minimum_sum, maximum_sum)) + "+" + str(random.randint(minimum_sum, maximum_sum))
	print sum5	
	estimation_sum5 = raw_input("Answer to question 5: ")
	sum_answer1 = add(random.randint(minimum_sum, maximum_sum), random.randint(minimum_sum, maximum_sum))
	sum_answer2 = add(random.randint(minimum_sum, maximum_sum), random.randint(minimum_sum, maximum_sum))
	sum_answer3 = add(random.randint(minimum_sum, maximum_sum), random.randint(minimum_sum, maximum_sum))
	sum_answer4 = add(random.randint(minimum_sum, maximum_sum), random.randint(minimum_sum, maximum_sum))
	sum_answer5 = add(random.randint(minimum_sum, maximum_sum), random.randint(minimum_sum, maximum_sum))
	if estimation_sum1 == sum_answer1:
		print "Correct."
	
sum_questions()

def main():
	print "Welcome to the conditionals mental maths game.\n Choose a category: addition, subtraction, multiplication, division."

