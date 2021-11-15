"""Format Strings(python 3.6+)
with f-Strings"""

# inappropriate code ✗
name = "Mohammad"
my_string = "Hello " + name
print(my_string)
for number in range(10):
    print(number, "squared is", number ** 2)

# appropriate code ✓
name = "Mohammad"
my_string = f"Hello {name}"
print(my_string)
for number in range(10):
    print(f"{number} squared is {number**2}")
