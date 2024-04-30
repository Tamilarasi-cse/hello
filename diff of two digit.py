n=int(input())
rem=0
if n>10:
    for i in range(10, n):
        dif = 0
        temp = i
        while i > 0:
            rem = i % 10
            dif = abs(dif - rem)
            i = i // 10
        if dif == 1:
            print(temp)
else:
    print(-1)