arr = list(map(int, input().split()))
k = int(input())
c = 0
for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr) ):
        if arr[i] + arr[j] == k:
            c += 1

print(c)