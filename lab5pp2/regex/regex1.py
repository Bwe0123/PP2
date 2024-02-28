import re
x=input()
r = re.search("ab", x)
if r:
    print("Yes we have elements")
else:
    print("None")