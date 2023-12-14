
str1=str(input("enter string 1 to replace : "))
str2=str(input("enter string 2 to replace : "))
num=int(input("enter number a words to replace : "))
a = str1[0:num]
b = str2[0:num]
str1=str1.replace(a,b)
str2=str2.replace(b,a)
print("string 1 " ,  str1)
print("string 2 " ,  str2)