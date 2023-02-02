"""
/***********************************************************\
    PROJET OUTILS POUR LA CONCEPTION D’ALGORITHMES
    DÉTECTION DES COMMUNAUTÉS DANS LES RÉSEAUX SOCIAUX
    RÉALISÉ PAR : ELFRANI KHADIJA & AGHLAL NIZAR
    IATIC4 2022-2023
************************************************************/
"""
# PREMIÈRE PARTIE



import random
import json
import re
import matplotlib.pyplot as plt
import networkx as nx

class Graphe:
    # attributs de la classe
    def __init__(self):
        self.liste_adjacence = {}
        self.nbr_sommets = 0
        self.graph_dic = {}
        self.d_max = 0
        self.degre_count = {}


    #Fonction pour générer un graphe aléatoire à partir d'un nbr de sommets.

    def generate_graph(self):
        nbr_sommets = int(input("Entrer un nombre de sommets : "))
        # p : La probabilité d'avoir un arête générée aléatoirement
        p = round(random.uniform(0, 1), 1)
        self.nbr_sommets = nbr_sommets
        for n in range(self.nbr_sommets):
            self.liste_adjacence[n] = []
            for m in range(self.nbr_sommets):
                if n != m: # on ne veut pas de boucle
                    if random.randint(0,1) <= p:
                        self.liste_adjacence[n].append(m)
        # assurer que tous les voisins des sommets sont ajoutés
        for n in self.liste_adjacence:
            for m in self.liste_adjacence[n]:
                if n not in self.liste_adjacence[m]:
                    self.liste_adjacence[m].append(n)
        self.graph_dic = self.liste_adjacence
        # Affichage
        print("Le graphe générer aléatoirement : ")
        print(self.graph_dic)

    #Fonction pour récupérer Le degré maximum du graphe.

    def max_degree(self):
        # réccuperation du degré maximum du graphe
        for noeud in self.graph_dic:
            degree = len(self.graph_dic[noeud])
            if degree > self.d_max:
                self.d_max = degree
        print(self.d_max)

    #Fonction pour donner pour chaque degré du graphe le nombre de sommets ayant ce degré.

    # Version terminal :
    def nb_sommetdegre(self):
        for adjacence in self.graph_dic.items():
            degre = len(adjacence)
            if degre in self.degre_count:
                self.degre_count[degre] += 1
            else:
                self.degre_count[degre] = 1
        # Affichage
        print(self.degre_count)

    # Version graphique

    def nb_sommet_degre_plot(self):

        degres = []
        for v, adjacence in self.graph_dic.items():
            degre = len(adjacence)
            degres.append(degre)

        # affichage
        plt.hist(degres, bins=max(degres))
        plt.xlabel("degré")
        plt.ylabel("nombre de sommets")
        plt.title('distribution des degrés ')
        plt.show()

    #Fonction pour récupérer Le nombre de chemins induits dans le graphe de longueur 2.

    def chemins_induit(self):
        chemins = []
        for noeud in self.graph_dic:
            for voisin in self.graph_dic[noeud]:
                for voisin_voisin in self.graph_dic[voisin]:
                    if voisin_voisin != noeud and noeud not in self.graph_dic[voisin_voisin] and voisin_voisin not in \
                            self.graph_dic[noeud]:
                        chemins = [noeud, voisin, voisin_voisin]
                        chemins.append(chemins)
        # Affichage
        print(len(chemins))

    # Fonction pour extraire les données apartir d'un fichier txt, generer la liste d'adjacence de ce graphe .
    def get_data_from_file(self, nom_fichier, destination_fichier):
        fichier = open(nom_fichier)
        # Dictionnaire pour stocker le graphe {sommet ->[voisin] } sous forme de liste d'adjacente
        for line in fichier:
            temp_liste = re.split('\t|\n| ', line)
            if temp_liste[0] not in self.liste_adjacence.keys():
                self.liste_adjacence[temp_liste[0]] = []
            self.liste_adjacence[temp_liste[0]].append(temp_liste[1])

    # assurer que tous les voisins des sommets sont des voisins correspondants
        temp_list_voisins = []
        for n in self.liste_adjacence:
            for m in self.liste_adjacence[n]:
                if m not in self.liste_adjacence:
                     temp_list_voisins.append(m)
        for n in  temp_list_voisins:
            self.liste_adjacence[n] = []

    # extraire les voisins de tous les sommets
        for n in self.liste_adjacence:
            for m in self.liste_adjacence[n]:
                if n not in self.liste_adjacence[m]:
                    self.liste_adjacence[m].append(n)

        # stocker la liste dans le fichier .json de destination
        json_file = open(destination_fichier, "w")
        json_file.write(json.dumps(self.liste_adjacence))
        with open(destination_fichier, 'w') as f:
            json.dump(self.liste_adjacence, f)
            self.graph_dic = self.liste_adjacence

    def afficher_liste_adjacence(self):
        print(self.liste_adjacence)