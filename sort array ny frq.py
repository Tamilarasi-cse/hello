arr=list(map(int,input().split()))
count={}
for i in range(len(arr)):
    if arr[i] in count:
        count[arr[i]]+=1
    else:
        count[arr[i]]=1
print(count)
sorted_dic=dict(sorted(count.items(),key=lambda a:a[1],reverse=True))
print(sorted_dic)
for i in sorted_dic.keys():
    for k in range(sorted_dic[i]):
        print(i,end=" ")