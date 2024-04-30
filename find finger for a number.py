n=int(input())
finger={0:'Thumb',1:'Index',2:'Middle',3:'Ring',4:'Pinky'}
if n>0:
    print(finger[(n-1)%4])