t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
e=()
print(t1[0:5])
print(t1[5:])
for i in t1 :
    if i % 2 == 0:
        e = e + (i,)
t2=(11,13,15) 
print('even numbers in t1 are  :' , e )
print("Concatenate a tuple t2=(11,13,15) with t1 : ", t1+t2)
print("max value =  ", max(t1+t2) , "\n","min value = ", min(t1+t2))
    
