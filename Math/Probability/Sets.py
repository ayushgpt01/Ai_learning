# Mathematical Set of elements
# Set is a collection of unique elements

A = {5,3,17,12,19}
B = {17,19,6}
C = {5,3,17,12}
D = {1,2}

print(A)
print(B)
print(C)
print(D)
    
# Union - Combination of all distinct elements in both sets
print(A | B)

# Intersection - Elements that are in both sets
print(A & B)

# Difference - Elements that are in A but not in B / Relative Complement
print(A - B)

# Symmetric Difference - Elements that are in A or B but not in both
print(A ^ B)

# isSubset - True if B is a subset of A (lhs, rhs matters)
print(C < A)

# isSuperset - True if A is a superset of B (lhs, rhs matters)
print(A > C)

# isdisjoint - True if A and B have no elements in common
print(D.isdisjoint(A))