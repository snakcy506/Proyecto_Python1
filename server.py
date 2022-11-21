# Importa socket y threading para creacion, ejecucion y envio de informacion del servidor
import socket
import threading
# Asignacion del puerto
port = 5050
# Asignacion automatica de la IPV4
ip = socket.gethostbyname(socket.gethostname())
# Creacion del servidor
server_add = (ip, port)
# Comando estandar de sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_add)

# Lista para las conexiones de los clientes
conex = []

def handleclient(conn, addr):
    # Append de la id del usaurio a la lsita de conexiones
    conex.append(conn)
    if len(conex) >= 2:
        conex[0].send("drawer".encode("utf-8"))
        for x in conex[1:]:
            x.send("".encode("utf-8"))
    while True:
        # Envio de coordenadas que nos permite que todos los clientes tengan el mismo dibujo
        msg = conn.recv(64)
        if msg:
            for x in conex:
                x.send(msg)


# Funcion que nos permite saber cuando el servidor esta en linea y cuando se conecta un cliente
def start_up():
    s.listen()
    print("Servidor en linea")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handleclient, args =(conn,addr)).start()
        print("Cliente conectado")
        
start_up()

