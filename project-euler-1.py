full = list(xrange(1000))
a = 0
for f in full:
	if f % 3 == 0:
		a = a + f
	elif f % 5 == 0:
		a = a + f
	else:
		pass

print a