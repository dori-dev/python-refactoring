"""use list comprehension
instead of raw for loops
"""

squares = []

for n in range(10):
    squares.append(n * n)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [n * n for n in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
