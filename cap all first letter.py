n =input()
res=""
ca_next=True
for char in n:
    if char.isalpha():
        if ca_next:
            res+=char.upper()
            ca_next=False
        else:
            res+=char.lower()
    else:
        res+=char
        ca_next=True
print(res)