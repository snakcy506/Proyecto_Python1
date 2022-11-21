import socket
# Comando universal para la utilizacion de socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind del servidor con el IP y PORT
client.connect(("localhost", 9999))

# Variable done para el while loop
done = False

# Asignacion del nombre sel usuario en el chat
username = input("Usuario: ")

# Loop que nos permite escribir hasta que el cliente se decida salir
while not done:
    client.send(input(username + ": ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == "salir":
        done = True
    else:
        print(msg)

# Cierra el cliente
client.close()