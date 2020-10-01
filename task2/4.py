a = int(input())
b = int(input())
c = int(input())
d = int(input())
if( (a==d and b==c) or (a==b and c==d) or (a==c and b==d) or ((a+c)%2!=0 and (b+d)%2!=0) or ((a+c)%2==0 and (b+d)%2==0) or (a==c or b==d)):
    print("Yes")
else: print ("No")