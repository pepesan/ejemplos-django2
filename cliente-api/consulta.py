import requests, json
url = "http://localhost:8000/api/"
id = 0
# Petición Get /
try:
    response = requests.get(url)
    json_data = response.json()
    print(json_data)
    for item in json_data:
        print(item)
        print(item['nombre'])

except :
    print("Error al hacer la consulta")

#Petición Post /
try:
    payload = {
        "nombre": "Pepe",
        "precio": 23.0
    }
    headers = {
        'Content-Type': "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    json_data = response.json()
    print(json_data)
    id=json_data['id']

except :
    print("Error al hacer la consulta")

# Petición Get /<int:pk>
try:
    response = requests.get(url+str(id))
    json_data = response.json()
    print(json_data)

except :
    print("Error al hacer la consulta Show")

#Petición PUT /<int:pk>
try:
    payload = {
        "nombre": "Pepe",
        "precio": 25.0
    }
    headers = {
        'Content-Type': "application/json"
    }
    response = requests.put(url+str(id), data=json.dumps(payload), headers=headers)
    json_data = response.json()
    print(json_data)

except :
    print("Error al hacer la consulta Edit")

# Petición Delete /<int:pk>
try:
    response = requests.delete(url+str(id))
    json_data = response.json()
    print(json_data)

except :
    print("Error al hacer la consulta Delete")




