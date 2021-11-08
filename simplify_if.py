"""Simplify if-statement for multiples checks
with if x in [a,b,c]"""

# inappropriate code ✗
color = "red"
if color == "red" or color == "blue" or color == "green":
    print("its main color!")

# appropriate code ✓
color = "red"
main_colors = ["red", "blue", "green"]
if color in main_colors:
    print("its main color!")
