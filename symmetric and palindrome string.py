str1=list(input())
s=str1[0]
n=len(str1)//2
if str1[:n]==str1[n:] and str1[::1]==str1[::-1]:
    print("String is symmetrical")
    print("String is palindrome")
elif str1[:n]==str1[n:]:
    print("String is symmetrical")
elif str1[::1]==str1[::-1]:
    print("String is palindrome")