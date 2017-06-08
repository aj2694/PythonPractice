inputstr=input("Enter a string")
a=len(inputstr)
if(inputstr[0:a-1:1]==inputstr[a-1:0:-1]):
	print("Palindrome")
else:
	print("Not a palindrome")
