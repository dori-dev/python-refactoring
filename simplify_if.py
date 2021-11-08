"""Simplify if-statement for multiples checks
with if x in [a,b,c]"""

color = "red"
if color == "red" or color == "blue" or color == "green":
    print("its main color!")

main_colors = ["red", "blue", "green"]
if color in main_colors:
    print("its main color!")
