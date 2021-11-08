"""Save memory
with generators
"""

# inappropriate code ✗
my_list = [n**3 for n in range(10000)]
print(sum(my_list))

# appropriate code ✓
my_generator = (n**3 for n in range(10000))
print(sum(my_generator))
