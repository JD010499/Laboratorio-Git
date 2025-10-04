import json
import time

def info():
    time.sleep(5)
    return json.dumps({"message": "Hola Mundo", "userChange": "Juan David Campiño"})

print(info())