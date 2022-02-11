import random


JustePrix = random.randint(1,100)
Bienvenue = print("Bonjour, Bienvenue au Juste prix, Vous devez trouver le juste prix entre 1 et 100.")



try:
	PrixJouer = int(input("Allez-y mettez votre premier prix: "))		

except ValueError:
		print("Il faut mettre un chiffre entre 1 et 100: ")		

else:

	i = 10
	while True:
		if i == 0:
			print("Vous avez perdu, le juste prix etait: ", JustePrix)
			exit()


		elif PrixJouer > JustePrix:
			print("Il vous reste", i, "essaie")
			PrixJouer = int(input("Plus petit: "))
			i-= 1
	
		elif PrixJouer < JustePrix:
			print("Il vous reste", i, "essaie")
			PrixJouer = int(input("Plus grand: "))
			i-= 1
	
		elif PrixJouer == JustePrix:
			i2 = 10 - i
			print("Vous avez gagné. En total de", i2, "essaie, et le juste prix etait: ", JustePrix)
			exit()







