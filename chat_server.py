import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostbyname(socket.gethostname())  # может поменяться
port = 8080

server.bind((host, port))

clients = []

print('*Connected*')
while True:
    data, address = server.recvfrom(1024)

    if address not in clients:
        clients.append(address)

    print(address, "::", data)

    for client in clients:
        if address == client:
            continue
        server.sendto(data, client)

server.close()
