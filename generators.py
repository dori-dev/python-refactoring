"""Save memory
with generators
"""

my_list = [n**3 for n in range(10000)]
print(sum(my_list))

my_generator = (n**3 for n in range(10000))
print(sum(my_generator))
