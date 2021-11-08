"""Sort complex iterables
with build-in sorted() method
"""

# simple use sorted
data = [3, 5, 1, 10, 9]
sorted_data = sorted(data)
print(sorted_data)

# use revers parameter
data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

# use key parameter
data = [
    {
        "name": "ali",
        "age": 20,
    },
    {
        "name": "mohammad",
        "age": 17,
    },
    {
        "name": "sina",
        "age": 50
    }
]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
