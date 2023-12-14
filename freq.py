def freq(n):
    f = {}
    for i in n:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
  
    print (f)
    
def replace(n):
    a=input("enter char to replace  :")
    b=input("enter char to replace with ")
    n1=n.replace(a,b)
    print("new string = " , n1)
h= True 
while h == True :
 rem=str(input("enter string to operate with :  "))
 freq(rem)
 b=input("do you want to replace an alphabet ? , y or n :  ")
 if b == 'y' or b == 'Y':
     replace(rem)
 else:
     print("bye")
 c=input("do you want to cont. ? , y or n :  ")
 if b == 'y' or b == 'Y':
    h == True
 else:
    h==False
    break