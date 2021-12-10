# -*- coding: cp1252 -*-

from random import *


class jeu():
    def __init__(self):
        self.pseudo = []  ## nom du joueur
        self.codeSecret = None  ## code secret
        self.entreJoueur = None  ##code saisi par le joueur
        self.niveau = []  ##niveau de difficulté [nb de tour ,nb de pions,nb couleur]
        self.fin = []  ## si le jeu est fini =1 sinon =0

    def verif(self):  ##verification de la combinaison saisi par le joueur
        vrai = 0
        place = 0
        pion = self.entreJoueur.para[1]
        mask1 = [0] * pion
        mask2 = [0] * pion
        self.entreJoueur.saisiJoueur()
        for i in range(pion):
            if self.codeSecret.code[i] == self.entreJoueur.code[i]:
                place = place + 1
                mask1[i] = 1
                mask2[i] = 1

        for i in range(pion):
            for j in range(pion):
                if self.codeSecret.code[i] == self.entreJoueur.code[j]:
                    if i != j:
                        if mask1[i] == 0:
                            if mask2[j] == 0:
                                vrai = vrai + 1
                                mask1[i] = 1
                                mask2[j] = 1

        if place == pion:
            self.fin = 1

        print("bonne couleurs mal placée:", vrai)
        print("bien placee:", place)

    def diff(self):  ##niveau de difficulté [nb de tour ,nb de pions,nb couleurs]

        cpt = 0
        test = 0
        boucle = 0
        while cpt == 0:
            dif = input("Niveau 1, 2, 3 ou 4 pour un niveau custom?")
            if dif.isdigit() == True:
                print("Niveau:", dif)

                if dif == "1":
                    self.niveau = [9, 4, 8]
                    print("9 tours pour deviner une combinaison de 4 pions composé de 8 couleurs compris entre 0 et 8")
                    cpt = 1

                if dif == "2":
                    self.niveau = [11, 5, 9]
                    print("11 tours pour deviner une combinaison de 5 pions composé de 9 couleurs compris entre 0 et 9")
                    cpt = 1

                if dif == "3":
                    self.niveau = [13, 6, 10]
                    print("13 tours pour deviner une combinaison de 6 pions composé de 10 couleurs compris entre 0 et 10")
                    test = 1
                    cpt = 1

                if dif == "4":
                    while test == 0:

                        while boucle == 0:
                            a = input("Nombre de tours?")
                            if a.isdigit() == True:
                                int(a)
                                self.niveau = [a]
                                boucle = 1
                            else:
                                print("La valeur n'est pas un niveau disponible")

                        while boucle == 1:
                            b = input("Nombre de pions?")
                            if b.isdigit() == True:
                                int(b)
                                self.niveau.append(int(b))
                                boucle = 2
                            else:
                                print("La valeur n'est pas un niveau disponible")

                        while boucle == 2:
                            c = input("Nombre de couleurs(<10)?")
                            if c.isdigit() == True:
                                self.niveau.append(int(c))
                                boucle = 0
                                test = 1
                                cpt = 1
                                print("tour:", a, "pions:", b, "couleurs:", c, "cpt", cpt)
                            else:
                                print("La valeur n'est pas un niveau disponible")


                else:
                    print("La valeur n'est pas un niveau disponible")

            else:
                print("Ce n'est pas un chiffre ")

        self.codeSecret = combi(self.niveau)
        self.entreJoueur = combi(self.niveau)

    def start(self): #Initialisation du jeu récupère les infos du joueur et la difficulté du niveau
        self.fin = 0
        self.pseudo = input("Quelle est ton pseudo?")
        print("Bienvenue", self.pseudo)
        self.diff()
        self.codeSecret.codeAlea()
        print("self.codeSecret", self.codeSecret.code)

        cpt = 0

        while cpt < int(self.entreJoueur.para[0]):
            self.verif()
            cpt = cpt + 1
            print("tour:", cpt)
            if self.fin == 1:
                cpt = self.entreJoueur.para[0]
                print("Bravo!!")
            if cpt == self.entreJoueur.para[0]:
                if self.fin == 0:
                    print("perdu")
                    print("Le code est:", self.codeSecret.code)


class combi():
    def __init__(self, para):
        self.code = []  ## code secret ou code saisi par le joueur
        self.para = para  ##niveau de difficulté [(0)nb de tour ,(1)nb de pions,(2)nb couleurs]

    def codeAlea(self):  ## génère un code aléatoire
        cpt = 0
        pion = self.para[1]
        couleur = int(self.para[2])
        while cpt < pion:
            c = randrange(0, couleur)
            self.code.append(int(c))
            cpt = cpt + 1

    def saisiJoueur(self):  ## aquisition du code saisi par le joueur
        cpt = 0
        pion = self.para[1]
        while cpt == 0:
            liste = input("combinaison?")
            if liste.isdigit() == True:
                if len(liste) == pion:
                    self.code = [int(u) for u in list(liste)]
                    pion = self.para[1]
                    pion = pion + 1
                    print(self.code)
                    cpt = 1
                else:
                    print("le code est trop court/long")
            else:
                print("Ce n'est pas un chiffre ")


mastermind = jeu()
mastermind.start()