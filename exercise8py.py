import random
class game:
	def game(self):
		num1=random.randint(1,9)
		num2=0
		count=0
		while(num2!=num1):
			num2=int(input("Enter your guess"))
			if(num2>num1):
				print("Guess lower")
				count+=1
			else:
				print("Guess higher")
				count+=1
		else:
			print("congratulation you guessed in %d guesses"%count)
game1=game()
game1.game()
