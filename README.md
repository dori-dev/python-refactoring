# Python Refactoring

Refactoring Python Applications for Simplicity

### You can open and read project files or use this summary 👇

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

#

## Format Strings

```python
name = "Mohammad"
my_string = f"Hello {name}"
```

#

## Generators

```python
my_generator = (n**3 for n in range(10000))
sum_numbers = sum(my_generator))
```

#

## List Comprehension

```python
squares = [n * n for n in range(10)]

```

#

## Merge Dictionaries

```python
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
```

#

## Unique Values

```python
my_list = [1, 3, 7, 7, 8, 5, 3, 2, 9, 7, 3]
unique_values = set(my_list)
```
