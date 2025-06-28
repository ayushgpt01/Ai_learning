from decimal import Decimal, getcontext
from math import fsum
from typing import Sequence, Union

def mean_with_error(values: Sequence[int], probabilities: Sequence[float]) -> float:
  if len(values) != len(probabilities):
    raise ValueError("Values and probabilities must have the same length")
  return sum(values[i] * probabilities[i] for i in range(len(values)))

def mean_decimal(values: Sequence[int], probabilities: Sequence[float]) -> Decimal:
  if len(values) != len(probabilities):
    raise ValueError("Values and probabilities must have the same length")
  
  # Set the precision for decimal calculations
  getcontext().prec = 50

  # Convert inputs to Decimal objects
  decimal_values = [Decimal(str(v)) for v in values] # Convert int to Decimal
  decimal_probabilities = [Decimal(str(p)) for p in probabilities] # Convert float strings to Decimal

  sum_products = Decimal('0')
  for i in range(len(decimal_values)):
    sum_products += decimal_values[i] * decimal_probabilities[i]
  
  return sum_products

def mean_fsum(values: Sequence[int], probabilities: Sequence[float]) -> float:
  if len(values) != len(probabilities):
    raise ValueError("Values and probabilities must have the same length")
  
  return fsum(values[i] * probabilities[i] for i in range(len(values)))

def variance(values: Sequence[int], probabilities: Sequence[float], mean: float | None = None) -> float:
  if len(values) != len(probabilities):
    raise ValueError("Values and probabilities must have the same length")
  
  if mean is None:
    mean = mean_with_error(values, probabilities)
  
  return fsum(((values[i] - mean) ** 2) * probabilities[i] for i in range(len(values)))  

def variance_with_decimal(values: Sequence[int], probabilities: Sequence[float], mean: Decimal | None = None) -> Decimal:
  if len(values) != len(probabilities):
    raise ValueError("Values and probabilities must have the same length")
  
  if mean is None:
    mean = mean_decimal(values, probabilities)
    
  # Set the precision for decimal calculations
  getcontext().prec = 50
    
  decimal_values = [Decimal(str(v)) for v in values] # Convert int to Decimal
  decimal_probabilities = [Decimal(str(p)) for p in probabilities] # Convert float strings to Decimal

  sum_products = Decimal('0')
  for i in range(len(decimal_values)):
    sum_products += ((decimal_values[i] - mean) ** 2) * decimal_probabilities[i]
  
  return sum_products

def standard_deviation(values: Union[float, Sequence[int]], probabilities: Sequence[float] | None = None, mean: float | None = None) -> float:
  if isinstance(values, Sequence):
    if probabilities is None or len(values) != len(probabilities):
      raise ValueError("Values and probabilities must have the same length")
    
    values = variance(values, probabilities, mean)
    
  return values ** 0.5

def standard_deviation_with_decimal(values: Union[Decimal, Sequence[int]], probabilities: Sequence[float] | None = None, mean: Decimal | None = None) -> Decimal:
  if isinstance(values, Sequence):
    if probabilities is None or len(values) != len(probabilities):
      raise ValueError("Values and probabilities must have the same length")
    
    values = variance_with_decimal(values, probabilities, mean)
    
  return values ** Decimal(0.5)

values = [-10000, 40000, 90000]
probabilities = [0.81, 0.18, 0.01]

result_decimal = mean_decimal(values, probabilities)
result_with_error = mean_with_error(values, probabilities)
result_fsum = mean_fsum(values, probabilities)
result_variance = variance(values, probabilities)
result_standard_deviation = standard_deviation(result_variance)
result_variance_with_decimal = variance_with_decimal(values, probabilities)
result_standard_deviation_with_decimal = standard_deviation_with_decimal(result_variance_with_decimal)

print(f"Result with Decimal: {result_decimal}")
print(f"Result with Error: {result_with_error}")
print(f"Result with fsum: {result_fsum}")

print(f"Variance With Error: {result_variance}")
print(f"Standard Deviation With Error: {result_standard_deviation}")
print(f"Variance With Decimal: {result_variance_with_decimal}")
print(f"Standard Deviation With Decimal: {result_standard_deviation_with_decimal}")

