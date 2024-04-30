test_list=["geeksforgeeks is best for geeks"]
char_list=['e','b','g','f']
s=test_list[0]
count={}
for i in s:
    if i in char_list:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)
sorted_dic=dict(sorted(count.items(),key=lambda a:a[1]))
print(sorted_dic)