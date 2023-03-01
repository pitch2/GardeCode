def main():
    choix = input("Que voulez-vous faire? \n1 - Générer un nouveau mot de passe\n2 - Lire mes mots de passe\nChoix: ")
    if choix == "1":
        generer_mot_de_passe()
    elif choix == "2":
        lire_mots_de_passe()
    else:
        print("Erreur: choix invalide.")

def generer_mot_de_passe():
    site = input("Site: ")
    identifiant = input("Identifiant: ")
    mot_de_passe = input("Mots de passe: ")
    print("Le mot de passe généré est:", mot_de_passe)
    with open("mots_de_passe.txt", "a") as f:
        f.write("Site: " + site + "\nIdentifiant: " + identifiant + "\nMot de passe: " + mot_de_passe + "\n\n")

def lire_mots_de_passe():
    choix = input("Que voulez-vous faire? \n1 - Lire tous les mots de passe\n2 - Chercher un site en particulier\nChoix: ")
    if choix == "1":
        with open("mots_de_passe.txt", "r") as f:
            print(f.read())
    elif choix == "2":
        site = input("Site à chercher: ")
        resultats = chercher_mots_de_passe(site)
        if resultats:
            for identifiant, mot_de_passe in resultats:
                print("Site:", site)
                print("Identifiant:", identifiant)
                print("Mot de passe:", mot_de_passe)
        else:
            print("Aucun résultat trouvé pour le site", site)
    else:
        print("Erreur: choix invalide.")

def chercher_mots_de_passe(site):
    resultats = []
    with open("mots_de_passe.txt", "r") as f:
        lignes = f.readlines()
    for i, ligne in enumerate(lignes):
        if ligne.startswith("Site:"):
            nom_site = ligne.strip().split(':')[1].strip()
            if nom_site == site:
                identifiant = lignes[i+1].strip().split(':')[1].strip()
                mot_de_passe = lignes[i+2].strip().split(':')[1].strip()
                resultats.append((identifiant, mot_de_passe))
    return resultats

def init():
    f = open("mots_de_passe.txt", "a")
    f.close()

main()


#Faire recherche par site, id, mdp