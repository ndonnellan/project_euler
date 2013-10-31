# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import sys

def print_int(i):
  sys.stdout.write("{:.0f} x ".format(round(i)))

def prime_factor(n):
  d = 2.0
  q = n
  while d < n:
    q = n / d
    if q == round(q):
      print_int(q)
      return prime_factor(round(q))

    d += 1

  return d


k = 600851475143
f = prime_factor(k)
print "Largest prime factor of {:.0f} is {:.0f}".format(k, f)