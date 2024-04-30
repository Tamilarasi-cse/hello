st=list(map(str,input().split()))
long_pre=st[0]
for i in st[1:]:
    j=0
    while j<len(long_pre) and j<len(st) and long_pre[j]==i[j]:
        j+=1
    long_pre=long_pre[:j]
print(long_pre)