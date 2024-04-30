def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))

n=int(input())
r=fact(n)
r=str(r)
c=0
b=[]
for i in range(len(r)):
   if r[i]=='0':
       c+=1
   else:
       c=0
   b.append(c)
print(max(b))