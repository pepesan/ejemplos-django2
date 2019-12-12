import coreapi
client = coreapi.Client()
schema = client.get('http://127.0.0.1:8000/api/')
for item in schema:
    print(item)
    for field in item:
        print(field)
        print(item[field])
