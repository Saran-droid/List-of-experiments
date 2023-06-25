str1 = input("Enter a string:")
str2 = input("Enter a string :")
flag =1
for i in str2:
    if i in str1.upper() or i in str1.lower():
         pass
    else :
        flag =0
if flag:
    print( str2,"is a substring of ",str1)
else:
    print(str2, "is not a substring of ", str1)