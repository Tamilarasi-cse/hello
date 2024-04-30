a=[3,4,7,34,78,90]
mid=len(a)//2
for i in range(0,mid):
    for j in range(i+1,mid+1):
        if a[j]<a[i]:

            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(mid,len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)