a = int(input())
b = int(input())
c = int(input())
d = int(input())
if(c==a+1 or d==b+1 or c==b+1 or a==c+1 or b==d+1 or (a==c and b==d)):
    print("Yes")
else: print ("No")