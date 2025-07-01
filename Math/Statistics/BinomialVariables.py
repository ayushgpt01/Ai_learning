from Combinatorics import combination

def binomial_probability(n: int,k :int) -> float:
  """
  Returns the binomial probability of getting exactly k successes out of n trials
  with a fair coin (p = 0.5).
  """
  if not (0 <= k <= n):
    raise ValueError("k must be between 0 and n (inclusive)")
  return combination(n, k) // 2 ** n

def binompdf(n: int, k: int, success_probability: float) -> float:
  if not (0 <= k <= n):
    raise ValueError("k must be between 0 and n (inclusive)")
  if not (0 <= success_probability <= 1):
    raise ValueError("success_probability must be between 0 and 1")
  # This is the binomial probability distribution function
  return combination(n, k) * (success_probability ** k) * ((1 - success_probability) ** (n - k))

def binomcdf(n: int, k: int, success_probability: float) -> float:
  if not (0 <= k <= n):
    raise ValueError("k must be between 0 and n (inclusive)")
  if not (0 <= success_probability <= 1):
    raise ValueError("success_probability must be between 0 and 1")
  # This is the binomial cumulative distribution function
  return sum(binompdf(n, i, success_probability) for i in range(k + 1))

def bernoulli_mean(p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the mean of a Bernoulli distribution with formula (0 * (1-p)) + (1 * p)
  # which is the same as the probability of getting a success
  return p

def beranulli_variance(p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the variance of a Bernoulli distribution with formula (1-p)((0-p)**2) + p(1 * p) ** 2
  return p * (1 - p)

def bernoulli_std_deviation(p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the standard deviation of a Bernoulli distribution
  return beranulli_variance(p) ** 0.5

def expected_value(n: int, p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the expected value of a binomial distribution with formula n * p
  # This comes from addition of n expected values
  
  # X : No. of successes from n trials where p is the probability 
  # of success for each independent trial
  # Y : Probability of success for Y is p and failure is 1 - p
  
  # E(X + Y) = E(X) + E(Y)
  # In our case equation is E(X) = E(Y) + E(Y) + ... + E(Y) -> n times
  # Which solving for E(X) gives us n * E(Y)
  # and E(Y) is the expected value of a binominal distribution with n trials and p probability
  # which is p * 1 + (1 - p) * 0
  # Solving, all this gives us n * p
  return n * p

def variance(n: int, p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the variance of a binomial distribution with formula n * p * (1 - p)
  
  return n * p * (1 - p) 

def standard_deviation(n: int, p: float) -> float:
  if not (0 <= p <= 1):
    raise ValueError("p must be between 0 and 1")
  # This is the variance of a binomial distribution with formula n * p * (1 - p)
  
  return variance(n, p) ** 0.5

print(f"{binomial_probability(60, 4) * 100}%")
print(f"{binompdf(7, 4, 0.35) * 100}%")
print(f"{binomcdf(7, 4, 0.35) * 100}%")

print(f"{expected_value(500, 0.02)}")
print(f"{standard_deviation(500, 0.02)}")