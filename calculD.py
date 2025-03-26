# Créé par m, le 12/03/2025 en Python 3.7
from math import *

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon moyen de la Terre en Km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2)* sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c  # Distance en km

# Exemple : Paris (48.8566, 2.3522) → New York (40.7128, -74.0060)
#distance = haversine(48.8566, 2.3522, 40.7128, -74.0060)
#print(f"Distance : {distance:.2f} km")

def distance(lat1,lon1,lat2,lon2,d):
    dist=haversine(lat1, lon1, lat2, lon2)
    if dist<=d:
        return True
    else:
        return False


