li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
if min(li1)<=min(li2) and max(li1)>=max(li2):
    print("True")
else:
    print("False")