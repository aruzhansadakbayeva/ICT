from math import sqrt

GRAVITY = 9.8  

height  = float(input("Height from which object is dropped (in meters): "))

velocity = sqrt(2 * GRAVITY * height)

print("Object will hit the ground at %.2f m/s." % velocity)
