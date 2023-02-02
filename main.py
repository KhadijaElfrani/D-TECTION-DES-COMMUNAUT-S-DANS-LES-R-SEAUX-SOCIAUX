"""
/***********************************************************\
    PROJET OUTILS POUR LA CONCEPTION D’ALGORITHMES
    DÉTECTION DES COMMUNAUTÉS DANS LES RÉSEAUX SOCIAUX
    RÉALISÉ PAR : ELFRANI KHADIJA & AGHLAL NIZAR
    IATIC4 2022-2023
************************************************************/
"""

from Graphe import Graphe
from bron_kerbosch import *
from cliques_bicliques_max import *

graphe1 = Graphe()
graphe2 = Graphe()
graphe3 = Graphe()

# extraction des BD des réseau sociaux et les stocker dans des fichiers json

graphe1.get_data_from_file("reseaux_sociaux_data/facebook_combined.txt", "reseaux_sociaux_data/facebook.json")
graphe2.get_data_from_file("reseaux_sociaux_data/email-Eu-core.txt", "reseaux_sociaux_data/email.json")
graphe3.get_data_from_file("reseaux_sociaux_data/lastfm_asia_edges.txt", "reseaux_sociaux_data/asia.json")

while (1):
    choix = 0
    print("\n------------ ACCUEIL -------------\n")
    print("1 - Afficher la liste d'adjacence du graphe Facebook \n")
    print("2 - Afficher la liste d'adjacence du graphe Email \n")
    print("3 - Afficher la liste d'adjacence du graphe Asia \n")
    print("4 - Énumération des cliques d’un graphe \n")
    print("Remarque : l'option 4 vous permet d'afficher les détails sur les graphes de Stanford ou sur un graphe généré aléatoirement")

    # choix doit être un chiffre
    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        choix = int(input("Faites votre choix en saisissant un entier: "))

    if (choix == 1):
        print("Liste d'adjacence du graphe Facebook : ")
        graphe1.afficher_liste_adjacence()
    elif (choix == 2):
        print("Liste d'adjacence du graphe Email : ")
        graphe2.afficher_liste_adjacence()
    elif (choix == 3):
        print("Liste d'adjacence du graphe Lastfm Asia : ")
        graphe3.afficher_liste_adjacence()
    elif (choix == 4):

        print("1 - Graphe Facebook  \n")
        print("2 - Graphe Email \n")
        print("3 - Graphe Asia \n")
        print("4 - Générer un Graphe aléatoirement\n")
        print(
            "Remarque : Puisque le graphe Facebook est le plus lourd, l'affichage de ses cliques prends plus de temps. \n")

        try:
            choixGraphe = int(input("Sélectionnez un graphe : "))
        except ValueError:
            choixGraphe = int(input("Faites votre choix en saisissant un entier: "))

        if choixGraphe == 1:
            print("--- PARTIE 1 --- ")
            print("Degre max du graphe généré : ")
            graphe1.max_degree()
            print("Le nombre de chemins induits dans le graphe de longueur 2")
            graphe1.chemins_induit()
            print("Nombre de sommets pour chaque degré en graphique ( veuillez fermer le graphique pour afficher les autres détails de graphe)")
            graphe1.nb_sommet_degre_plot()
            print("--- PARTIE 2 --- ")
            print("Cliques du graphe Généré : ")
            print(cliques_bron_kerbosch(graphe1.graph_dic))
            print("--- PARTIE 3 --- ")
            print("Cliques et bicliques maximales du graphe Généré : ")
            cliques_max = enumerer_cliques_max(graphe1.graph_dic)
            print(cliques_max)

        elif choixGraphe == 2:
            print("--- PARTIE 1 --- ")
            print("Degre max du graphe généré : ")
            graphe2.max_degree()
            print("Le nombre de chemins induits dans le graphe de longueur 2")
            graphe2.chemins_induit()
            print("Nombre de sommets pour chaque degré en graphique ( veuillez fermer le graphique pour afficher les autres détails de graphe)")
            graphe2.nb_sommet_degre_plot()
            print("--- PARTIE 2 --- ")
            print("Cliques du graphe Généré : ")
            print(cliques_bron_kerbosch(graphe2.graph_dic))
            print("--- PARTIE 3 --- ")
            print("Cliques et bicliques maximales du graphe Généré : ")
            cliques_max = enumerer_cliques_max(graphe2.graph_dic)
            print(cliques_max)

        elif choixGraphe == 3:
            print("--- PARTIE 1 --- ")
            print("Degre max du graphe généré : ")
            graphe3.max_degree()
            print("Le nombre de chemins induits dans le graphe de longueur 2")
            graphe3.chemins_induit()
            print("Nombre de sommets pour chaque degré en graphique ( veuillez fermer le graphique pour afficher les autres détails de graphe)")
            graphe3.nb_sommet_degre_plot()
            print("--- PARTIE 2 --- ")
            print("Cliques du graphe Généré : ")
            print(cliques_bron_kerbosch(graphe3.graph_dic))
            print("--- PARTIE 3 --- ")
            print("Cliques et bicliques maximales du graphe Généré : ")
            cliques_max = enumerer_cliques_max(graphe3.graph_dic)
            print(cliques_max)

        elif choixGraphe == 4:
                    graphe4 = Graphe()
                    graphe4.generate_graph()
                    print("--- PARTIE 1 --- ")
                    print("Degre max du graphe généré : ")
                    graphe4.max_degree()
                    print("Le nombre de chemins induits dans le graphe de longueur 2")
                    graphe4.chemins_induit()
                    print("Nombre de sommets pour chaque degré en graphique ( veuillez fermer le graphique pour afficher les autres détails de graphe)")
                    graphe4.nb_sommet_degre_plot()
                    print("--- PARTIE 2 --- ")
                    print("Cliques du graphe Généré : ")
                    print(cliques_bron_kerbosch(graphe4.graph_dic))
                    print("--- PARTIE 3 --- ")
                    print("Cliques et bicliques maximales du graphe Généré : ")
                    cliques_max = enumerer_cliques_max(graphe4.graph_dic)
                    print(cliques_max)

