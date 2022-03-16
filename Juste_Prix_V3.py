import random



Bienvenue = print("Bienvenue au Juste prix, Veuillez choisir votre mode de difficulté \n1 = Facile, dans ce mode vous devez trouver un nombre entre 1 et 100 et vous avez un nombre illimité d'essai \n2 = Normal, comme dans le premier mode, sauf que vous avez seulement 10 essais \n3 = personnalisé, dans ce mode, vous pouvez choisir le prix maximal à deviner et aussi le nombre d'essais pour trouver le Juste Prix (si vous sélectionnez '0', vous avez un nombre illimité d'essais")


try:
	Choice_Level = int(input("Choisir un niveau, 1 à 3 : "))
		

except ValueError:
		print("Il faut choisir le niveau en nombre entier")		


else:
	Juste_Prix = random.randint(1,100)

	# ----------------  Niveau 1 ------------------
	if Choice_Level == 1:

		try:
			Prix_Jouer = int(input("Allez-y mettez votre premier prix: "))

		except ValueError:
			print("Il faut choisir un nombre entre 1 et 100")


		else:
			while True:
				if Prix_Jouer > Juste_Prix:
					Prix_Jouer = int(input("Plus petit: "))
			
				elif Prix_Jouer < Juste_Prix:
					Prix_Jouer = int(input("Plus grand: "))
			
				elif Prix_Jouer == Juste_Prix:
					print("Vous avez gagné, le Juste prix etais:", Juste_Prix)
					exit()





	# ----------------  Niveau 2 ------------------
	elif Choice_Level == 2:
		
		try:
			Prix_Jouer = int(input("Allez-y mettez votre premier prix: "))

		except ValueError:
			print("Il faut choisir un nombre entre 1 et 100")

		else:
			i = 10
			while True:
				if i == 1:
					print("Vous avez perdu, le juste prix etait:", Juste_Prix)
					exit()		
		
				elif Prix_Jouer > Juste_Prix:
					i-= 1
					print("Il vous reste", i, "essaie")
					Prix_Jouer = int(input("Plus petit: "))
					
			
				elif Prix_Jouer < Juste_Prix:
					i-= 1
					print("Il vous reste", i, "essaie")
					Prix_Jouer = int(input("Plus grand: "))
			
				elif Prix_Jouer == Juste_Prix:
					i2 = 10 - i
					print("Vous avez gagné. En total de", i2, "essaie, et le juste prix etait:", Juste_Prix)
					exit()





	# ----------------  Niveau 3 ------------------
	elif Choice_Level == 3:
		while True:
	
			Prix_Max = int(input("Veuillez choisir un prix maximal a deviner :"))
			Nombre_essai = int(input("Veuillez choisir le nombre d'essais maximal pour deviner le prix (0 pour avoir un nombre illimité d'essais) :"))
	
			Juste_Prix2 = random.randint(1,Prix_Max)
			i2 = Nombre_essai
	
			if Nombre_essai == 0:
	
				try:
					Prix_Jouer = int(input("Allez-y mettez votre premier prix: "))
	
				except ValueError:
					print("Il faut choisir un nombre entre 1 et", Prix_Max)
		
		
				else:
					while True:
						if Prix_Jouer > Juste_Prix2:
							Prix_Jouer = int(input("Plus petit: "))
					
						elif Prix_Jouer < Juste_Prix2:
							Prix_Jouer = int(input("Plus grand: "))
					
						elif Prix_Jouer == Juste_Prix2:
							print("Vous avez gagné, le Juste prix etais:", Juste_Prix2)
							exit()
	
	
	
	
	
	
			# ---------- nombre d'essais limité --------------
				
			else:
				try:
					Prix_Jouer = int(input("Allez-y mettez votre premier prix: "))
		
				except ValueError:
					print("Il faut choisir un nombre entre 1 et", Prix_Max)
		
		
				else:
					while True:
						if i2 == 1:
							print("Vous avez perdu, le juste prix etait:", Juste_Prix2)
							exit()		
				
						elif Prix_Jouer > Juste_Prix2:
							i2-= 1
							print("Il vous reste", i2, "essaie")
							Prix_Jouer = int(input("Plus petit: "))
							
					
						elif Prix_Jouer < Juste_Prix2:
							i2-= 1
							print("Il vous reste", i2, "essaie")
							Prix_Jouer = int(input("Plus grand: "))
					
						elif Prix_Jouer == Juste_Prix2:
							i3 = i2 - 10
							print("Vous avez gagné. En total de", i3, "essaie, et le juste prix etait:", Juste_Prix2)
							exit()







