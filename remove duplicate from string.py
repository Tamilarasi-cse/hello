n=input()
p=""
for char in n:
    if char not in p:
        p=p+char
print(p)