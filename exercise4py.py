import random
a=random.sample(range(1000),random.randint(1,100))
b=random.sample(range(1000),random.randint(1,100))
c=[]
for i in a:
	if i in b:	
		if i in c:
			continue
		else:
 			c.append(i)
print(c)
				
