from math import radians, acos, cos, sin, asin, sqrt
t1 = float(input())
g1 = float(input())
t2 = float(input())
g2 = float(input())
distance  = float
distance = (6371.01 * acos(sin(t1) * sin(t2) * cos(t1) * cos(t2) * cos(g1-g2)))
print (distance)