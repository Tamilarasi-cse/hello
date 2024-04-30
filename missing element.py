n=int(input())
arr=[]
for i in range(n-1):
    arr.append(int(input()))
u=set(arr)
for i in range(1,n+1):
    if i not in u:
        print(i)