n = int(input("enter the n value : "))
l=["True" for i in range(n+1)] # l=["True"]*n
p = 2
while p*p<=n:
    if l[p]=="True":
        for i in range(p*p,n+1,p):
            l[i]='False'
    p=p+1
for p in range(2,n+1):
    if l[p]=="True":
        print(p,end=' ')

if l[n]=="True":
    print("yes")
else:
    print("No")
