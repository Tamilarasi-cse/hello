n=list(map(int,input().split()))
st=0
end=len(n)-1
a=[]
while st<end:
    for i in range(1, int(len(n)/2)-1):
        a.append(n[end])
        a.append(n[st])
        end -= 1
        st += 1
a.append(st+1)
for i in a:
    print(i,end=' ')
