txt=str(input())

upper,lower=0,0
for i in range(len(txt)):
    if txt[i].isupper():
        upper+=1
    elif txt[i].islower():
        lower+=1

if upper>lower: print (txt.upper())
else: print(txt.lower())