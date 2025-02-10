import requests

# URL de l'API
url = 'https://request.openradiation.net/measurements?apiKey=bde8ebc61cb089b8cc997dd7a0d0a434'

# Faire une requête GET
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Traiter la réponse JSON
    data = response.json()
    print(data)
else:
    print(f"Erreur: {response.status_code}")
