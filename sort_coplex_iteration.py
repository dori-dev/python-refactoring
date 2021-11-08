"""Sort complex iterables
with build-in sorted() method
"""

data = [3, 5, 1, 10, 9]
sorted_data = sorted(data)
print(sorted_data)

data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data = [
    {
        "name": "mohammad",
        "family": "dori",
        "age": 17,
    },
    {
        "name": "ali",
        "family": "dori",
        "age": 20,
    }
]
