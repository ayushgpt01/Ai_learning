from math import factorial

e = 2.71828

def poisson_distribution(lbd: float, k: int) -> float:
  # It comes from taking a very large lbd for a binomial distribution
  return (lbd ** k) * (e ** (-lbd)) / (factorial(k))
  