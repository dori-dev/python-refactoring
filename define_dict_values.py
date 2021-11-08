"""Define default values in dictionaries
with .get() and .setdefault()
"""


my_dict = {
    "item": "footbal",
    "price": 10
}
# inappropriate code ✗
# count = my_dict["count"]  # KeyError: 'count'
# print(count)

# appropriate code ✓
# 1)
count = my_dict.get("count", 1)
print(count)

# 2)
count = my_dict.setdefault("count", 1)
print(count)
print(my_dict)
