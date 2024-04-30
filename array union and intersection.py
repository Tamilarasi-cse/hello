n= int(input())
m= int(input())
l1=[]
l2=[]
#c=0
c1=0
for i in range(0,n):
   l1.append(int(input()))
for j in range(0,m):
  l2.append(int(input()))

#for x in l2:
#   if x not in l1:
#       c1+=1
#print("elements after union :",len(l1)+c1)
#for i in range(0,n):
#   for j in range(0,m):
#       if(l1[i]==l2[j]):
#           c+=1
#print("elements that intersect",c)
for x in l1:
    if x in l2:
        c1+=1
    if x not in l2:
        l2.append(l1)
print(len(l2))
print(c1)