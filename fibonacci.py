#!/usr/bin/env python

# 0 1 1 2 3 5 8 13

#alternative would be to print a series starting at x and go to kth number
#x = 12
#12 13 25 38 63 101



def fibonacci(x):
	sequence_list = []

	current = 0
	next = 1
	
	for i in range (x):
	
		sequence_list.append(current)
		current = next
		if i > 0:
			next = sequence_list[i] + current
		else:
			next = 1
	return sequence_list	
	

#produces a sum for the kth fibonacci number
def print_fibonacci(x):
	print str(fibonacci(x))
	
print print_fibonacci (7)