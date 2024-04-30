org=list(map(int,input().split()))
li=org
dup=sorted(org)
ind=1
par=[]
while len(li)>0:
    if sorted(li[:ind])==dup[:ind]:
        par.append(dup[:ind])
        li=li[ind:]
        dup=dup[ind:]
        ind=1
    else:
        ind+=1
print(par)
print(len(par))
