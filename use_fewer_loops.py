"""Do not use too many loops
"""

found = False
conditions = [False, False, False, True, False, True, True]
for condition in conditions:
    if condition:
        fount = True
        break
