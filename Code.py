import random
import string
def passwd(num):

    for i in range(0,num-3):
        yield random.choice(string.ascii_letters)
    for i in range(0,2):
        yield random.choice(string.digits)
    for i in range(0,1):
        yield random.choice(string.punctuation)

ans=input("Do you want a strong or a weak password")
password=""
if (ans=="Strong"):

    num=int(input("Enter the number of characters in password"))
    for char in passwd(num):
        password=password+char
    password=''.join(random.sample(password,len(password)))

    print(password)

else:
    list=["ibieb","oheo","puqw","lkkoehd","oiei"]
    count=0
    while(count<2):
        i=random.randrange(0,4)
        count+=1
        password=password+list[i]
    print(password)