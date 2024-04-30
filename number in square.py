n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j:
            val=i-j+1
        else:
            val=j-i+1
        print(val,end=" ")
    print()