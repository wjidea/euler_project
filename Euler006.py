# Euler 006
Lsqr = map(lambda x:x**2, range(1,101))
Lsum = (reduce(lambda x,y:x+y, range(1,101)))**2
LsqrSum = reduce(lambda x,y:x+y,Lsqr)
print Lsum - LsqrSum