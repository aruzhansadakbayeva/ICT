print("Input your height: ")
infeet = int(input("Feet: "))
ininch = int(input("Inches: "))

ininch += infeet * 12
incm= round(ininch * 2.54, 1)

print("Your height is : %d cm. " % incm)