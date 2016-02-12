#euler 014
def callatz(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    return counter
# print callatz(1)

big = callatz(13)
idx = 0
for i in xrange(1,10**6):
    temp = callatz(i)
    if temp > big:
        big = temp
        idx = i

print idx    
    
