import math
tip = 0,18
tax = 0,6
price = float(input("enter the price: $"))
tip1 = price * tip
tax1= price * tax
total = price +tip1 + tax1
print ("\nTip:  ", format(tip1, '8,2f'))
print ("Tax:  ", format(tax1, '8,2f'))
print ("Total:  ", format(total, '8,2f'))