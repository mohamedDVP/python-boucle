import random


# On vous donne une list n, parcourez cette liste et affichez ses valeurs
def display_list(ma_liste: list):
    for i in ma_liste:
        print(str(i))
    #for index, value in enumerate(ma_liste):
        #print("à l'index " + str(index) + ", se situe la valeur " + str(value))

#En python, les str sont egalement des tableau. des tableau de caractères
#Avec cette information, afficher chaque lettre d'une phrase donnée en parametre
def display_word_str(un_mot : str):
    for i in un_mot:
        print(str(i))


# Completez la fonction afin qu'elle puisse nous afficher les 100 premiers nombres entiers
def display_hundred_int():
    for i in range(0, 100):
        print(str(i))


# generez des nombres random, ajoutez les dans un tableau et faites la moyenne des notes.
# Si la note, est en dessous de 10 (exclu), affichez "Non admin", sinon, "admin"
def mention_moyenne():
    liste_note: list = []
    saisie_continue: bool = True
    while(saisie_continue):
        choix_utilisateur = input("Saisissez yes ou no : ")
        if choix_utilisateur == "no":
            saisie_continue = False
        else:
            note: float = random.uniform(0, 20)
            liste_note.append(note)
    if len(liste_note) == 0:
        print("non admis")
    else:
        somme: float = 0
        for i in liste_note:
            somme += i # somme = somme + 1
        resultat: float = somme / len(liste_note)
        if resultat < 10:
            print("non admis")
        else:
            print("admis")


# Affichez le nombre de voyelle que comporte un mot saisie par l'utilisateur
# Vous pouvez varier cet exercice en affichant le nombre de consonne
def display_number_voyelle():
    print("TODO")


# Affichez la table de multiplication (jusque 10 inclus) d'un nombre saisie par l'utilisateur
# different de 0
def table_multiplication():
    print("TODO")


# Calculez la factorielle d'un nombre
# Pour rappel, la factorielle de 5 vaux (1*2*3*4*5)
def factorielle():
    print("TODO")

if __name__ == "__main__":
    mention_moyenne()

