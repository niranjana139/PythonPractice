# Example values (operands)
a = 10
b = 3
c = 5

print("Arithmetic Operators:")
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor division
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")
print("(a > b) and (c < b):", (a > b) and (c < b))
print("(a > b) or (c < b):", (a > b) or (c < b))
print("not(a > b):", not (a > b))

print("\nAssignment Operators:")
d = a  # = operator
print("d = a:", d)
d += 2  # d = d + 2
print("d += 2:", d)
d *= 3  # d = d * 3
print("d *= 3:", d)

print("\nBitwise Operators:")
print("a & b =", a & b)    # Bitwise AND
print("a | b =", a | b)    # Bitwise OR
print("a ^ b =", a ^ b)    # Bitwise XOR
print("~a =", ~a)          # Bitwise NOT
print("a << 1 =", a << 1)  # Left Shift
print("a >> 1 =", a >> 1)  # Right Shift

print("\nMembership Operators:")
name = "Python2"
print("'P' in name:", 'P' in name)
print("'z' not in name:", 'z' not in name)

print("\nIdentity Operators:")
x = 100
y = 100
print("x is y:", x is y)
print("x is not y:", x is not y)
