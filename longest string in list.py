st=list(map(str,input().split()))
k=int(input())
st=sorted(st,key=len,reverse=True)
print(' '.join(st[:k]))