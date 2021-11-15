"""Concatenate string
with .join()"""

# inappropriate code ✗
list_of_string = ["Hi", "Mohammad", "Dori"]
my_string = ""
for word in list_of_string:
    my_string += word + " "
print(my_string)

# appropriate code ✓
list_of_string = ["Hi", "Mohammad", "Dori"]
my_string = " ".join(list_of_string)
print(my_string)

names = ["Mohammad", "Salar", "Ali"]
my_string = " and ".join(names)
print(f"Hello {my_string}")
