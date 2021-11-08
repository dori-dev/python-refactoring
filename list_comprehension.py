"""Use list comprehension
instead of raw for loops
"""

# inappropriate code ✗
squares = []
for n in range(10):
    squares.append(n * n)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# appropriate code ✓
squares = [n * n for n in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
