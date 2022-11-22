#!/usr/bin/python3
# Se imprtorta vidsteam la cual debe ser instalada previamente
# Importar SteamingServer de Vidstream
from vidstream import StreamingServer
import threading

# Asignar IP y PORT al servidor para crearlo
host = StreamingServer('192.168.100.5', 8888)
# Ejecucion del servidor
host.start_server()
# Envio de infromacion por medio de thread
t = threading.Thread(target=host.start_server)
t.start()
# While loop para que el servidor corra hasta que se esriba 'stop'
while input("") != 'stop':
    continue
# Cierra el servidor
host.stop_server()
