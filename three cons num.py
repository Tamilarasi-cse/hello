li=list(map(int,input().split()))
for i in range(len(li)-2):
    if li[i]==li[i+1] and li[i]==li[i+2]:
        print(li[i])