import requests

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
response = requests.get(url)
data = response.json()

# Punto 2: Número de respuestas contestadas y no contestadas
answered = 0
unanswered = 0

for item in data['items']:
    if item['is_answered'] == True:
        answered += 1
    else:
        unanswered += 1

print("Punto 2:")
print(f"Preguntas constestadas: {answered}")
print(f"Preguntas No Contestadas: {unanswered}")
print()

# Punto 3: Respuesta con menor número de vistas
sorted_items = sorted(data['items'], key=lambda x: x['view_count'])
print("Punto 3:")
print(f"Pregunta con el menor numero de vistas: {sorted_items[0]['title']}")
print()

# Punto 4: Respuesta más vieja y más actual
oldest = min(data['items'], key=lambda x: x['creation_date'])
newest = max(data['items'], key=lambda x: x['creation_date'])

print("Punto 4:")
print(f"La respuesta mas antigua es: {oldest['title']}, creada: {oldest['creation_date']}")
print(f"La respuesta mas nueva es: {newest['title']}, creada: {newest['creation_date']}")
print()

# Punto 5: Respuesta del propietario que tenga una mayor reputación
max_rep = max(data['items'], key=lambda x: x['owner']['reputation'])
print("Punto 5:")
print(f"La respuesta del propietario que tenga una mayor reputación es: {max_rep['title']}, reputation: {max_rep['owner']['reputation']}")