#Section 1: Terminology
#	1)What is a recursive function?
#		It is a function that calls itself within its body (definition).
#	2)What happens if there is no base case defined in a recursive function?
#		It will repeat infinitely (i.e., infinite recursion)-python will eventually print a runtime error when it reaches its recursion limit.
#	3)What is the first thing to consider when designing a recursive function?
#		Its base case, to determine when the function stops (i.e., what its ultimate goal is), and recursive case.
#	4)How do we put data into a function call?
#		By using specific parameters when you call that function.
#	5)How do we get data out of a function call?
#		By using specific parameters when you call that function.

#Section 2: Reading
#	Read the following function definitions and function calls.
#	Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 = 4
#c3 = 45

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#	Write a script that asks the user to enter a series of numbers.
#	When the user types in nothing, it should return the average of all the odd numbers
#	that were typed in. 
#	In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#	Also add a comment label BEFORE the recursive case.
#	It is NOT NECESSARY to print out a running total with each user input.

def odd_avg(addition = 0, odds = 0):
	number = raw_input("Please type in your next number for this quiz game: ")
	if number == "":
		print """The average of only the odd numbers you listed during this game is: {}""".format(addition/odds)
	else:
		if float(number) % 2 == 0:
			return odd_avg(addition, odds)
		else:
			return odd_avg(addition + float(number), odds + 1)
odd_avg() 
