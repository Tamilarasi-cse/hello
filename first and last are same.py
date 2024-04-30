st=list(map(str,input().split()))
c=0
for word in st:
    if len(word) >= 2 and word[0] == word[-1]:
        c+=1
print(c)