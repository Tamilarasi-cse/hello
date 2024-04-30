
import math
def square(n):
    if n<=1:
        return True
    sr=int(math.sqrt(n))
    print(sr,n)
    if sr*sr==n:
        return True
    return False
    # l, r = 1, n
    # while l <= r:
    #     mid = (l + (r-l)) // 2
    #     sq = mid * mid
    #     if sq == n:
    #         return True
    #     elif sq < n:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # return False
n=int(input())
c=0
li=list(map(int,input().split()))
for i in li:
    if square(i):
        print(i)
        c+=1
print(c)