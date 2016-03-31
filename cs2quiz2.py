#PART 1: TERMINOLOGY
#1) Give 3 examples of boolean expressions.
	#a) 1 == 1 (True)
	#b)	2 != 2 (False)
	#c) 3 > 3 (False)

#2) What does 'return' do?
	#It spits out a value immediately from the function and uses the following expressions as the return value. 
	#It also sets variables to a value in a function.

#3) What are 2 ways indentation is important in python code?
	#a)It delimits the function structures-it denotes the code blocks.
	#b)It makes reading the code easier-it enhances the readability of the function.

#PART 2: READING
#Type the values for 12 of the 16 of the variables below.
	#problem1_a) = -36 
	#problem1_b) = -sqrt(3)
	#problem1_c) = 0
	#problem1_d) = -5

	#problem2_a) = True
	#problem2_b) = False
	#problem2_c) = False
	#problem2_d) = True

	#problem3_a) = 0.3
	#problem3_b) = 0.5
	#problem3_c) = 0.5
	#problem3_d) = 0.5

	#problem4_a) = 7
	#problem4_b) = 5
	#problem4_c) = 0.125
	#problem4_d) = 5

#PART 3: PROGRAMMING
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function).

import math

def compare(a, b, c):
	if float(a) > float(b) > float(c):
		return str(a) + " is the largest number."
	elif float(b) < float(c) < float(a):
		return str(a) + " is the largest number."
	elif float(a) < float(b) < float(c):
		return str(c) + " is the largest number."
	elif float(b) < float(a) < float(c):
		return str(c) + " is the largest number."
	elif float(a) < float(c) < float(b):
		return str(b) + " is the largest number."
	elif float(c) < float(a) < float(b):
		return str(b) + " is the largest number."
	elif float(a) >= float(b) >= float(c):
		return "You did not follow directions."
	elif float(b) <= float(c) <= float(a):
		return "You did not follow directions."
	elif float(a) <= float(b) <= float(c):
		return "You did not follow directions."
	elif float(b) <= float(a) <= float(c):
		return "You did not follow directions."
	elif float(a) <= float(c) <= float(b):
		return "You did not follow directions."
	elif float(c) <= float(a) <= float(b):
		return "You did not follow directions."
	elif float(a) == float(b) == float(c):
		return "You did not follow directions."
	else:
		"I don't know."	

def main():
	#Input
	x = float(raw_input("Type in a number-decimals are accepted. "))
	y = float(raw_input("Type in another number-decimals are accepted. "))
	z = float(raw_input("Type in the last number-decimals are accepted. "))
	#Processing/Output
	print compare(x, y, z)
main()
