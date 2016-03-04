# Total : (39.5/40)

#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for? (1)
#It is an assignment operator and it assigns values from the right side operands to the left side operands.
	#An operand is a value the operator is applied to.

#2 3pts) Write a technical definition for 'function.' (3)
#A function is a named sequence of statements that performs a computation/calculation. It is a block of organized, reusable code that is used to perform a single, related action.

#3 1pt) What does the keyword "return" do? (1)
#It spits out a calue (returns) immediately from the specific function and uses the following expression (code that follows return) as a return value.

#4 5pts) We know 5 basic data types. Write the name for each one and provide two examples of each below. (5)
#	1: string - "Hello" "Bye"
#	2: booleann - True, False
#	3: integer - 0, 456
#	4: floating point (float) - 0.0, 0.9
#	5: tuple - ("Se Min Park", "Hello", 47, "Bye"), ("Bye", "Hello", 45668.6, "Smile")

#5 2pts) What is the difference between a "function definition" and a "function call"? (2)
#A function call is when you define a function and specify it name and the sequence of statements that follows. Later, you can call the function by the name you defined it as.A function definition, on the other hand, specifies the name of a new function and the sequence of statements that execute when the function is called. definition

#6 3pts) What are the 3 phases that every computer program has? What happens in each of them? (3)
#	1: Input - This is a function that is called so the program stops and waits for the user to type something.
#	2: Calculation - This is the main part of the function, where the computations will be done. It may use variables defined in the input stage.
#	3: Output - This is what the function yields when it is called. The most basic form is print().

#Part 2: Programming (25 points) 
#Write a program that asks the user for the areas of 3 circles. (25)
	#It should then calculate the diameter of each and the sum of the diameters of the 3 circles.
	#Finally, it should produce output like this:
		#Circle  Diameter
		#c1      ...
		#c2      ...
		#c3      ...
		#TOTALS  ...
	# Hint: Radius is the square root of the area divided by pi

#1 pt for header line (1)
#3 pt for correct formula (3)
#1 pt for return value (1)
#1 pt for parameter name(1)
#1 pt for function name (1)
import math
def areaofcircle1(x):
	return float(x)
def areaofcircle2(y):
	return float(y)
def areaofcircle3(z):
	return float(z)
def diameter(a):
	return 2 * math.sqrt(a / (math.pi))
def add(s, t, u):
	return s + t + u

#1pt for header line(1)
#1pt for parameter names (1)
#1pt for return value (1)
#1pt for correct output format (1)
#3pt for correct use of format function (3)
def output(diameter1, diameter2, diameter3, sumofdiameters):
	out = """
Diameter of circle 1: {}\n
Diameter of circle 2: {}\n
Diameter of circle 3: {}\n

Sum of the diameters of the circles: {}
""".format(diameter1, diameter2, diameter3, sumofdiameters)
	return out

#1pt header line (1)
#1pt getting input (1)
#1pt converting input (1)
#1pt for calling output function (1)
#2pt for correct diameter formula (2)
#1pt for variable names (1)
#1pt for calling main(1)
def main():
	#Input
	x = int(raw_input("Area of circle 1 (make sure it is not a negative value):\n"))
	y = int(raw_input("Area of circle 2 (make sure it is not a negative value):\n"))
	z = int(raw_input("Area of circle 3 (make sure it is not a negative value):\n"))	
	#Processing	
	diameter1 = diameter(x)
	diameter2 = diameter(y)
	diameter3 = diameter(z)
	sumofdiameters = add(diameter1, diameter2, diameter3)
	#Output
	out = output(diameter1, diameter2, diameter3, sumofdiameters)
	print out
main()

#1pt explanatory comments (1)
#1pt code format (0.5)
#1pt for no errors while running code (1)
