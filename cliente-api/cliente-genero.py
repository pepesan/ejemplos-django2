import requests, json
url = "http://localhost:8000/api/genero/"
id = 0

def dameItems():
    # Petición Get /
    try:
        response = requests.get(url)
        json_data = response.json()
        print(json_data)
        for item in json_data:
            print(item)

    except :
        print("Error al hacer la consulta")

def insertaItem():
    # Petición Post /
    try:
        payload = {
            "nombre": "Novela Negra"
        }
        headers = {
            'Content-Type': "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        json_data = response.json()
        print(json_data)
        id = json_data['id']
        return id
    except:
        print("Error al hacer la consulta")

def cogeItem(id):
    # Petición Get /{id}
    try:
        response = requests.get(url+str(id))
        json_data = response.json()
        print(json_data)

    except:
        print("Error al hacer la consulta")

def actualizaItem(id):
    # Petición Put /{id}
    try:
        payload = {
            "nombre": "Novela Negra!"
        }
        headers = {
            'Content-Type': "application/json"
        }
        response = requests.put(url+str(id), data=json.dumps(payload), headers=headers)
        json_data = response.json()
        print(json_data)
    except:
        print("Error al hacer la consulta")

def borraItem(id):
    # Petición DELETE /{id}
    try:
        response = requests.delete(url + str(id))
        print(response)
        json_data = response.json()
        print(json_data)

    except:
        print("Error al hacer la consulta de borrado")

dameItems()
id = insertaItem()
cogeItem(id)
actualizaItem(id)
borraItem(id)