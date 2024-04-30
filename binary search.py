pos=-1
def search(arr,ele):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==ele:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid]<ele:
                l=mid+1
            else:
                u=mid-1

    return False
arr=list(map(int,input().split( )))
ele=int(input())
if search(arr,ele):
    print("FOUND AT ",pos+1)
else:
    print("NOT FOUND")