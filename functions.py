import math

def add(a, b):
	return a + b
print add(3, 4)
a = 5
b = 1
sigma = add(a, b)
print sigma

def sub(c, d):
	return c - d
print sub(5, 3)
c = 2
d = 3
difference = sub(c, d)
print difference

def mul(e, f):
	return e * f
print mul(4, 4)
e = 3
f = 4
product = mul(e, f)
print product

def div(g, h):
	return float(g)/h
print div(2, 3)
g = 3
h = 4
quotient = div(g, h)
print quotient

def secondstohours(i):
	return i/3600
print secondstohours(86400)
i = 18000
numberofhoursinseconds = secondstohours(18000)
print numberofhoursinseconds

def circlearea(j):
	return (float(j) ** 2) * math.pi
print circlearea(5)
j = 3
areaofcircle = circlearea(3)
print areaofcircle

def spherevolume(k):
	return (float(k) ** 3) * math.pi * (float(4)/3)
print spherevolume(5)

def averagespherevolumes(l, m):
	return (float(spherevolume(l/2)) + spherevolume(m/2))/2
print averagespherevolumes(10, 20)

def areaoftrianglegiven3sides(n, o, p):
	return math.sqrt(((n + o + p)/2) * (((n + o + p)/2) - n) * (((n + o + p)/2) - o) * (((n + o + p)/2) - p))
print areaoftrianglegiven3sides(1, 2, 2.5)

def alignright(term):
	return (80 - len(term)) * " " + term
print alignright("Hello")

def center(word):
	return (40 - (len(word)/2)) * " " + word
print center("Hello")

def messagebox(statement):
	return "+" + (len(statement) + 4) * "-" + "+\n" "|" + "  " + statement + "  " + "|\n" "+" + (len(statement) + 4) * "-" + "+"
print messagebox("Hello")

































