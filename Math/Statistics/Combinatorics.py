from math import prod, perm, comb


# Can also use math.factorial, which is much faster than even this implementation
def factorial(num : int) -> int:
  if num == 0: return 1
  if num < 0: raise ValueError("Factorial is not defined for negative numbers")

  # x = 1
  # for i in range(1, num + 1):
  #   x *= i
  # return x
  
  # Factorial using math.prod which is more efficient than python loop 
  # because math.prod is implemented in C
  return prod(range(1, num + 1))

def permutation(n: int, r: int):
  if r > n: return 0
  if n < 0 or r < 0: raise ValueError("n and r must be non-negative integers")
  # return factorial(n) // factorial(n - r)

  # Calculate the number of permutations of n items taken r at a time
  # The formula for permutation is n! / (n-r)!
  # where n! (n factorial) is the product of all positive integers up to n
  # and (n-r)! is the product of all positive integers up to (n-r)
  # This formula gives the number of ways to arrange r items out of n unique items
  
  # Permuation using math.perm which is more efficient than python factorials 
  # because math.perm is implemented in C
  return perm(n, r)

def combination(n: int, r: int):
  if r > n: return 0
  if n < 0 or r < 0: raise ValueError("n and r must be non-negative integers")
  # return permutation(n, r) // factorial(r)
  
  # Calculate the number of combinations of n items taken r at a time
  # The formula is n! / (r! * (n-r)!)
  # This is the same as the permutation formula, but divided by r!
  # because the order of the items doesn't matter in a combination
  # (the number of permutations of r items is r!)
  
  # Combination using math.comb which is more efficient than python factorials
  return comb(n, r)

def binomial_probability(n: int,k :int):
  # This is the binomial probability of observing k successes in n trials with 𝑝=0.5
  return combination(n, k) // 2 ** n

assert combination(5, 2) == 10
assert permutation(5, 2) == 20

print(permutation(5, 3))
print(combination(60, 4))