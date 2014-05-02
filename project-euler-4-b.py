factor_1 = list(xrange(999, 99, -1))
attempts_unordered = []
a = 999
highest_palindrome = None

while a > 99:
	for factor in factor_1:
		attempts_unordered.append(factor * a)
	a = a -1
	
attempts = sorted(attempts_unordered, reverse=True)

def isPalindrome(attempt):
	forwards = str(attempt)
	backwards = str(''.join(reversed(forwards)))
	if forwards == backwards:
		return True
	else:
		return False

	
while highest_palindrome == None:
		for attempt in attempts:
			if isPalindrome(attempt) == True:
				highest_palindrome = attempt
				break
			else:
				pass

print highest_palindrome