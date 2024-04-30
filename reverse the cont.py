st=input()
n=len(st)
a=[]
b=[]
for i in range(n-1,-1,-1):
    if st[i] in 'aeiou':
        b.append(st[i])
    else:
        b.append(" ")
    if st[i] not in 'aeiou':
        a.append(st[i])
b=b[::-1]
i=0
for j in range(len(b)):
    if b[j]==' ':
        b[j]=a[i]
        i+=1
print(''.join(b))