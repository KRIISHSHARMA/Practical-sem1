#WAP to create a pyramid of the character ‘*’ and a reverse pyramid
r = int(input("enter number of rows :  "))

for i in range(r):
    for j in range(i+1):
        print("*",end="")
    print("\n")
#inverted pyramid 
for i in range(r,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")