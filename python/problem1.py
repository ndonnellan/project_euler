# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def sum_of_3_or_5_multiples(max_number):
  sum_of_multiples = 0
  for n in range(0, max_number):
    if n % 3 == 0 or n % 5 == 0:
      sum_of_multiples += n
  return sum_of_multiples

print "Answer: %d", sum_of_3_or_5_multiples(1000)