# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

# This is a very simple brute force method. It takes under a minute to solve on a macbook air (2012)
import math

# Borrowed and modified from problem 5

def is_prime(n):
  k = 2.0
  while k <= math.sqrt(n):
    a = n / k
    if a == int(a):
      return False
    else:
      k += 1

  return True


k = 1
s = 0
N = 10001
while s < N:
  k += 1
  if is_prime(k):
    s += 1


print "The {0}th prime number is {1}".format(N, k)
