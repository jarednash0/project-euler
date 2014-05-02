base_number = 600851475143
def findFactors(base_number):
	factors = []
	if base_number % 2 ==0:
		half = base_number/2
	else:
		half = (base_number - 1)/2
	prime_tries = list(xrange(half+1))
	for try in prime_tries:
		result = base_number/try
		if isinstance(result, int) = True
			factors.append(try)
		else:
			pass
	return factors

def findLargestPrime(factors):
	final_factor = None
	while final_factor = None:
		