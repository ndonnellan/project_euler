# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys

def list_of_factors(n):
  k = 2.0
  factors = []
  a = 0
  while k <= n:
    a = n / k
    if a == int(a):
      factors.append(k)
      if a == 1:
        return factors
      else:
        return factors + list_of_factors(a)
    else:
      k += 1

  return factors

def group_factors(factors):
  d = {}
  for f in factors:
    if d.has_key(f):
      d[f] += 1
    else:
      d[f] = 1

  return d



def smallest_set_of_factors(numbers):
  # Return the smallest set of factors necessary to create any number
  # in the list
  dict_of_factors = {}
  for n in numbers:
    sys.stdout.write("n = {0}".format(n))
    factors = group_factors(list_of_factors(n))

    for k, power in factors.iteritems():
      sys.stdout.write(" {0}^{1}, ".format(int(k), power))
      if not (dict_of_factors.has_key(k)) or (power > dict_of_factors[k]):
          dict_of_factors[k] = power

    sys.stdout.write("\n")
  return dict_of_factors

def smallest_multiple_in_range(numbers):
  m = 1
  for k, power in smallest_set_of_factors(numbers).iteritems():
    m = m * (k ** power)

  return m

a0 = 1
a1 = 20

print "Smallest positive number between {0} and {1} that can be divisible be each member is: {2}".format(a0, a1, smallest_multiple_in_range(range(a0, a1+1)))