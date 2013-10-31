# Largest palindrome product
# Problem 4

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
  s = str(n)
  return s[::-1] == s

def largest_palindrome_in_range(min_number, max_number):
  a = max_number
  b = max_number
  max_p = 0
  while min_number <= a:
    p = a * b
    if is_palindrome(p):
      if p > max_p:
        max_p = p

    if b == min_number:
      b = a - 1
      a = b
    else:
      b -= 1

  return max_p

m0 = 100
m1 = 999
print "Largest palindrome with factors between {0} and {1} is {2}".format(m0, m1, largest_palindrome_in_range(m0, m1))

