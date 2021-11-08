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
# 1) return value of `count` key if available and else return `1`
count = my_dict.get("count", 1)
print(count)

# 2) return value of `count` key if available and else return `1`
# and add `count` key with `1` value
count = my_dict.setdefault("count", 1)
print(count)
print(my_dict)
