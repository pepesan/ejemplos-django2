import coreapi
client = coreapi.Client()
schema = client.get('http://127.0.0.1:8000/doc/')
for item in schema:
    print(item)

data = client.action(schema, ['api', 'class', 'list'])
print(data)
for item in data:
    print(item)
    print(item['nombre'])

data = client.action(schema, ['api', 'class', 'create'], params={
    'nombre': 'Pepe',
}, validate=False)
print(data)
id= data['id']

data = client.action(schema, ['api', 'class', 'read'], params={
    'id': str(id)
})
print(data)
for item in data:
    print(data[item])

data = client.action(schema, ['api', 'class', 'update'], params={
    'id': id,
    'nombre': "Pepe",
    'precio': 14
}, validate=False)
print(data)

data = client.action(schema, ['api', 'class', 'delete'], params={
    'id': str(id)
})
print(data)
for item in data:
    print(data[item])
"""
data = client.action(schema, ['api', 'list'], params={
    'from': 'LHR',
    'to': 'PA',
    'date': '2016-10-12'
})
"""