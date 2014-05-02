factor_1 = list(xrange(999, 99, -1))
factor_2 = list(xrange(100, 1000))
highest_palindrome = None

def isPalindrome(attempt_at_palindrome):
	forwards = str(attempt_at_palindrome)
	backwards = str(''.join(reversed(forwards)))
	if forwards == backwards:
		return True
	else:
		return False

	
while highest_palindrome == None:
	for factor in factor_1:
		highest_factor = factor_2.pop()
		attempt_at_palindrome = factor * highest_factor
		if isPalindrome(attempt_at_palindrome) == True:
			highest_palindrome = attempt_at_palindrome
		else:
			pass

print highest_palindrome