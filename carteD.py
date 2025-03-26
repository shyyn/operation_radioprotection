# Créé par m, le 12/03/2025 en Python 3.7

#  Affichage des lieux de mesure sur une carte
#crée la carte centrée sur la position de la première mesure
#récupère la latitude et la longitude et les stockent dans une variable (tuple)
import folium

def mapDonnees(l1,l2,l3,l4): #l1 latitude 1m l2 longitude 1m l3 latitude sol l4 longitude sol 
    #l1 latitude, l2 longitude
    coords = (l1[0],l2[0])
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

    for i in range (1,len(l1)):
    #récupère la latitude et la longitude et les stockent dans une variable (tuple)
        coords1m = (l1[i],l2[i])
        folium.Marker(location=coords1m, icon=folium.Icon(color='blue', icon='cloud'), popup = "Mesure n° " + str(i)+" à 1m sol").add_to(map)

    for i in range (1,len(l3)):
    #récupère la latitude et la longitude et les stockent dans une variable (tuple)
        coordsSol = (l3[i],l4[i])
        folium.Marker(location=coordsSol, icon=folium.Icon(color='green', icon='cloud'), popup = "Mesure n° " + str(i)+" au sol").add_to(map)

 #Ajouter un fond de carte (par exemple, 'Stamen Terrain')
 #folium.TileLayer('Geol').add_to(map)
 #https://www.geoportail.gouv.fr/carte?c=9.538240428706654,42.65116387114088&z=10&l0=ORTHOIMAGERY.ORTHOPHOTOS::GEOPORTAIL:OGC:WMTS(1)&l1=GEOLOGY.GEOLOGY::EXTERNAL:OGC:EXTERNALWMS(1)&permalink=yes'''

 #Sauvegarde la carte en html
        map.save(outfile='Openradiation.html')