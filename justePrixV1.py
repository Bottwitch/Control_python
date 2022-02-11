import random


JustePrix = random.randint(1,100)


Bienvenue = print("Bonjour, Bienvenue au Juste prix, Vous devez trouver le juste prix entre 1 et 100.")


try:
	PrixJouer = int(input("Allez-y mettez votre premier prix: "))
		

except ValueError:
		print("Il faut mettre un chiffre entre 1 et 100: ")
		

else:
	while True:
		if PrixJouer > JustePrix:
			PrixJouer = int(input("Plus petit: "))
	
		elif PrixJouer < JustePrix:
			PrixJouer = int(input("Plus grand: "))
	
		elif PrixJouer == JustePrix:
			print("Vous avez gagné, le Juste prix etais:", JustePrix)
			exit()

	
		







