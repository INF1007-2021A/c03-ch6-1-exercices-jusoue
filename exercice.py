#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        nbr_list = []
        for nbr in range(10):
            nbr = input()
            nbr_list.append(nbr)
    nbr_list.sort()
    return print("Les valeurs ordonnees sont:", nbr_list)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        first = input("Premier mot:")
        second = input("Deuxieme mot:")
        mot1 = []
        mot2 = []
        anagramme = False
        for letter in first:
            mot1.append(letter)
        for letter in second:
            mot2.append(letter)
    
    if(mot1 == mot2):
        anagramme = True
    else:
        anagramme = False
    return print(anagramme)


def contains_doubles(items: list) -> bool:
    nbr_occ = 0
    for item in items:
        nbr_occ = items.count(item)
        if nbr_occ != 0:
            return True
        else:
            return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
