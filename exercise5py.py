bdictionary={"Neha J":"29/01/1960",
"Anil J":"12/08/1957",
"Anuja J":"24/11/1986",
"Agraja J":"26/12/1994"}
print("Welcome to the birthday dictionary. We know the birthdays of\nNeha J\nAnil J\nAnuja J\nAgraja J")
name="Nila"
while(name!="Exit"):
	name=input("Whose birthday do you want to look up?")
	if(name!="Exit"):
		print("%s's birthday is on %s"%(name,bdictionary[name]))
	else:
		break
