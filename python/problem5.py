# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def factor(n):
  k = 1
  factors = []
  while k < n:
    a = n / k
    if a == int(a):
      factors.append(k)
      factors.append(factor(k))

  return factors

def group_factors(factors):
  d = {}
  for f in factors:
    if d.has_key(f):
      d[f] += 1
    else:
      d[f] = 1

  return d



def smallest_multiple(min_number, max_number):
  # Remove each element of array that has a number for which it is a factor
  array = range(min_number, max_number+1)
  d = {}
  for e in array:
    n = n * e
    if is_divisible(n, array):
      return n


a0 = 1
a1 = 20

print "Smallest positive number between {0} and {1} that can be divisible be each member is: {2}".format(a0, a1, smallest_multiple(a0, a1))