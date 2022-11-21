# Se imprtorta vidsteam la cual debe ser instalada previamente
# Importar ScreenShareClient de Vidstream 
from vidstream import ScreenShareClient

# Envio de informacion por medio de la IP y PORT
sender = ScreenShareClient('192.168.100.5', 8888)

# Iniciacion del stream
sender.start_stream()
