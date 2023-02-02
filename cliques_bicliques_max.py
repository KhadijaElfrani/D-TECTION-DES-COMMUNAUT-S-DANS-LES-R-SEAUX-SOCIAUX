"""
/***********************************************************\
    PROJET OUTILS POUR LA CONCEPTION D’ALGORITHMES
    DÉTECTION DES COMMUNAUTÉS DANS LES RÉSEAUX SOCIAUX
    RÉALISÉ PAR : ELFRANI KHADIJA & AGHLAL NIZAR
    IATIC4 2022-2023
************************************************************/
"""
# TROISIÈME PARTIE

"""
Dans cette partie, on a implémenté des algorithmes liés à l’énumération des cliques et de bicliques maximales.
On a implementé l'algorithme 1 du papier : Hermelin, Manoussakis. “Efficient enumeration of maximal induced 
bicliques,” Discrete Applied Mathematics, 2021
Pour l'implémentation on aura aussi besoin de l’algorithme d’énumération de la partie 2 (bron_kerbosch)

Entrée: un graphe G
Sortie: tous les bicliques maximales du graphe G

"""

from bron_kerbosch import *

# Remarque : ci-dessous l'implémentation de l'algorithme 1 : les commentaires alors représentes les lignes du l'algorithme

def enumerer_cliques_max(G):
    # 1 : Calculer le k dégénéré et la liste des sommet ordonnée L
    k = degenerescence(G, False, True)

    # 2 : Calculer la liste d'adjacente générée par G
    L = degenerescence(G, True)

    n = len(list(G.keys()))

    # 3 : Initialiser un dictionnaire vide T (suffix tree)
    T = []
    # 4 : La boucle
    for j in range(1, n + 1):

        # 5 : calculer tous les cliques maximales du graphe g (on utilise la fonction de la partie 2)
        cliques = cliques_bron_kerbosch(G)
        # 6 : pour chaque clique du graphe
        for K in cliques:
            # 8 : Ordonner les sommets de k suivant L
            if K in T:
                break
            else:
                # 13 : insert the proper suffixes of I in T
                T.append(K)
                # 14 : Output I
                print(K)
