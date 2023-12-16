i = input("enter  ").split()
for x in i :
    print(int(x)**3)

# or 

e = [int(x)**3 for x in i]
print(e)
