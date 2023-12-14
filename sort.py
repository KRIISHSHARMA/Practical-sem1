str1= input("Enter characters  :  ")

# Function to return the word
def pv(digit):
	if digit == '0':
		print("Zero ", end = " ")


	elif digit == '1':
		print("One ", end = " ")

	
	elif digit == '2':
		print("Two ", end = " ")

	
	elif digit=='3':
		print("Three",end=" ")

	
	elif digit == '4':
		print("Four ", end = " ")

	
	elif digit == '5':
		print("Five ", end = " ")


	elif digit == '6':
		print("Six ", end = " ")


	elif digit == '7':
		print("Seven", end = " ")

	
	elif digit == '8':
		print("Eight", end = " ")

	
	elif digit == '9':
		print("Nine ", end = " ")

# Function to iterate through every digit to num
def pw(N):
	i = 0
	length = len(N)

	
	while i < length:
		
		
		pv(N[i])
		i += 1


if str1.isalpha() :
    print("characters are alphabets")
    if str1.isupper():
        print("UPPERCASE")
    else:
        print("lowercase")    
if str1.isdigit() :
    print("characters are digits ")
    pw(str1)
else:
    print("characters are special")
    
    