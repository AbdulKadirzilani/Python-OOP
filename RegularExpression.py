import re

pattern = r"color"

#match function just check the beginnning part of string

if re.match(pattern,"the color is grenn"):
    print("match")
else:
    print("Not Match")