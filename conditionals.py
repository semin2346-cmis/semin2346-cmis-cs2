#This game will give you 5 mental maths questions pertaining to the category you pick-addition, subtraction, multiplication, division.
#At the end of the quiz, it will give you a score out of 5.

import math
import random

def add(a, b):
	return int(a) + int(b)
def mul(a, b):
	return int(a) * int(b)

#Addition quiz.
def sum_questions():
	#Boundaries for equation.	
	minimum_sum = int(raw_input("Please type a minimum value for your questions. "))
	maximum_sum = int(raw_input("Please type a maximum value for your questions. "))
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
	#Variable for grading.
	numbercorrect = 0
	print "None of the numbers used in the questions will exceed the set extremes."
	#Question 1.
	sum1 = str(a1) + "+" + str(a2)
	print sum1	
	estimation_sum1 = raw_input("Answer to question 1: ")	
	if int(estimation_sum1) == int(sum_answer1):
		numbercorrect = numbercorrect + 1		
		print "Correct."	
	else:
		print "Incorrect."
	#Question 2.
	sum2 = str(b1) + "+" + str(b2)
	print sum2
	estimation_sum2 = raw_input("Answer to question 2: ")	
	if int(estimation_sum2) == int(sum_answer2):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 3.
	sum3 = str(c1) + "+" + str(c2)
	print sum3
	estimation_sum3 = raw_input("Answer to question 3: ")	
	if int(estimation_sum3) == int(sum_answer3):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 4.	
	sum4 = str(d1) + "+" + str(d2)
	print sum4	
	estimation_sum4 = raw_input("Answer to question 4: ")
	if int(estimation_sum4) == int(sum_answer4):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."	
	#Question 5.
	sum5 = str(e1) + "+" + str(e2)
	print sum5	
	estimation_sum5 = raw_input("Answer to question 5: ")
	if int(estimation_sum5) == int(sum_answer5):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Scoring.
	if numbercorrect >= 3:
		print "You passed. Your score is " + str(numbercorrect) + " out of 5."
	else:
		print "You failed. Your score is " + str(numbercorrect) + " out of 5."

#Multiplication quiz.
def product_questions():
	#Boundaries for equation.	
	minimum_product = int(raw_input("Please type a minimum value for your questions. "))
	maximum_product = int(raw_input("Please type a maximum value for your questions. "))
	#Variables for equation.
	f1 = random.randint(minimum_product, maximum_product)
	f2 = random.randint(minimum_product, maximum_product)
	g1 = random.randint(minimum_product, maximum_product)
	g2 = random.randint(minimum_product, maximum_product)
	h1 = random.randint(minimum_product, maximum_product)
	h2 = random.randint(minimum_product, maximum_product)
	i1 = random.randint(minimum_product, maximum_product)
	i2 = random.randint(minimum_product, maximum_product)
	j1 = random.randint(minimum_product, maximum_product)
	j2 = random.randint(minimum_product, maximum_product)
	#Answers for equation.
	product_answer1 = mul(f1, f2)
	product_answer2 = mul(g1, g2)
	product_answer3 = mul(h1, h2)
	product_answer4 = mul(i1, i2)
	product_answer5 = mul(j1, j2)
	#Variable for grading.
	numbercorrect = 0
	print "None of the numbers used in the questions will exceed the set extremes."
	#Question 1.
	product1 = str(f1) + "*" + str(f2)
	print product1	
	estimation_product1 = raw_input("Answer to question 1: ")	
	if int(estimation_product1) == int(product_answer1):
		numbercorrect = numbercorrect + 1		
		print "Correct."	
	else:
		print "Incorrect."
	#Question 2.
	product2 = str(g1) + "*" + str(g2)
	print product2
	estimation_product2 = raw_input("Answer to question 2: ")	
	if int(estimation_product2) == int(product_answer2):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 3.
	product3 = str(h1) + "*" + str(h2)
	print product3
	estimation_product3 = raw_input("Answer to question 3: ")	
	if int(estimation_product3) == int(product_answer3):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 4.	
	product4 = str(i1) + "*" + str(i2)
	print product4	
	estimation_product4 = raw_input("Answer to question 4: ")
	if int(estimation_product4) == int(product_answer4):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."	
	#Question 5.
	product5 = str(j1) + "*" + str(j2)
	print product5	
	estimation_product5 = raw_input("Answer to question 5: ")
	if int(estimation_product5) == int(product_answer5):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Scoring.
	if numbercorrect >= 3:
		print "You passed. Your score is " + str(numbercorrect) + " out of 5."
	else:
		print "You failed. Your score is " + str(numbercorrect) + " out of 5."

#Main function.
def main():
	print "Welcome to the conditionals mental maths game.\n"
	z = raw_input("Choose a category: addition, subtraction, multiplication, division. ")
	print z
	if z == "addition":
		sum_questions()
	elif z == "multiplication":
		product_questions()
	else:
		print "Dude, you had one job. How can you already fail?"
main()
