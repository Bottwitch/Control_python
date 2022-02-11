import random



with open("mots.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split()))
    motChoice = random.choice(words)  
      
print("Bienvenue au jeu du pendu, vous devez trouver le mot avant que le dessin du pendu soit completé\n") 
print(motChoice)

SizeWord = len(motChoice)

for x in range(SizeWord):
    print("_", end=" " )

tiret = "-"
tiret = "-","-","-","-","-"

while True:
    ChoiceLetter = input("\n \nVeillez entrer une lettre: ")


    if ChoiceLetter.upper() in motChoice:
        for x in range(SizeWord): 
            print("_", end=" " )
            
        indexLet = motChoice.index(ChoiceLetter.upper())
            












