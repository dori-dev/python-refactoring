"""Do not use too many loops
"""

# inappropriate code ✗
found = False
conditions = [False, False, False, True, False, True, True]
for condition in conditions:
    if condition:
        fount = True
        break

# appropriate code ✓
conditions = [False, False, False, True, False, True, True]
found = any(conditions)
