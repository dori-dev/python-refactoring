"""Do not repeat and
Avoid duplicate codes"""

NUMBER = 100

# inappropriate code ✗
if NUMBER < 50:
    result = NUMBER ** 3
    result = f"Result: {result}"
else:
    result = NUMBER ** 2
    result = f"Result: {result}"

# appropriate code ✓
if NUMBER < 50:
    result = NUMBER ** 3
else:
    result = NUMBER ** 2
label = f"Result: {result}"
