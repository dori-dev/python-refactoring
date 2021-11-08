"""Count any objects
with collections.Counter
"""
from collections import Counter

# A good way to count values in any objects
my_list = [4, 4, 4, 4, 8, 9, 7, 7, 7, 5, 5, 5, 5, 5, 5]
counter = Counter(my_list)
print(counter)
print(counter[5])
print(counter[10])
# Get most of the values used in the object
most_common = counter.most_common(2)
print(most_common)
most_common = counter.most_common(3)
print(most_common)
