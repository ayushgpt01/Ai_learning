from math import isclose

def joint_probability(p_b_given_a: float, p_a: float):
  # This function computes the joint probability of two events occurring,
  # given the probability of one of the events and the probability of the second
  # event given the first event.
  #
  # p_a is the probability of event A, i.e. P(A)
  # p_b_given_a is the probability of event B given event A, i.e. P(B|A)
  #
  # The joint probability of two events occurring is computed as:
  # P(A and B) = P(B|A) * P(A)
  #
  # This is also known as the probability of event A given event B, i.e. P(A|B).
  # This can be computed using Bayes' Theorem, which states that:
  # P(A|B) = [P(B|A) * P(A)] / P(B)
  #
  # So this function is computing the numerator of Bayes' Theorem, i.e. P(B|A) * P(A)
  return p_a * p_b_given_a

def bayes_theorem(p_a: float, p_b: float, p_b_given_a: float):
  # p_a: Probability of event A, P(A)
  # p_b: Probability of event B, P(B)
  # p_b_given_a: Probability of event B given event A has occurred, P(B|A)

  # Calculate the conditional probability of A given B, P(A|B)
  # According to Bayes' Theorem:
  # P(A|B) = [P(B|A) * P(A)] / P(B)
  # Here, conditional_probability(p_b_given_a, p_a) computes P(B|A) * P(A)
  return joint_probability(p_b_given_a, p_a) / p_b  # Divide by P(B) to get P(A|B)

p_a = 7/10
p_b = 7/10
p_a_and_b = 5/10

print(joint_probability(p_a_and_b, p_a))
print(bayes_theorem(p_a, p_b, p_a_and_b))

assert isclose(bayes_theorem(0.7, 0.7, 0.5), 0.5)
