# Euler 009
# a + b + c = 1000
# a^2 + b^2 = c^2
isFound = False
for a in range(1,999):
    if isFound == True:
        break
    for b in range(998,0,-1):
        c = 1000 - a - b
        if c**2 == b**2 + a**2:
            print a*b*c
            isFound = True
            break