t = True
while t == True :
    str1=input("enter string 1  : ")
    str2=input("enter string 2  : ")
    l=[]
    list1=list(str1)
    a=len(list1)
    for i in range(a):
        l.append(i)
    #l=str(l)
   # str2=str2+l
   # print(str2)
    for i in l:
        str2=str2 +','+ str(i)
    print(str2)