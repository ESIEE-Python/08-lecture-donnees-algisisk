#### Imports et définition des variables globales

"""
Ce script lit un fichier CSV contenant des listes d'entiers et propose plusieurs
fonctions pour manipuler ces listes : extraction, calcul de max, min, somme, etc.
"""

FILENAME = "listes.csv"

#### Fonctions secondaires
# fonction met chaque lignes dans une liste qui est lui même dans un grand liste

def read_data(filename):
    """
    Retourne le contenu du fichier <filename>
    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    try:
        l = []
        with open(filename, "r", encoding="utf8") as file:
            for line in file:
                l.append([int(x) for x in
                list((line.strip()).split(';'))])
                # '12;23;45;78" -> [12,23,45,78]
        return l
    except FileNotFoundError:
        print("Error fichier introuvable")
        return None


def get_list_k(data, k):
    """
    Retourne le kième liste de la grande liste
    Args :
        data : la liste des listes
        k : indice de la liste

    Returns : kième liste

    """
    assert  0 <= k <= len(data)
    return data[k]

def get_first(l):
    """
    Retourne la première liste
    Args :
        l : la liste de listes

    Returns : première liste

    """
    if not l:
        return None
    return l[0]

def get_last(l):
    """
    Retourne la dernière liste
    Args :
        l : la liste de listes

    Returns : dernière liste

    """
    if not l:
        return None
    return l[len(l) - 1]

def get_max(l):
    """
    Retourne l'entier maximum de la liste
    Args :
        l : la liste

    Returns : int maximum

    """
    if not l:
        return None
    return max(l)

def get_min(l):
    """
    Retourne l'entier minimum de la liste
    Args :
        l : la liste

    Returns : int minimum

    """
    if not l :
        return None
    return min(l)

def get_sum(l):
    """
    Retourne la somme de tous les entiers de la liste
    Args :
        l : la liste

    Returns : la somme des entiers

    """
    if not l :
        return None
    return sum(int(x) for x in l)


#### Fonction principale


def main():
    """
    Fonction principale qui exécute les différentes manipulations
    sur les données lues dans le fichier.
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

    print(get_first(read_data(FILENAME)))
    print(get_min(get_first(read_data(FILENAME))))
    print(get_max(get_first(read_data(FILENAME))))

if __name__ == "__main__":
    main()
