n=int(input())
a = [ ]
for I in range(n) : 
      row = input().split()
      for j in range(n):
            row[j] = int(row[j]);
      a.append(row)
x = 0
for I in range (len(a)):
       x += sum(a[I])


if(x==0):
    print ("YES")
else:
    print("NO")