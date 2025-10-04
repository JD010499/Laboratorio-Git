import json
import time

def info():
    time.sleep(5)
    print("Procesando solicitud...")
    return json.dumps({"message": "Hola Mundo", "userChange": "Juan David Campiño", "status": "Limpieza"})

print(info())