pos=-1
def search(arr,ele):
    for i in range(len(arr)-1):
        if arr[i]==ele:
            globals()['pos']=i
            return True
    return False
arr=list(map(int,input().split( )))
ele=int(input())
if search(arr,ele):
    print("FOUND AT ",pos+1)
else:
    print("NOT FOUND")