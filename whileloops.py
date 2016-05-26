#def countdown(x):
#	while x > 0:
#		print x
#		x -= 1
#countdown(10)

#def counter(x):
#	while x <= 0:
#		print x
#		x += 1
#		if x == y:
#			print y
#	while x >= 0:
#		print x
#		x -= 1
#		if x == y:
#			print y
#counter(-6)

#def counting(x, y):
#	while x < y:
#		print x
#		x += 1
#		if x == y:
#			print y
#	while x > y:
#		print x
#		x -= 1
#		if x == y:
#			print y
#counting(9, 2)
#counting(2, 9)

def sum_of_odds(x, y = 0):
	while x < 0:
		print x
		x += 1
		while x % 2 == 1:
			print sum_of_odds(x + x, y + 1)
	while x > 0:
		print x
		x -= 1
		while x % 2 == 1:
			print sum_of_odds(x + x, y + 1)
sum_of_odds(5)


































