"""Save memory
with generators
"""
import sys

# inappropriate code ✗
my_list = [n**3 for n in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")  # 87616

# appropriate code ✓
my_generator = (n**3 for n in range(10000))
print(sum(my_generator))
print(sys.getsizeof(my_generator), "bytes")  # 112
