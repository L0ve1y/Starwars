# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:56:49 2022

@author: PC
"""

class film:#Classe film
    nom_class="film"
    eps=[]
    def __init__(self):
        self.titre=""
        self.annee_sortie=0
        self.numero_episode=0
        self.cout=0
        self.recette=0
        self.actor=[]
    def __str__(self):
        print("les attributs de cette instance ", self.nom_class," sont:\nTitre= ",self.titre,"\nNumero d'Episode= ",self.numero_episode,"\nAnnée de sortie= ", self.annee_sortie,"\nCout de Production= ",self.cout,"\nRecette Généré= ",self.recette)
        return " "
    
#Question 11
    def nbActeurs(self):
        actor_length=(len(self.actor))-1
        return actor_length
    def nbPersonnages(self,lst):
        caract_length=0
        for i in self.actor:
            for j in lst:
                if i==j:
                    caract_length=caract_length+1
        return caract_length
    def calculBenefice(self):
        montant=0
        boolean=True
        if self.cout<self.recette:
            montant=self.recette-self.cout
            return (montant,boolean)
        else:
            montant=self.cout-self.recette
            boolean=False
            return (montant,boolean)
    def isBefore(self,annee):
        valeur=True
        if annee>self.annee_sortie:
            return valeur
        else:
            valeur=False
            return valeur
        
class acteur:# Classe Acteurs
    nom_class="acteur"
    def __init__(self):
        self.prenom=""
        self.nom=""
        self.perso=()
    def __str__(self):
        print("les attributs de cette instance ", self.nom_class," sont:\nNom= ",self.nom,"\nPrenom= ", self.prenom,"\n")
        return " "
#Question 9 retourner le nombre de personnage
    def nbPersonnages(self):
        perso_length=len(self.perso)
        return perso_length
    
class personnage:#Classe personnage
    nom_class="personnage"
    def __init__(self):
        self.prenom=""
        self.nom=""
    def __str__(self):
        print("les attributs de cette instance ", self.nom_class," sont:\nNom= ",self.nom,"\nPrenom= ", self.prenom,"\n")
        return " " 
class Gentil(personnage):#Classe de la force
    force=True
    
class Mechant(personnage):#Classe du coté obscur
    Obscur=True
    
def defil(values):
    for value in values:
        print(str(value))
        
#Question 13
def makeBackUp(dico):
     
     for v in dico.values():
         if v.numero_episode!=0:
             benef=0
             if v.cout<v.recette:
                 benef=v.recette-v.cout
             else:
                 benef=v.cout-v.recette
             print(v.annee_sortie," - ",v.titre," - ",benef)
      
#Question 2
#Création des trilogies
un=film();deux=film();trois=film();quatre=film();cinq=film();six=film();sept=film();huit=film();neuf=film()

#Remplissage des deux films    
quatre.titre="Un nouvel espoir"
quatre.annee_sortie=1977
quatre.numero_episode=4
quatre.cout=11000000
quatre.recette=775400000

    
cinq.titre="L'empire contre-attaque"
cinq.annee_sortie=1980
cinq.numero_episode=5
cinq.cout=18000000
cinq.recette=538380000

#Création du dico de film
dico_film={1:un,2:deux,3:trois,4:quatre,5:cinq,6:six,7:sept,8:huit,9:neuf}
numero_valeur=0
    
print("Hello!\nVeuillez entrer s'il vous plait:\n")
numero_valeur=int(input("Le numéro d'épisode(Compris entre 1 et 9 mise à part le 4 et le 5): "))
dico_film[numero_valeur].numero_episode=numero_valeur
dico_film[numero_valeur].titre=input("Le nom du film: ")
dico_film[numero_valeur].annee_sortie=int(input("L'année de sortie du film: "))

dico_film[numero_valeur].cout=int(input("Le coût de production du film: "))
dico_film[numero_valeur].recette=int(input("La recette généré par le film: "))

#Question 4 création collection
film.eps =[quatre,cinq,dico_film[numero_valeur]]

# Question 1 str et Question 5
print("\n",str(dico_film[numero_valeur]))
defil(film.eps)
#Question 3
Lst_caract=[]
caract_1=personnage()
print("Veuillez entrer s'il vous plait:\n")
caract_1.nom=input("Le nom du personnage:")
caract_1.prenom=input("Le prenom du personnage:")
dico_film[numero_valeur].actor.append(str(numero_valeur))
Lst_caract.append(str(numero_valeur))
Lst_caract.append(caract_1.nom)
#Question 8 Ajouter deux personnage à un même acteur
j=0
player_1=acteur()
print("Veuillez entrer s'il vous plait:\n")
player_1.nom=input("Le nom de l'acteur")
player_1.prenom=input("Le prenom de l'acteur")

dico_film[numero_valeur].actor.append(player_1.nom)
i=0
li=list(player_1.perso)
while i<2:
    caract_nom=input("Veuillez entrez le nom du personnage: ")
    li.append(caract_nom)
    Lst_caract.append(player_1.nom)
    Lst_caract.append(caract_nom)
    caract_prenom=input("Veuillez entrez le prenom du personnage: ")
    li.append(caract_prenom)
    i=i+1
player_1.perso=tuple(li)
print(player_1.nom, player_1.prenom)
for p in player_1.perso:
    print(p)
    
#NbActeur
nbA=film.nbActeurs(dico_film[numero_valeur])
print("Il y a :",nbA," acteurs dans ce film\n")

#NbPersonnage
nbP=film.nbPersonnages(dico_film[numero_valeur],Lst_caract)
print("Il y a :",nbP,"personnages dans ce film\n")
#CalculBenefice
boolean_3=True
somme,boolean_3=film.calculBenefice(dico_film[numero_valeur])
if boolean_3==True:
    print("Le Film est Bénéficiaire de: ",somme)
elif boolean_3==False:
    print("Le Film est Déficitaire de: ",somme)

#isBefore
boolean_2=True
an=int(input("Veuillez entrer une année s'il vous plait:"))
boolean_2=film.isBefore(dico_film[numero_valeur],an)
if boolean_2==True:
    print("Le Film est sortie avant l'année indiqué")
elif boolean_2==False:
    print("Le Film est sortie apres l'année indiqué")

#Tri
dico_film[numero_valeur].actor.remove(str(numero_valeur))
print("Voici le tableau d'acteur trié\n")
dico_film[numero_valeur].actor=sorted(dico_film[numero_valeur].actor)
for a in dico_film[numero_valeur].actor:
    print(a)
#makeBackUp
dico={1999:un,2002:deux,2005:trois,1977:quatre,1980:cinq,1983:six,2015:sept,2017:huit,2019:neuf}
print("Voici les résumé des films")
makeBackUp(dico)

