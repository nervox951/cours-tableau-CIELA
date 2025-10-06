import random

def juste_prix():
    prix = random.randint(1, 100)
    essais = 0
    print("Bienvenue au jeu du Juste Prix !")
    print("Devinez le prix (entre 1 et 100) :")

    while True:
        try:
            proposition = int(input("Votre proposition : "))
            essais += 1
            if proposition < prix:
                print("C'est plus !")
            elif proposition > prix:
                print("C'est moins !")
            else:
                print(f"Bravo ! Le juste prix était {prix}. Vous avez trouvé en {essais} essais.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    juste_prix()