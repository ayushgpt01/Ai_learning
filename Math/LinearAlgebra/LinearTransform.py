
from Vectors import Number, Vector
from Matrix import Matrix

# Linear transformation is when metrix is transformed linearly, i.e, after
# transformation the lines of the plane remain evenly spaced and origin remains same
# 
# Mathematically - For a transform L, 
# L(x) = A(x) where A = [[1,2], [3,4]]
# 
# L(V + W) = L(V) + L(W)    -- Additivity, 
# L(cV) = cL(V)             -- Scalibility

def linear_fx(vec: Vector):
    # Represent the transformation matrix A as a list of row vectors
    # A = [[1, 2],
    #      [3, 4]]
    # So, a[0] is the first row [1, 2]
    # And a[1] is the second row [3, 4]
    a: Matrix = Matrix([Vector([1, 2]), Vector([3, 4])])

    # Check for dimension compatibility:
    # The number of columns in the matrix (dimension of each row vector in 'a')
    # must be equal to the dimension of the input vector.
    if vec.dimension != a.rows:
        raise ValueError("Vector dimension does not match transformation matrix columns.")

    result_items: list[Number] = []
    print(a)
    # Iterate through each row of the transformation matrix 'a'
    for row_vector in a:
        print(row_vector)
        result_items.append(row_vector * vec)

    result = Vector(result_items)
    print(f"Output {result}")
    return result

v = Vector([1, 2])
w = Vector([2, -1])
c = 3

# Additive
s = v + w
additiveLhs = linear_fx(s)
additiveRhs = linear_fx(v) + linear_fx(w)
additive = additiveLhs == additiveRhs
print(f"lhs = {additiveLhs} rhs = {additiveRhs} additive? {additive}")

# Scalable
scalabilityLhs = linear_fx(c * v)
scalabilityRhs = c * linear_fx(v)
scalable = scalabilityLhs == scalabilityRhs
print(f"lhs = {scalabilityLhs} rhs = {scalabilityRhs} scalable? {scalable}")
