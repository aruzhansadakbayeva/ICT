
m = input();
n = int(m);
i = 1; cnt = 0;
while i*i<=n:
	if n%i==0:
		if i==1 or i*i==n:
			cnt+=1;
		else:
			cnt+=2;
	i+=1;
print(cnt);