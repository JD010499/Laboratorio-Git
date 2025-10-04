import json

def info():
    return json.dumps({"message": "Hola Mundo", "userChange": "Juan David Campiño"})

print(info())