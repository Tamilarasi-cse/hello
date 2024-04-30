arr=list(map(int,input().split( )))
profit=0
max=0
minprice=arr[0]
for i in range(1, len(arr)):
    if arr[i] > minprice:
        curr = arr[i] - minprice
        if max < curr:
            max = curr
    else:
        profit = max
        minprice = arr[i]
profit+=max
print(profit)