from Vectors import Vector, Number

# Matrix is how we represent the data
# 
# Transformation is a function that when applied on a vector returns another vector
# after moving it in space.
# 
# Linear transformation is when metrix is transformed linearly, i.e, after
# transformation the lines of the plane remain evenly spaced and origin remains same
# 
# Mathematically - For a transform L, 
# L(x) = A(x) where A = [[1,2], [3,4]]
# 
# L(V + W) = L(V) + L(W)    -- Additivity, 
# L(cV) = cL(V)             -- Scalibility

def linear_fx(vec: Vector):
    print(f"Input vector: {vec}")

    # Represent the transformation matrix A as a list of row vectors
    # A = [[1, 2],
    #      [3, 4]]
    # So, a[0] is the first row [1, 2]
    # And a[1] is the second row [3, 4]
    a: list[Vector] = [Vector([1, 2]), Vector([3, 4])]

    # Check for dimension compatibility:
    # The number of columns in the matrix (dimension of each row vector in 'a')
    # must be equal to the dimension of the input vector.
    if vec.dimension != a[0].dimension:
        raise ValueError("Vector dimension does not match transformation matrix columns.")
    if not all(row.dimension == a[0].dimension for row in a):
         raise ValueError("Rows in the transformation matrix have inconsistent dimensions.")

    result_items: list[Number] = []

    # Iterate through each row of the transformation matrix 'a'
    for row_vector in a:
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
