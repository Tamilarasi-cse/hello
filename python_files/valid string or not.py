str=input()
c=0
# for ele in str:
#     if (ele.isalpha()) or (ele.isnumeric()) or (ele==" "):
#         continue
#     else:
#         c+=1
# print(c)

for ele in str:
    if (ele>='a' and ele<='z') or (ele>='A' and ele<='Z') or (ele>='1' and ele<='9') or (ele==" "):
        continue
    else:
        c+=1
print(c)