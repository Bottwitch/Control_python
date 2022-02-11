import random



Bienvenue = print("Bienvenue au Juste prix, Veuillez choisir votre mode de difficulté \n1 = Facile, dans ce mode vous devez trouver un nombre entre 1 et 100 et vous avez un nombre illimité d'essai \n2 = Normal, comme dans le premier mode, sauf que vous avez seulement 10 essais \n3 = personnalisé, dans ce mode, vous pouvez choisir le prix maximal à deviner et aussi le nombre d'essais pour trouver le Juste Prix (si vous sélectionnez '0', vous avez un nombre illimité d'essais")


try:
	ChoiceLevel = int(input("Choisir un niveau, 1 à 3 : "))
		

except ValueError:
		print("Il faut choisir le niveau en nombre entier")		


else:
	JustePrix = random.randint(1,100)

	# ----------------  Niveau 1 ------------------
	if ChoiceLevel == 1:

		try:
			PrixJouer = int(input("Allez-y mettez votre premier prix: "))

		except ValueError:
			print("Il faut choisir un nombre entre 1 et 100")


		else:
			while True:
				if PrixJouer > JustePrix:
					PrixJouer = int(input("Plus petit: "))
			
				elif PrixJouer < JustePrix:
					PrixJouer = int(input("Plus grand: "))
			
				elif PrixJouer == JustePrix:
					print("Vous avez gagné, le Juste prix etais:", JustePrix)
					exit()





	# ----------------  Niveau 2 ------------------
	elif ChoiceLevel == 2:
		
		try:
			PrixJouer = int(input("Allez-y mettez votre premier prix: "))

		except ValueError:
			print("Il faut choisir un nombre entre 1 et 100")

		else:
			i = 10
			while True:
				if i == 1:
					print("Vous avez perdu, le juste prix etait:", JustePrix)
					exit()		
		
				elif PrixJouer > JustePrix:
					i-= 1
					print("Il vous reste", i, "essaie")
					PrixJouer = int(input("Plus petit: "))
					
			
				elif PrixJouer < JustePrix:
					i-= 1
					print("Il vous reste", i, "essaie")
					PrixJouer = int(input("Plus grand: "))
			
				elif PrixJouer == JustePrix:
					i2 = 10 - i
					print("Vous avez gagné. En total de", i2, "essaie, et le juste prix etait:", JustePrix)
					exit()





	# ----------------  Niveau 3 ------------------
	elif ChoiceLevel == 3:

		PrixMax = int(input("Veuillez choisir un prix maximal a deviner :"))
		NbTry = int(input("Veuillez choisir le nombre d'essais maximal pour deviner le prix (0 pour avoir un nombre illimité d'essais) :"))

		JustePrix2 = random.randint(1,PrixMax)
		i2 = NbTry

		if NbTry == 0:

			try:
				PrixJouer = int(input("Allez-y mettez votre premier prix: "))

			except ValueError:
				print("Il faut choisir un nombre entre 1 et", PrixMax)
	
	
			else:
				while True:
					if PrixJouer > JustePrix2:
						PrixJouer = int(input("Plus petit: "))
				
					elif PrixJouer < JustePrix2:
						PrixJouer = int(input("Plus grand: "))
				
					elif PrixJouer == JustePrix2:
						print("Vous avez gagné, le Juste prix etais:", JustePrix2)
						exit()






		# ---------- nombre d'essais limité --------------
			
		else:
			try:
				PrixJouer = int(input("Allez-y mettez votre premier prix: "))
	
			except ValueError:
				print("Il faut choisir un nombre entre 1 et", PrixMax)
	
	
			else:
				while True:
					if i2 == 1:
						print("Vous avez perdu, le juste prix etait:", JustePrix2)
						exit()		
			
					elif PrixJouer > JustePrix2:
						i2-= 1
						print("Il vous reste", i2, "essaie")
						PrixJouer = int(input("Plus petit: "))
						
				
					elif PrixJouer < JustePrix2:
						i2-= 1
						print("Il vous reste", i2, "essaie")
						PrixJouer = int(input("Plus grand: "))
				
					elif PrixJouer == JustePrix2:
						i3 = 10 - i2
						print("Vous avez gagné. En total de", i3, "essaie, et le juste prix etait:", JustePrix2)
						exit()







