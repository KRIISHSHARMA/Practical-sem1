import math
def pa(n):
    for i in range(2,n):
        if (n%i)==0 :
           return False
           break
   
    return(True)
        

def pab(n):
         
         for i in range(1,n+1):
            if(pa(i)):
                print(i) 
                
def nprime(n):
    i = 2
    while n != 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            n -= 1
        i += 1
input1=int(input("enter number :  "))
if pa(input1):
    print(input1 , "is a prime number")
else :
    print(input1 , "is not a prime number")  
pab(input1)
print("first",input1 ,"prime numbers are  ")
nprime(input1)