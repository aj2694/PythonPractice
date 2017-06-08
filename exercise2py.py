num=int(input("Enter a number"))
if(num%2==0):
	print("Number you entered is even")
	if(num%4==0):
		print("This number is also a multiple of 4")
else:
	print("Number you entered is odd")
num1=int(input("Enter a number again"))
num2=int(input("Enter a number that will divide the first number"))
if(num1%num2==0):
	print("%d is a multiple of %d"%(num1,num2))
else:
	print("%s is not a multiple of %d"%(num1,num2))

