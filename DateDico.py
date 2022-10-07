#Entrer les valeurs
jour=int(input("Veuillez indiquez la journée: "))
mois=input("Veuillez indiquer le mois (en lettres minuscules): ")
annee=int(input("Veuillez indiquer l'année(entre 1600 et 2199): "))
#Trouver les 2 derniers chiffres de l'année
an=annee%100
#Trouver et ajouter le 1/4 de an et la valeur de jour à N 
N=an+((an-(an%4))/4)+jour
#Création du dico
dico={"janvier":0,"fevrier":3,"mars":3,"avril":6,"mai":1,"juin":4,"juillet":6,"aout":2,"septembre":5,"octobre":0,"novembre":3,"decembre":5,16:6,17:4,18:2,19:0,20:6,21:4,0:"Dimanche",1:"Lundi",2:"Mardi",3:"Mercredi",4:"Jeudi",5:"Vendredi",6:"Samedi"}
#Ajouter la valeur de mois à N
N=N+dico[mois]
i=0
#Verifier que l'année est bisextile
if (i==0 or i==2) and (annee%4==0 and annee%100!=0) or (annee%400==0):
    N=N-1
#Trouver les 2 premières valeurs de l'année
pre=(annee-an)/100
#Trouver la valeur finale de N
N=N+dico[pre]
#Trouver la valeur de la date
date=N%7
print("Le",jour,mois,annee,"était un :",dico[date])