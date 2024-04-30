n=int(input())
x=((n*2+1)//2)-1
print(x)
for i in range(0,(n*2)+1):
    if i==0 or i==(n*2):
        print("*")
    elif (i>n):
        print("*",((10**x//9)**2),"*")
        x-=1
    else:
        print("*",((10**i//9)**2),"*")