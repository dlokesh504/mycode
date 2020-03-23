l=[(1,4),(45,54),(58,77),(77,99),(10,12)]
for a,b in l:
    print(a)
    print(b)
l1=["loki","venu","navneeth","saqi"]
l2=[10,11,12,13]
s=zip(l1,l2)
print(list(s))
for a,b in s:
    print('{}      ---{}'.format(a,b))
