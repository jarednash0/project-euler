natural_numbers = list(xrange(1,101))

def sum_of_squares(natural_numbers):
	sum_squares = 0
	for number in natural_numbers:
		sum_squares += number**2
	return sum_squares

def square_of_sums(natural_numbers):
	square_sums = 0
	for number in natural_numbers:
		square_sums += number
	square_sums = square_sums**2
	return square_sums

difference = square_of_sums(natural_numbers) - sum_of_squares(natural_numbers)

print difference