import math

arr=list(map(int,input().split()))
count=0
sum=0
for num in arr:
    if num>1:
        flag= True
        for i in range(2,int(math.sqrt(num))+1):
            print(i)
            if num%i==0:
                flag= False
                break
        if flag ==True:
            count+=1
            sum+=num
print(count)
print(sum)