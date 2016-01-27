def isPalin(x):
    xStr = str(x)
    xLen = len(xStr)
    if xLen % 2 != 0:
        return False
    for i in range(xLen/2):
        if xStr[i] != xStr[-i-1]:
            return False
    return True

big = 0
for i in range(100,1000):
    for j in range(100, 1000):
        product = i * j
        if product > big and isPalin(product):
            big = product
print big
