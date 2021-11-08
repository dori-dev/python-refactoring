"""Merge Dictionaries (python 3.5+)
with {**d1, **d2}"""

d1 = {
    "name": "Mohammad Dori",
    "age": 25
}

d2 = {
    "name": "Mohammad Dori",
    "city": "Tehran",
    "job": "Developer"
}

merged_dict = {**d1, **d2}
print(merged_dict)
