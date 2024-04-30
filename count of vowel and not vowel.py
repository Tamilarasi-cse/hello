n=input()
m=n.split()
v1=0
nv1=0
fl=1
vo=['a','e','i','o','u']
for i in vo:
    for j in m:
        if j in vo:
            v1+=1


print("vowel word count:",v1)
print("No vowel word count:",c)