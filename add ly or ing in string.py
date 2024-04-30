st=input()
if len(st)>=3:
    if st[-3:] =="ing":
        print(st+'ly')
    else:
        print(st+'ing')
else:
    print(st)

