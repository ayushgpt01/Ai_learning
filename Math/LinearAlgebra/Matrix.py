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

class Matrix:
    def __init__(self, columns: list[Vector]) -> None:
        if len(columns) > 0 and any(x.dimension != columns[0].dimension for x in columns):
            raise ValueError("Matrix cannot have different sized vectors")
        
        self.value = columns
        self._rows = columns[0].dimension if len(columns) > 0 else 0
        self._cols = len(columns)
        
    @property
    def rows(self):
        return self._rows
    
    @property
    def cols(self):
        return self._cols
    
    @staticmethod
    def identity(size: int):
        """
        Returns the identity matrix of size
        """
        return Matrix([Vector([1 if x == y else 0 for y in range(size)]) for x in range(size)])
    
    # addition
    def __add__(self, other: "Matrix") -> "Matrix":
        return Matrix([])
    
    # subtraction
    def __sub__(self, other: "Matrix") -> "Matrix":
        return Matrix([])
    
    # Vector or matrix multiplication
    def __mul__(self, other: "Matrix | Vector") -> "Matrix":
        return Matrix([])
    
    # Scalar multiplication
    def __rmul__(self, other: Number) -> "Matrix":
        return Matrix([])
    
    # Scalar division
    def __truediv__(self, scalar: Number) -> "Matrix":
        return Matrix([])
    
    # Equality
    def __eq__(self, other: object) -> bool:
        return False
    
    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Matrix.
        This is what you see when you print() the matrix.
        """
        if not self.cols: 
            return "Matrix([])"

        # Create a list of lists where each inner list is a row
        # This makes it easier to print row by row
        rows_data: list[list[str]] = []
        for r_idx in range(self.rows):
            current_row: list[str] = []
            for c_idx in range(self.cols):
                # Assuming Vector objects have a 'value' attribute which is a list of numbers
                current_row.append(str(self.value[c_idx].items[r_idx]))
            rows_data.append(current_row)

        # Determine the maximum width needed for each column to align them
        column_widths = [0] * self.cols
        for c_idx in range(self.cols):
            for r_idx in range(self.rows):
                column_widths[c_idx] = max(column_widths[c_idx], len(rows_data[r_idx][c_idx]))

        # Format each row
        formatted_rows: list[str] = []
        for row in rows_data:
            formatted_elements = [element.rjust(column_widths[i]) for i, element in enumerate(row)]
            formatted_rows.append(f"[{' '.join(formatted_elements)}]")

        return "\n".join(formatted_rows)
    
    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the Matrix,
        ideally allowing it to be recreated using eval().
        This is typically used for debugging.
        """
        vector_reprs = [repr(col_vec) for col_vec in self.value]
        return f"Matrix([{', '.join(vector_reprs)}])"
    
    def __getitem__(self, index: tuple[int, int]) -> Number:
        if index[0] < 0 or index[0] >= self.cols or index[1] < 0 or index[1] >= self.rows:
            raise IndexError("Index out of bounds for the matrix")
        return self.value[index[0]].items[index[1]]
    
    def __setitem__(self, index: tuple[int, int], value: Number) -> None:
        self.value[index[0]].items[index[1]] = value
    
    def transpose(self) -> "Matrix":
        return Matrix([])
    
    # Determinant
    def det(self) -> Number:
        return 0
    
    def inverse(self) -> "Matrix":
        return Matrix([])

id = Matrix.identity(3)
print(id[1, 1])
id[1, 1] = 4
print(id)


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
