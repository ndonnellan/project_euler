# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math

def is_prime(n):
  k = 2.0
  while k <= math.sqrt(n):
    a = n / k
    if a == int(a):
      return False
    else:
      k += 1

  return True


def sum_primes_up_to(max_number):
  s = 2 # Start at two
  n = 3

  while n < max_number:
    if is_prime(n):
      s += n

    n += 1

  return s

N = 2000000
print "Sum of primes up to {0} is {1}".format(N, sum_primes_up_to(N))
