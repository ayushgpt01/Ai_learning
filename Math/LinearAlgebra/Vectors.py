from typing import Union

Number = Union[int, float]

# Vectors are ordered list of numbers (Array of number)
# Vector is a list and it's dimension is the order of array. So, a 2d vector is 
# vec[i][j]

# An advantage of vectors is that we can switch between the two notations
# of lists and geometric projections easily allowing us to model the data in
# lists and also visualize them in graphs.

class Vector:
  def __init__(self, items: list[Number] | tuple[Number, ...], dimension: int = -1):
    if dimension == -1: dimension = len(items)
    
    if dimension < 2:
      raise ValueError("Dimension must be an integer >= 2 (e.g., 2 for 2D, 3 for 3D)")
    if len(items) != dimension:
      raise ValueError(f"Items must be a list or tuple with {dimension} components")
  
    self.items = list(items)
    self._dimension = dimension
    
  @property
  def dimension(self) -> int:
    """
    Returns the dimension of the vector.
    This is a read-only property.
    """
    return self._dimension
    
  def __str__(self) -> str:
      """
      Returns a human-readable string representation of the Vector.
      Example: "3D Vector:[1, 2, 3]"
      """
      return f"{self.dimension}D Vector:{self.items}"

  def __repr__(self) -> str:
      """
      Returns an unambiguous string representation of the Vector,
      ideally allowing it to be recreated using eval().
      Example: "Vector([1, 2, 3])" or "Vector((1, 2, 3), dimension=3)"
      """
      return f"{self.__class__.__name__}({self.items})"
   
  def __add__(self, other: "Vector") -> "Vector":
    return addition(self, other)
  
  def __mul__(self, other: "Vector") -> Number:
    return dot_product(self, other)
  
  def __rmul__(self, scalar: Number) -> "Vector":
    return scalar_multiply(self, scalar)
  
  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Vector): return False
    return self.items == other.items and self.dimension == other.dimension
  
  def __getitem__(self, index: int) -> Number:
    return self.items[index]
  
  def magnitude(self) -> float:
    return sum(x * x for x in self.items) ** 0.5
  
  def normalize(self) -> "Vector":
    mag = self.magnitude()
    if mag == 0:
      raise ValueError("Cannot normalize zero vector")
    return 1/mag * self
  
  def __iter__(self):
    return iter(self.items)
  
  def __len__(self):
    return self.dimension
  
  @staticmethod
  def linear_combination(vectors: list["Vector"], scalars: list[Number]) -> "Vector":
    result = (s * v for s, v in zip(scalars, vectors))
    return sum(result, Vector([0.0] * vectors[0].dimension))

def scalar_multiply(vec: Vector, scalar: Number) -> Vector: 
  result = [x * scalar for x in vec.items]
  return Vector(result)

def dot_product(vec: Vector, vec2: Vector) -> Number:
  if (vec.dimension != vec2.dimension):
    raise ValueError("Vector dimensions must match")
  return sum(x * y for x, y in zip(vec, vec2))

def addition(vec: Vector, vec2: Vector) -> Vector:
  if (vec.dimension != vec2.dimension):
    raise ValueError("Vector dimensions must match")
  result = [x + y for x, y in zip(vec, vec2)]
  return Vector(result)

