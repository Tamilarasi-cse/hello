li=list(map(int,input().split()))
flag=True
for i in range(len(li)):
    if i%2==0 and li[i]%2!=0:
        flag=False
    elif i%2!=0 and li[i]%2==0:
        flag=False
print(flag)