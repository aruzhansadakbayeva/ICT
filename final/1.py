t=int(input())

a = [ ]
for I in range(t) : 
      row = input().split()
      for j in range(len(row)):
            row[j] = int(row[j]);
      a.append(row)

for I in range(t):
    for j in range(len(row)):
        if row[I]%row[j]==0:
             print("YES")
             break
        else:
         print("NO")
         break


