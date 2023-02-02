"""
/***********************************************************\
    PROJET OUTILS POUR LA CONCEPTION D’ALGORITHMES
    DÉTECTION DES COMMUNAUTÉS DANS LES RÉSEAUX SOCIAUX
    RÉALISÉ PAR : ELFRANI KHADIJA & AGHLAL NIZAR
    IATIC4 2022-2023
************************************************************/
"""
# DEUXIÈME PARTIE


"""
Pour l'énumération des cliques on a choisi l'algorithme de bron_kerbosch état l'algorithme le plus connu
pour cette tâche, on a pris la version avec l'ordre de degenerescence et comme demandé,
 on a implémenté que la version sans pivot de cette algorithme pour qu'il soit plus rapide étant donné des grands graphes.
L'algorithme à été trouvé en ligne et implementé par nous-mêmes sous python
source de l'algorithme : https://fr.wikipedia.org/wiki/Algorithme_de_Bron-Kerbosch

      Paramètres
          - param1: Une graphe G au format liste d'adjacence.
          - param2: Une ensemble contenant tous les sommets dans G tel que "p = set(G.keys())"
          - params(optionel) Il faut rien mettre

      Renvoyer
          Une liste contenant tous les cliques maximales
"""

import copy


def cliques_bron_kerbosch(graphe):
    p = set(graphe.keys())
    r = set()
    x = set()
    cliques = []
    for v in degenerescence(graphe, True):
        sommet = graphe[v]
        cliques_avec_pivot(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
        p.remove(v)
        x.add(v)
    return cliques


def cliques_avec_pivot(graphe, r, p, x, cliques):
    if len(p) == 0 and len(x) == 0:
        cliques.append(r)
    else:
        pivot = next(iter(p.union(x)))
        for v in p.difference(graphe[pivot]):
            sommet = graphe[v]
            cliques_avec_pivot(graphe, r.union([v]), p.intersection(sommet), x.intersection(sommet), cliques)
            p.remove(v)
            x.add(v)


"""
Fonction pour récupérer la liste des sommets ayant le même degré
Entrée: Un graphe
Sortie: Un dictionnaire trié (en ordre croissant) par clé.
            
"""


def sommets_pour_degre(graphe):
    D = {}

    for i in graphe.keys():
        try:
            D[len(graphe[i])].append(i)

        except KeyError:
            D[len(graphe[i])] = [i]

    D = dict(sorted(D.items()))

    return D


"""
Fonction pour dériver l’ordre de dégénérescence d’un graphe

Entrée : Un graphe 
Entrées optionnels :
    - en ordre : True si on veut la liste L dans l'ordre de dégénerescence
    - avec_degenerescense : True si on veut la dégénerescence k
Sortie :
        - (par defaut) Un dictionnaire avec le stockage des sommets regoupé de 1-core à k-core
        - la liste L dans l'ordre de dégénerescence
        - la dégénerescence k

source de l'algorithme implémenté : https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)

"""

def degenerescence(graphe, en_ordre=False, avec_degenerescense=False):
    """"
    # k : la dégénérescence
    # L : L'ordre de dégénerescence des sommets (liste)
    # sortie : Le stockage des sommets par groupe de 1-core à k-core
    # D :  La distribution des degrées
    """
    copie_graphe = copy.deepcopy(graphe)
    k = 0
    L = []
    sortie = {}
    D = sommets_pour_degre(copie_graphe)

    # Initialisation
    for i in range(1, max(D.keys())):
        sortie[i] = []

    # On initialise le degré courant i à 0
    i = 0

    while D:

        # Le degré minimum dans le graphe actuel
        i = list(D.keys())[0]

        k = max(k, i)

        # Choisit un sommet avec le degré minimum
        v = D[i].pop(0)

        L.append(v)

        del copie_graphe[v]

        sortie[k].append(v)

        for liste in copie_graphe.values():
            if v in liste:
                liste.remove(v)

        # Recalcul de La distribution des degrées
        D = sommets_pour_degre(copie_graphe)

        # Tri
    for e in sorted(sortie.keys(), reverse=True)[1:]:

        if not sortie[e + 1]:
            del sortie[e + 1]

        else:
            sortie[e] += sortie[e + 1]

    # On choisit la sortie en fonction du paramétres d'entrée
    if en_ordre:
        return L
    elif avec_degenerescense:
        return k
    else:
        return sortie
