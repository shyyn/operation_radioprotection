
import matplotlib.pyplot as plt
from math import *
import requests, folium, time, carteD,graphiqueD,calculD

# Calcul de moyennes:
def moyenneLocale(lat,lon,d):
    moy=0.0
    n=0
    for i in range(len(table3)):
        if calculD.distance(table3[i],table4[i],lat,lon,d):
            moy=moy+table2[i]
            n=n+1
    if n!=0:
        return moy/n,n
    else:
        return 'Pas de valeurs'

def moyenneLocaleAlti(lat,lon,d):
    moy0,moy1=0.0,0.0
    n,m=0,0
    for i in range(len(table3)):
        if table5[i]==0:
            if calculD.distance(table3[i],table4[i],lat,lon,d):
                moy0=moy0+table2[i]
                n=n+1
        if table5[i]==1:
            if calculD.distance(table3[i],table4[i],lat,lon,d):
                moy1=moy1+table2[i]
                m=m+1
    if n!=0 and m!=0:
        return moy0/n, moy1/m,n,m
    elif n!=0:
        return moy0/n, 'Pas de valeurs',n,m
    elif m!=0:
        return 'Pas de valeurs',moy1/m,n,m
    else:
        return 'Pas de valeurs'

def mesuresNum(lat,lon,d):
    mes,nume=[],[]
    for i in range(len(table3)):
        if calculD.distance(table3[i],table4[i],lat,lon,d):
            mes.append(table2[i])
            nume.append(i)
    return mes,nume

def mesuresNumAlti(lat,lon,d):
    mes0,mes1,nume0,nume1=[],[],[],[]
    for i in range(len(table3)):
        if calculD.distance(table3[i],table4[i],lat,lon,d):
            if table5[i]==0:
                mes0.append(table2[i])
                nume0.append(i)
            elif table5[i]==1:
                mes1.append(table2[i])
                nume1.append(i)

    return mes0,mes1,nume0,nume1

# Traiterment du fichier de données

#fich=str(input("Entrer le nom du fichier à traiter : "))
#fich=fich+".csv"

f=open('donnees24Mars15j.csv','r')
champs=f.readline()
ch=champs.rstrip().split(';')
lignes=f.readlines()
table1,table2,table3,table4,table5=[],[],[],[],[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
# table1 contient la température en°C (int)
    liste[4]=int(liste[4])
    table1.append(liste[4])
# table2 contient la mesure en microS/h (float)
    liste[5]=float(liste[5])
    table2.append(liste[5])
# table3 contient la latitude
    liste[10]=float(liste[10])
    table3.append(liste[10])
# table4 contient la longitude
    liste[11]=float(liste[11])
    table4.append(liste[11])
# table5 contient la hauteur par rapport au sol
    liste[28]=float(liste[28])
    table5.append(liste[28])

   # table=[ligne.rstrip().split(';') for ligne in f]
f.close()

#graphiqueD.fichierChamps('rep.txt',ch)
#graphiqueD.grapheTemp(table1,table2)
#print('Températures : ',table1)
#print('Mesures : ',table2)


# On choisit une lat et long: exemple L Giocante: 40,70360 et 9,44548
latG=42.70360
lonG=9.44548

#On choisit une distance d:
#d=float(input("Entrer la distance d :"))
d=10


mesureSolLati,mesureSollongi,mesure1mLati,mesure1mLongi=[],[],[],[]

for i in range(len(table3)) :
    if table5[i]==0:
        mesureSolLati.append(table3[i])
        mesureSollongi.append(table4[i])
    if table5[i]==1:
        mesure1mLati.append(table3[i])
        mesure1mLongi.append(table4[i])

#l1 latitude 1m l2 longitude 1m l3 latitude sol l4 longitude sol 
carteD.mapDonnees(mesureSolLati,mesureSollongi,mesure1mLati,mesure1mLongi)

# Affichage selon l'altitude:

moyL,nbr=moyenneLocale(latG,lonG,d)
moyL0,moyL1,nbr0,nbr1=moyenneLocaleAlti(latG,lonG,d)
print('moyenne : ',"{:.3f}".format(moyL),' microS/h à une distance de : ',d,' Km pour: ',nbr,' valeurs')
print('moyenne au sol : ',"{:.3f}".format(moyL0),' microS/h à une distance de : ',d,' Km pour: ',nbr0,' valeurs')
print('moyenne à 1 m : ',"{:.3f}".format(moyL1),' microS/h à une distance de : ',d,' Km pour: ',nbr1,' valeurs')
val,num=mesuresNum(latG,lonG,d)
val0,val1,num0,num1=mesuresNumAlti(latG,lonG,d)

#print(graphiqueD.grapheValMoy(val,num,moyL))
print(graphiqueD.grapheValMoyAlti(val0,val1,num0,num1,moyL0,moyL1))
