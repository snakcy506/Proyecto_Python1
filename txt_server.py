# Import socket
import socket
# Comando universal para la utilizacion de socket
txt_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind del servidor con el IP y PORT
txt_server.bind(("localhost", 9999))

# Nos indica que el servidor esta listo para aceptar conexiones de lcientes
txt_server.listen()
# Acepta conexion del cliente
client, addr = txt_server.accept()

# Variable done para el while loop
done = False

# Asignacion del nombre sel usuario en el chat
username = input("Usuario: ")

# Loop que nos permite escribir hasta que el cliente se decida salir
while not done:
    msg = (client.recv(1024).decode('utf-8'))
    if msg == 'salir':
        done = True
    else:
        print(msg)
    client.send(input(username + ": ").encode('utf-8'))

# Cerra el cliente y el server
client.close()
txt_server.close()
