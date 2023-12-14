import os
y = True 
while y == True:
    f= open("/home/kriish/Desktop/vscode/hello.txt","r")
    line1=0
    words=0
    char=0
    d={}
    lt=[]
    g=f.read()
    for i in g.split():
       words+=1
       lt.append(i)
       for k in i:
           if k in d:
               d[k]+=1
           else : 
               d[k]=1
       for j in i :
            char+=1
    lt=lt[::-1]
    u=input("do you wanna see reverse of the file ?(y/n) : ")
    if u == 'y':
        print(str(lt))
    else:
        pass
    print("Total no. of words is", words)
    print("Total no. of characters is", char)
    print("Frequency of every character in the file is: ","\n" + str(d))
    k = 1
    for line in f.readlines():
        line1+=1
        if k % 2 == 0 :
            with open('/home/kriish/Desktop/vscode/even.txt',"w") as r:
                r.writeline(line)
        k+=1
    print("Total no. of lines is", line1)
    f.close()
    y = input("Do you want to run the program again? (y/n): ")
    if y == "y":
      y = True
    else:
      y = False
    
