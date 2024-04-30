arr =list(map(int,input().split()))
rot=int(input())
    for i in range(1,rot+1):
        last=arr[len(arr)-1]
        for j in range(len(arr)-1,0):
            arr[j]=arr[j-1]
    arr[0]=last
print(arr)