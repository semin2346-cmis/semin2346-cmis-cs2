x = "2"
y = int(x) * 45
print y

r = 6
diameter = 2 * r
print float(diameter) * (3 ** 2)
print 2 * str(diameter)

word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
lenword = len(word)
print lenword
print int(lenword) * 2
print 2 * str(lenword)

import math

print math.factorial(len(word))
print math.pi
print len(str(math.pi)) - 2

def need_help(name):
	print "Please do help me %s" % name + "."
	print "I like to write essays."
need_help("Fred")

def go_home(word,term):
	print "I think I should go home %s" % word + "."
	print "I want to go to sleep %s" % term + "."
go_home("now","please")


name = raw_input("What's your name? \n")
word = raw_input("Type a word. \n")
x = len(word)

print name + ", did you know that \"" + word + "\" has " + str(x) + " letters in it?"

bob = """
{}, did you know that "{}" has {} letters in it?
""".format(name, word, x) 

print bob
