#This game will give you 5 mental maths questions pertaining to the category you pick-addition, subtraction, multiplication, division.
#At the end of the quiz, it will give you a score out of 5.

import math
import random

def add(a, b):
	return int(a) + int(b)
def mul(a, b):
	return int(a) * int(b)
def diff(a, b):
	return int(a) - int(b)
def quot(a, b):
	return (float(a))/(float(b))

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

#Subtraction quiz.
def difference_questions():
	#Boundaries for equation.	
	minimum_difference = int(raw_input("Please type a minimum value for your questions. "))
	maximum_difference = int(raw_input("Please type a maximum value for your questions. "))
	#Variables for equation.
	k1 = random.randint(minimum_difference, maximum_difference)
	k2 = random.randint(minimum_difference, maximum_difference)
	l1 = random.randint(minimum_difference, maximum_difference)
	l2 = random.randint(minimum_difference, maximum_difference)
	m1 = random.randint(minimum_difference, maximum_difference)
	m2 = random.randint(minimum_difference, maximum_difference)
	n1 = random.randint(minimum_difference, maximum_difference)
	n2 = random.randint(minimum_difference, maximum_difference)
	o1 = random.randint(minimum_difference, maximum_difference)
	o2 = random.randint(minimum_difference, maximum_difference)
	#Answers for equation.
	difference_answer1 = diff(k1, k2)
	difference_answer2 = diff(l1, l2)
	difference_answer3 = diff(m1, m2)
	difference_answer4 = diff(n1, n2)
	difference_answer5 = diff(o1, o2)
	#Variable for grading.
	numbercorrect = 0
	print "None of the numbers used in the questions will exceed the set extremes."
	#Question 1.
	difference1 = str(k1) + "-" + str(k2)
	print difference1	
	estimation_difference1 = raw_input("Answer to question 1: ")	
	if int(estimation_difference1) == int(difference_answer1):
		numbercorrect = numbercorrect + 1		
		print "Correct."	
	else:
		print "Incorrect."
	#Question 2.
	difference2 = str(l1) + "-" + str(l2)
	print difference2
	estimation_difference2 = raw_input("Answer to question 2: ")	
	if int(estimation_difference2) == int(difference_answer2):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 3.
	difference3 = str(m1) + "-" + str(m2)
	print difference3
	estimation_difference3 = raw_input("Answer to question 3: ")	
	if int(estimation_difference3) == int(difference_answer3):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 4.	
	difference4 = str(n1) + "-" + str(n2)
	print difference4	
	estimation_difference4 = raw_input("Answer to question 4: ")
	if int(estimation_difference4) == int(difference_answer4):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."	
	#Question 5.
	difference5 = str(o1) + "-" + str(o2)
	print difference5	
	estimation_difference5 = raw_input("Answer to question 5: ")
	if int(estimation_difference5) == int(difference_answer5):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Scoring.
	if numbercorrect >= 3:
		print "You passed. Your score is " + str(numbercorrect) + " out of 5."
	else:
		print "You failed. Your score is " + str(numbercorrect) + " out of 5."

#Division quiz.
def quotient_questions():
	#Boundaries for equation.	
	minimum_quotient = float(raw_input("Please type a minimum value for your questions. "))
	maximum_quotient = float(raw_input("Please type a maximum value for your questions. "))
	#Variables for equation.
	p1 = random.randint(minimum_quotient, maximum_quotient)
	p2 = random.randint(minimum_quotient, maximum_quotient)
	q1 = random.randint(minimum_quotient, maximum_quotient)
	q2 = random.randint(minimum_quotient, maximum_quotient)
	r1 = random.randint(minimum_quotient, maximum_quotient)
	r2 = random.randint(minimum_quotient, maximum_quotient)
	s1 = random.randint(minimum_quotient, maximum_quotient)
	s2 = random.randint(minimum_quotient, maximum_quotient)
	t1 = random.randint(minimum_quotient, maximum_quotient)
	t2 = random.randint(minimum_quotient, maximum_quotient)
	#Answers for equation.
	quotient_answer1 = quot(p1, p2)
	quotient_answer2 = quot(q1, q2)
	quotient_answer3 = quot(r1, r2)
	quotient_answer4 = quot(s1, s2)
	quotient_answer5 = quot(t1, t2)
	#Variable for grading.
	numbercorrect = 0
	print "None of the numbers used in the questions will exceed the set extremes."
	#Question 1.
	quotient1 = str(p1) + "/" + str(p2)
	print quotient1	
	estimation_quotient1 = raw_input("Answer to question 1: ")	
	if float(estimation_quotient1) == float(quotient_answer1):
		numbercorrect = numbercorrect + 1		
		print "Correct."	
	else:
		print "Incorrect."
	#Question 2.
	quotient2 = str(q1) + "/" + str(q2)
	print quotient2
	estimation_quotient2 = raw_input("Answer to question 2: ")	
	if float(estimation_quotient2) == float(quotient_answer2):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 3.
	quotient3 = str(r1) + "/" + str(r2)
	print quotient3
	estimation_quotient3 = raw_input("Answer to question 3: ")	
	if float(estimation_quotient3) == float(quotient_answer3):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."
	#Question 4.	
	quotient4 = str(s1) + "/" + str(s2)
	print quotient4	
	estimation_quotient4 = raw_input("Answer to question 4: ")
	if float(estimation_quotient4) == float(quotient_answer4):
		numbercorrect = numbercorrect + 1
		print "Correct."
	else:
		print "Incorrect."	
	#Question 5.
	quotient5 = str(t1) + "/" + str(t2)
	print quotient5	
	estimation_quotient5 = raw_input("Answer to question 5: ")
	if float(estimation_quotient5) == float(quotient_answer5):
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
	print "Welcome to the conditionals mental maths game."
	z = raw_input("Choose a category: Addition, Subtraction, Multiplication, Division.")
	if z == "Addition" or z == "addition":
		sum_questions()
	elif z == "Subtraction" or z == "subtraction":
		difference_questions()
	elif z == "Multiplication" or z == "multiplication":
		product_questions()
	elif z == "Division" or z == "division":
		quotient_questions()
	else:
		print "Dude, you had one job. How can you already fail?"
main()
