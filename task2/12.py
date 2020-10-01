import math
n = int(input())

i = 1
while math.pow(2,i) <= n:
    print(math.pow(2,i))
    i += 1

