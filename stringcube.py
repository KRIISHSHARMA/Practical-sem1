import math as m
l = []

while True:
    f = input("Enter an element (to stop, write 'done'): ")
    t = input("Continue? (yes or no): ")
    
    if t.lower() != 'no':
        l.append(f)  
    else:
        break

print("Original list:", l)

l1 = []

for i in l:
    if (int(i) % 2) == 0:
        l1.append(int(i)**3)  # Calculate the cube of the even number

print("Cubes of even numbers:", l1)
