from socket import *

# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 1111))
#
# server.listen()
#
# client, address = server.accept()
# name = input("Enter your name: ")
#
# while True:
#     data = client.recv(1024).decode('utf-8')
#     if data == 'quit':
#         client.close()
#     else:
#         print(data)
#     client.send(input(f"{name}: ").encode('utf-8'))

host = ''
port = 3000
buffer_size = 1024
sockaddres = (host, port)
servsock = socket(AF_INET, SOCK_STREAM)
servsock.bind(sockaddres)


while True:
    data, addr = servsock.recvfrom(buffer_size)
    print(data.decode('utf-8'))
    servsock.send(data, addr)
servsock.close()




