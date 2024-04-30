st=input()
len_z=0
len_o=0
for letter in st:
    if letter =='o':
        len_o+=1
    elif letter == 'z':
        len_z+=1
    else:
        break
if len_o==2*len_z:
    print(True)
else:
    print(False)