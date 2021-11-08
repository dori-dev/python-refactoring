"""Iterate with enumerate()
instead of range(len(x))
"""


# inappropriate code ✗
data = [1, -5, 8, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)  # [1, 0, 8, 0]


# appropriate code ✓
data = [1, -5, 8, -3]
for index, number in enumerate(data):
    if number < 0:
        data[index] = 0
print(data)  # [1, 0, 8, 0]
