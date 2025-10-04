import json
import time

def info():
    time.sleep(5)
    print("Procesando solicitud...")
    return json.dumps({"message": "Hola Mundo", "userChange": "Juan David Campiño", 'metadata': {'status': 'success', 'code': 200}})

print(info())