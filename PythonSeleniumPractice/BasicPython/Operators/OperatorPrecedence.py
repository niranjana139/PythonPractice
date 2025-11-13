# Example values
a = 20
b = 10
c = 5
d = 2

# Operator Precedence Example
# * and / have higher precedence than + and -
result1 = a + b * c        # 20 + (10 * 5) = 70
result2 = (a + b) * c      # (20 + 10) * 5 = 150
result3 = a + b / c        # 20 + (10 / 5) = 22.0

# Exponentiation and Associativity (right to left)
result4 = 2 ** 3 ** 2      # 2 ** (3 ** 2) = 2 ** 9 = 512

# Left to Right associativity of -, +, *, /
result5 = 100 - 50 + 25    # (100 - 50) + 25 = 75
result6 = 100 / 10 * 5     # (100 / 10) * 5 = 50.0

# Mixing comparison and logical operators
result7 = a > b and b > c  # True and True = True
result8 = a < b or c < d   # False or False = False

# Printing results
print("a + b * c =", result1)
print("(a + b) * c =", result2)
print("a + b / c =", result3)
print("2 ** 3 ** 2 =", result4)
print("100 - 50 + 25 =", result5)
print("100 / 10 * 5 =", result6)
print("a > b and b > c =", result7)
print("a < b or c < d =", result8)
