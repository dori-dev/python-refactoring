"""Use less "if"
"""

CONDITION_A = True
CONDITION_B = True

# inappropriate code ✗
if CONDITION_A:
    if CONDITION_B:
        print('mohammad dori')

# appropriate code ✓
if CONDITION_A and CONDITION_B:
    print('mohammad dori')
