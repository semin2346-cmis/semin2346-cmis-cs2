#n = int(raw_input("Type number: "))
#def countup(n):
#	if n > 10:
#		print "Ye."
#	else:
#		print n
#		countup(n + 1)
#countup(n)

#def countup(start, stop):
#	if start > stop:
#		print "Ye.\n"
#	else:
#		print start
#		countup(start + 1, stop)
#countup(4, 10)

#def countdown(start, stop):
#	if start < stop:
#		print "Ye."
#	else:
#		print start
#		countdown(start - 1, stop)
#countdown(10, 4)

def adder(s): 
	s = raw_input("Next number: ")
	if s == '':
		print "No."
	else:
		adder(s)
adder("s")
