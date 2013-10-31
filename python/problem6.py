# Problem 6

# The sum of the squares of the first ten natural numbers is:
#   1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#   (1 + 2 + ... 10)^2 = 3025
#
# Hence the difference between the sum of the squares and the square of the sum
# for those numbers is 3025 - 385
#
# Find the difference of the sum of the squares and the square of the sum
# for the first 100 natural numbers

def sum_of_squares_for_range(r):
  return reduce(lambda x, y: x + y**2, r, 0)

def square_of_sum_for_range(r):
  return reduce(lambda x, y: x + y, r, 0)**2

def difference_for_range(r):
  return square_of_sum_for_range(r) - sum_of_squares_for_range(r)

range100 = range(1, 100+1)
print "Difference = {0}".format(difference_for_range(range100))