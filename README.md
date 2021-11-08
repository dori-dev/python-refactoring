# Python Refactoring

Refactoring Python Applications for Simplicity

#

## Concatenate String

```python
my_string = " ".join(["Hi", "Mohammad", "Dori"])
```

#

## Define Values in Dictionaries

```python
my_dict = {
    "item": "footbal",
    "price": 10
}
count = my_dict.get("count", 1)
count = my_dict.setdefault("count", 1)
```

#

## Iterate with Enumerate

```python
data = [1, -5, 8, -3]
for index, number in enumerate(data):
    if number < 0:
        data[index] = 0
```
