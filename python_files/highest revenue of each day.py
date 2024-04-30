def great(arr):
    max=0
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i]
    return max

n,m=map(int,input().split())
li=list(map(int,input().split()))
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
r=great(li)
l=great(li1)
k=great(li2)
print(r,l,k)