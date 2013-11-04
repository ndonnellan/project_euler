# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a^2 + b^2 = c^2

# For example:
#   3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c
#
# => a^2 + b^2 = (1000 - (a + b))^2
# => a^2 + b^2 = 1000^2 - 2000(a + b) + (a + b)^2
# => a^2 + b^2 = 1000^2 - 2000a - 2000b + a^2 + 2ab + b^2
# => 0 = 1000^2 - 2000a - 2000b + 2ab

N = 1000

def f(a,b):
  return N**2 - 2*N*a - 2*N*b + 2*a*b

def find_triplet(a0, b0):
  a = a0
  b = b0

  # Since 'a' must be less than 'b' and 'c', we can assume it's bounded by 1/3 of N
  while a < N / 3:
    if f(a, b) == 0:
      return [a, b, N - (a + b)]

    elif b >= N / 2:
      # Since 'b' must be less than 'c' we can assume it's bounded by 1/2 of N
      # Once we reach that bound, walk 'a' up one and reset 'b' to one above 'a'
      a += 1
      b = a + 1

    else:
      # Otherwise, walk 'b' up
      b += 1

  return [0,0,0]

ans = find_triplet(1,2)
print "The Pythagorean triplet for which a + b + c = 1000 is {0}".format(ans)
print "The product abc is {0}".format(reduce(lambda x,y: x*y, ans))
