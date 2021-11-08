"""Count hashable objects
with collections.Counter
"""
from collections import Counter

my_list = [4, 4, 4, 4, 8, 9, 7, 7, 7, 5, 5, 5, 5, 5, 5]
counter = Counter(my_list)
print(counter)
print(counter[5])
print(counter[10])

most_common = counter.most_common(2)
print(most_common)
most_common = counter.most_common(3)
print(most_common)
