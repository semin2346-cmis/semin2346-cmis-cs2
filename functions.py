import math

#You add two numbers.
def add(a, b):
	return a + b
#print add(3, 4)
a = 5
b = 1
sigma = add(a, b)
#print sigma
sigma1 = add(5, 7)

#You subtract two numbers.
def sub(c, d):
	return c - d
#print sub(5, 3)
c = 2
d = 3
difference = sub(c, d)
#print difference
difference1 = sub(5, 6)

#You multiply two numbers.
def mul(e, f):
	return e * f
#print mul(4, 4)
e = 3
f = 4
product = mul(e, f)
#print product
product1 = mul(2, 4)

#You divide two numbers.
def div(g, h):
	return float(g)/h
#print div(2, 3)
g = 3
h = 4
quotient = div(g, h)
#print quotient
quotient1 = div(4, 1)

#You convert a number of seconds into hours.
def hours_from_seconds(i):
	return float(i)/3600
#print hours_from_seconds(86400)
i = 18000
numberofhoursinseconds = hours_from_seconds(i)
#print numberofhoursinseconds
numberofhoursinseconds1 = hours_from_seconds(36000)

#You find the area of a circle using math.pi * j ** 2 when j is the radius.
def circle_area(j):
	return (float(j) ** 2) * math.pi
#print circle_area(5)
j = 3
areaofcircle = circle_area(j)
#print areaofcircle
areaofcircle1 = circle_area(4)

#You find the volume of a sphere provided the k is the radius-use the formula k ** 3 * float(4)/3 * math.pi.
def sphere_volume(k):
	return (float(k) ** 3) * math.pi * (float(4)/3)
#print sphere_volume(5)
k = 3
volumeofsphere = sphere_volume(k)
#print volumeofsphere
volumeofsphere1 = sphere_volume(6)

#You find the average of the volumes of two spheres provided l and m are diameters.
def avg_volume(l, m):
	return (float(sphere_volume(l/2)) + sphere_volume(m/2))/2
#print avg_volume(10, 20)
l = 6
m = 4
averageofvolumeofspheres = avg_volume(l, m)
#print averageofvolumeofspheres
averageofvolumeofspheres1 = avg_volume(15, 12)

#You find the area of a triangle given 3 valid sides using Heron's formula.
def area(n, o, p):
	return math.sqrt(((n + o + p)/2) * (((n + o + p)/2) - n) * (((n + o + p)/2) - o) * (((n + o + p)/2) - p))
#print area(1, 2, 2.5)
n = 5
o = 4
p = 3
heronsformula = area(n, o, p)
#print heronsformula
heronsformula1 = area(6, 7, 8)

#You align a random term along the right end of the screen that is 80 spaces long.
def right_align(term):
	return (80 - len(term)) * " " + term
#print right_align("Hello")
term = "Blue"
termalignedright = right_align(term)
#print termalignedright
termalignedright1 = right_align("Purple")

#You center a random word on the center of the screen that is 80 spaces long.
def center(word):
	return (40 - (len(word)/2)) * " " + word
#print center("Hello")
word = "I am Se Min."
centeredword = center(word)
#print centeredword
centeredword1 = center("Awesome.")

#You make a little box around the statements.
def msg_box(statement):
	return "+" + (len(statement) + 4) * "-" + "+\n" "|" + "  " + statement + "  " + "|\n" "+" + (len(statement) + 4) * "-" + "+"
print msg_box("Hello")
statement = "I want to go home."
boxedstatement = msg_box(statement)
print boxedstatement

print msg_box("The result of add is " + str(sigma) + ".") #Printed my variable sigma in a msg_box.
print msg_box("Another result of add is " + str(sigma1) + ".") #Printed my variable sigma1 in a msg_box.
print msg_box("The result of sub is " + str(difference) + ".") #Printed my variable difference in a msg_box.
print msg_box("Another result of sub is " + str(difference1) + ".") #Printed my variable difference1 in a msg_box.
print msg_box("A result of mul is " + str(product) + ".") #Printed my variable product in a msg_box.
print msg_box("Another result of mul is " + str(product1) + ".") #Printed my variable product1 in a msg_box.
print msg_box("A result of div is " + str(quotient) + ".") #Printed my variable quotient in a msg_box.
print msg_box("Another result of div is " + str(quotient1) + ".") #Printed my variable quotient1 in a msg_box.
print msg_box(str(numberofhoursinseconds)) #Printed my variable numberofhousinseconds in a msg_box.
print msg_box(str(numberofhoursinseconds1)) #Printed my variable numberofhousinseconds1 in a msg_box.
print msg_box(str(volumeofsphere)) #Printed my variable volumeofsphere in a msg_box.
print msg_box(str(volumeofsphere1)) #Printed my variable volumeofsphere1 in a msg_box.
print msg_box(str(averageofvolumeofspheres)) #Printed my variable averageofvolumeofspheres in a msg_box.
print msg_box(str(averageofvolumeofspheres1)) #Printed my variable averageofvolumeofspheres1 in a msg_box.
print msg_box(str(heronsformula)) #Printed my variable heronsformula in a msg_box.
print msg_box(str(heronsformula1)) #Printed my variable heronsformula1 in a msg_box.
print msg_box(termalignedright) #Printed my variable termalignedright in a msg_box.
print msg_box(termalignedright1) #Printed my variable termalignedright1 in a msg_box.
print msg_box(centeredword) #Printed my variable centeredword in a msg_box.
print msg_box(centeredword1) #Printed my variable centeredword1 in a msg_box.
