# Créé par m, le 12/03/2025 en Python 3.7
import matplotlib.pyplot as plt
import numpy as np

def fichierChamps(nom,ls):
    # nom du fichier .txt en str et ls liste des champs
    g=open(nom,'w')
    for i in range(1,len(ls)):
   # print("Champs"+str(i),ch[i-1])
        g.write("Champs"+str(i) +' : ')
        g.write(ls[i-1])
        g.write('\n')
    g.close()


def grapheTemp(l1,l2):
    # l1 liste des température l2 liste des mesures
    print('Températures : ',l1)
    print('Mesures : ',l2)

    plt.plot(l1,l2,'rx',label='Mesures en fonction de la température')
    plt.legend()
    plt.show()

def grapheValMoy(l1,l2,m):
    # l1 liste des valeurs l2 liste des n°de mesure m moyenne
    mess1='Mesures en fonction du numéro '
    marr="{:.3f}".format(m)
    mess2='Valeur moyenne locale : '+str(marr)+' microS/h'
    plt.plot(l2,l1,'rx',label=mess1)
    mListe=[m for i in range(len(l1))]
    plt.plot(l2,mListe,'b-',label=mess2)
    plt.legend()
    plt.show()

# Séparation des valeurs entre sol et 1 m:
def grapheValMoyAlti(l1,l2,l3,l4,m0,m1):
    # l1 liste des valeurs au sol, l2 liste des valeurs à 1m, l3 des n°de mesure m moyenne au sol, l4 à 1m
    mess1='Mesures en fonction du numéro '
    marr0="{:.3f}".format(m0)
    marr1="{:.3f}".format(m1)
    mess2='Valeur moyenne locale : '+str(marr0)+' microS/h au sol'
    mess3='Valeur moyenne locale : '+str(marr1)+' microS/h à 1m'
    sigma0=np.std(l1)
    s0="{:.3f}".format(sigma0)
    sigma1=np.std(l2)
    s1="{:.3f}".format(sigma1)
    plt.plot(l3,l1,'bx',label=mess1)
    plt.plot(l4,l2,'gx',label=mess1)
    mListe0=[m0 for i in range(len(l1))]
    mListe1=[m1 for i in range(len(l2))]
    mListeSigma0P=[m0+3*sigma0 for i in range(len(l1))]
    mListeSigma0M=[m0-3*sigma0 for i in range(len(l1))]
    mListeSigma1P=[m1+3*sigma1 for i in range(len(l2))]
    mListeSigma1M=[m1-3*sigma1 for i in range(len(l2))]
    plt.plot(l3,mListe0,'b-',label=mess2)
    plt.plot(l4,mListe1,'g-',label=mess3)
    plt.plot(l3,mListeSigma0P,'r-')
    plt.plot(l3,mListeSigma0M,'r-')
    plt.plot(l4,mListeSigma1P,'r-')
    plt.plot(l4,mListeSigma1M,'r-')
    plt.legend()
    plt.show()