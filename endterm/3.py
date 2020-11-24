year=int(input())
a=int
b=int
c=int
d=int

while(year<1000 and year>9000):
  
    year=year+1
    a=year/1000
    b=year/100%10
    c=year/10%10
    d=year%10
    if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        break
    

print(year)