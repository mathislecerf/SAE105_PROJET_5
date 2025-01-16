import csv
import matplotlib.pyplot as plt

#Importation des données csv dans une table.
table = []

with open('temperature-quotidienne-departementale.csv', newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        table.append(row)

del table[0] #Supression de la ligne 0 où se trouvent les descriptifs des données.


Temperature=[]
for i in range(len(table)-1) :
    if table[i]!= '':
        Temperature.append(table[i])
#Initialisation des listes nécessaire à la récupération des informations nécessaire du fichier csv
Date=[]
TemperatureMaximale=[]
TemperatureMinimale=[]
Departement=input('Entrez le code de département de votre choix : ')
for i in range(len(Temperature)-1 ):
    if Temperature[i][1] == Departement :
        Date.append(Temperature[i][0])
        TemperatureMaximale.append(Temperature[i][4])
        TemperatureMinimale.append(Temperature[i][3])

#Importation des seuils de température maximale et minimal de chaque département
Seuil=[]
with open('Seuil_température_canicule.csv', newline="") as csvfile:
    reader1=csv.reader(csvfile,delimiter=';')
    for row in reader1:
        Seuil.append(row)
del Seuil[0] #Supression de la ligne 0 où se trouvent les descriptifs des données.


#Récupération du seuil de température maximum et minimum du département demandé
for i in range(len(Seuil)-2):
    if Seuil[i][0] == Departement :
        TempMaxDep=Seuil[i][2]
        TempMinDep=Seuil[i][3]

duree_canicule=0 #Initialisation de la durée à 0 afin de traiter le cas d'une erreur dans le input
while duree_canicule <= 0 :
    duree_canicule=int(input("Entrez la durée minimale désirée : "))

#Initialisation des variables nécessaire à la détermination des canicules
jour_canicule=0
debut_canicule=""
fin_canicule=""
Canicule=[]
duree_canicule_jours = []
#Recherche des périodes de canicule
for j in range(len(TemperatureMaximale)-2):
    if float(TemperatureMaximale[j]) >= float(TempMaxDep) and float(TemperatureMinimale[j]) >= float(TempMinDep) :
        jour_canicule+=1
        '''
        print(f"Jour canicule détecté : {Date[j]}")
        print(jour_canicule)
        Ligne afin de tester le bon fonctionnement des conditions
        '''
        if jour_canicule==1:
            debut_canicule=Date[j]
        if jour_canicule >= duree_canicule:
            fin_canicule = Date[j]
            '''
            print(f"Début : {debut_canicule}, Fin : {fin_canicule}")
            ligne de test 
            '''           
    else :
        if jour_canicule >=duree_canicule:
            Canicule.append((debut_canicule,fin_canicule)) #Stockage des périodes de Canicule sous forme de tuple
            duree_canicule_jours.append(jour_canicule)
        jour_canicule = 0
        debut_canicule = ""
        fin_canicule=""

#Affichage des résultats du programme
periodes = [f"{c[0]}\n{c[1]}" for c in Canicule] 

plt.figure(figsize=(10, 6))
plt.bar(periodes, duree_canicule_jours, color='orange', edgecolor='black')
plt.xlabel("Périodes de canicule", fontsize=12)
plt.ylabel("Nombre de jours de canicule", fontsize=12)
plt.title(f"Histogramme des canicules pour le département {Departement}", fontsize=14)
plt.show()