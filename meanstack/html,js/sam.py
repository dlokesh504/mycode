k=list(map(int,input().split('+')))
k.sort()
if len(k)==1:
	print(k[0])
else:
	l=''	
	for i in k:
		if len(l)==0:
			l=str(i)
		else:
			l=l+'+'+str(i)
	print(l)		
