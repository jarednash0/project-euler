a = 1
b = 2
f = 0

while b <= 4000000:
	if b % 2 == 0:
		f = f + b
	c = a + b
	a = b
	b = c

print f
