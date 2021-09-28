import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 0

# host может измениться; хз, как корректно провернутьсвязь с сервером
server = '127.0.1.1', 8080


def get_msg():
    while True:
        data, address = s_client.recvfrom(1024)
        print(data)


s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_client.bind((host, port))

name = input('Введите имя: ')

string = threading.Thread(target=get_msg)
string.start()

s_client.sendto((name + ' connect to server').encode('utf-8'), server)

while True:
    message = input()
    s_client.sendto((name + ' :: ' + message).encode('utf-8'), server)

s_client.close()
