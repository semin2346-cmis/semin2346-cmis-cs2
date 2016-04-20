n = int(raw_input("Type number. "))
o = int(raw_input("Type bigger number. "))

#def countup(n):
#	if n <= 10:
#		print "Ye."
#	else:
#		print n
#		countup(n + 1)
#countup(n)

def countup(start, stop):
	if start == stop:
		print "Ye."
	else:
		print start
		countup(start + 1, stop)
countup(1, 5)
