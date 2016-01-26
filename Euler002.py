# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
iniL = [1,2]
evenL = [2]
i = 2
nextNumber = 0

while nextNumber < 4000000:
    nextNumber = iniL[i-2] + iniL[i-1]
    iniL.append(nextNumber)
    if nextNumber % 2 == 0:
        evenL.append(nextNumber)
    i = i + 1
print sum(evenL)