"""
Système de gestion des employés 
Auteur : Amélie Jehanne Lanto
Description : Menu CLI pour gérer des employés stockés dans un dictionnaire.
"""


class Employé :

    def __init__(self, nom, id, département, titre):

        self.nom = nom
        self.id = id
        self.département = département
        self.titre = titre


    def afficher_informations(self):

        print("Nom:", self.nom)
        print("Numéro d'identification:", self.id)
        print("Département:", self.département)
        print("Titre du poste:", self.titre)
        print(" ")



def ajouter_employé(dictionary):

    nom = input("Nom de l'employé: ")
    id = int(input("Numéro d'identification: "))
    département = input("Département: ")
    titre = input("Titre du poste: ")

    employé = Employé(nom, id, département, titre)
    dictionary[id] = employé



def rechercher_employé(dictionary):

    id = int(input("Entrez l'id de l'employé à rechercher: "))
    
    if id in dictionary:
        print("Informations de l'employé:")
        dictionary[id].afficher_informations()
    else:
        print("Employé introuvable")



def modifier_employé(dictionary):

    id = int(input("Entrez l'id' de l'employé à modifier: "))
    
    if id in dictionary:
        print("Modifiez les informations de l'employé:")
        employé = dictionary[id]
        employé.nom = input("Nouveau nom: ")
        employé.département = input("Nouveau département: ")
        employé.titre = input("Nouveau titre du poste: ")
    else:
        print("Employé introuvable")



def supprimer_employé(dictionary):

    id = int(input("Entrez l'id' de l'employé à supprimer: "))
    
    if id in dictionary:
        del dictionary[id]
        print("Employé supprimé avec succès.")
    else:
        print("Employé introuvable")



def afficher_menu():

    print("Menu:")
    print("1. Rechercher un employé")
    print("2. Ajouter un nouvel employé")
    print("3. Modifier les informations d'un employé")
    print("4. Supprimer un employé")
    print("5. Quitter le programme")



def main():

    dictio_employés = {
        47899: Employé("Susan Meyers", 47899, "Accounting", "Vice President"),
        39119: Employé("Mark Jones", 39119, "IT", "Programmer"),
        81774: Employé("Joy Rogers", 81774, "Manufacturing", "Engineer")
                }

    menu = input("Voulez-vous voir le menu? : (y pour oui) ")
    while menu =='y'  :

        afficher_menu()
        choix = input("Choississez une option: ")

        if choix == "1":
            rechercher_employé(dictio_employés)
        elif choix == "2":
            ajouter_employé(dictio_employés)
        elif choix == "3":
            modifier_employé(dictio_employés)
        elif choix == "4":
            supprimer_employé(dictio_employés)
        elif choix == "5":
            print("Programme quitté")
            break
        else:
            print("Choix invalide")
        menu = input("Voulez-vous revoir le menu? : (y pour oui) ")



if __name__ == '__main__':
    main()
