import getpass
print("This is a game of rock paper scissor")
dict={"Rock":"1",
"Paper":"2",
"Scissor":"3"}
while(1):
	input1=getpass.getpass("Enter your choice")
	input2=getpass.getpass("Enter your choice")
	if(input1=="Exit" or input2=="Exit"):
		break
	elif(input1==input2):
		print("Tie!")
	else:
		if(dict[input1]>dict[input2]and(int(dict[input1])-int(dict[input2]) in [1,-1])):
			print("Player one wins")
		else:
			print("Player two wins")

