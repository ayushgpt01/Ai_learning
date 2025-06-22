from typing import Iterator
from Vectors import Number, Vector

# Matrix is how we represent the data
# 
# Transformation is a function that when applied on a vector returns another vector
# after moving it in space.

class Matrix:
    def __init__(self, columns: list[Vector] | tuple[int, int]) -> None:
        if isinstance(columns, tuple):
            rows, cols = columns
            if rows < 1 or cols < 1:
                raise ValueError("Matrix dimensions must be positive numbers")
            self.value = [Vector([0.0] * rows) for _ in range(cols)]
            self._rows = rows
            self._cols = cols
        else:
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
    
    def __len__(self)-> int:
        return self.rows
    
    # addition
    def __add__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result: list[Vector] = []
        for c_idx in range(self.cols):
            addedValue = self.value[c_idx] + other.value[c_idx]
            result.append(addedValue)
            
        return Matrix(result)
    
    # subtraction
    def __sub__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result: list[Vector] = []
        for c_idx in range(self.cols):
            value = self.value[c_idx] - other.value[c_idx]
            result.append(value)
        return Matrix(result)
    
    # Vector or matrix multiplication
    def __mul__(self, other: "Matrix | Vector") -> "Matrix | Vector":
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    f"Matrix dimensions incompatible for multiplication: "
                    f"({self.rows}x{self.cols}) * ({other.rows}x{other.cols})"
                )
                
            result_columns: list[Vector] = []
            for col_vector in other.value:
                vec_col_list: list[Number] = []
                
                for row_vector in self:
                    vec_col_list.append(row_vector * col_vector)
                    
                result_columns.append(Vector(vec_col_list))
            return Matrix(result_columns)

        if self.cols != other.dimension:
            raise ValueError(
                f"Matrix and Vector dimensions incompatible for multiplication: "
                f"Matrix cols ({self.cols}) != Vector dimension ({other.dimension})"
            )
            
        result: list[Number] = []        
        for row_vector in self:
            result.append(row_vector * other)
            
        return Vector(result)

    
    # Scalar multiplication or scaling transformation
    def __rmul__(self, other: Number) -> "Matrix":
        return Matrix([other * col for col in self.value ])
    
    # Scalar division
    def __truediv__(self, scalar: Number) -> "Matrix":
        return Matrix([ col / scalar for col in self.value ])
    
    # Equality
    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Matrix) and 
            self.rows == other.rows and 
            self.cols == other.cols and 
            self.value == other.value
        )

    
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
    
    def is_square(self) -> bool:
        return self.rows == self.cols

    def copy(self) -> "Matrix":
        return Matrix([Vector(col.items[:]) for col in self.value])

    
    def __getitem__(self, index: tuple[int, int]) -> Number:
        rowIdx, colIdx = index
        if rowIdx < 0 or rowIdx >= self.rows or colIdx < 0 or colIdx >= self.cols:
            raise IndexError("Index out of bounds for the matrix")
        return self.value[colIdx].items[rowIdx]
    
    def __setitem__(self, index: tuple[int, int], value: Number) -> None:
        rowIdx, colIdx = index
        if rowIdx < 0 or rowIdx >= self.rows or colIdx < 0 or colIdx >= self.cols:
            raise IndexError("Index out of bounds for the matrix")
        self.value[colIdx].items[rowIdx] = value
    
    def transpose(self) -> "Matrix":
        # Swapped cols and rows for transpose
        result: Matrix = Matrix((self.cols, self.rows))
        for r_idx in range(self.rows):
            for c_idx in range(self.cols):
                result[c_idx, r_idx] = self[r_idx, c_idx]
        return result
    
    def rows_iter(self) -> Iterator['Vector']:
        """
        Yields each row of the matrix as a Vector object.
        """
        for r_idx in range(self.rows): # Iterate through each row index
            current_row_items: list[Number] = []
            for c_idx in range(self.cols): # For each row, iterate through columns to build the row Vector
                current_row_items.append(self[r_idx, c_idx])
            yield Vector(current_row_items) # Yield a new Vector object for the current row

    # Make the Matrix object itself iterable, yielding its rows
    def __iter__(self) -> Iterator['Vector']:
        """
        Allows iteration directly over the Matrix object to get its rows.
        Example: for row_vector in my_matrix: ...
        """
        return self.rows_iter()
    
    # Determinant
    def det(self) -> Number:
        
        raise NotImplementedError("Determinant calculation not yet implemented.")
    
    def inverse(self) -> "Matrix":
        # For now, don't consider non-square matrices as they require full rank
        # and other edge cases to be handled
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to have an inverse")
        raise NotImplementedError("Inverse calculation not yet implemented.")

# Addition
A = Matrix([Vector([1, 2]), Vector([3, 4])])
B = Matrix([Vector([5, 6]), Vector([7, 8])])
assert A + B == Matrix([Vector([6, 8]), Vector([10, 12])])

# Transpose
assert A.transpose() == Matrix([Vector([1, 3]), Vector([2, 4])])

# Identity
I = Matrix.identity(2)
assert I * Vector([3, 4]) == Vector([3, 4])
