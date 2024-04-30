def sun(n):
    re=0
    sum=0
    if n<=1:
        return n
    while n>0:
        rem=n%10
        sum+=rem
        n=n//10
    return sum


n=int(input())
c=0
li=list(map(int,input().split()))
for i in li:
    r=sun(i)
    print(r)