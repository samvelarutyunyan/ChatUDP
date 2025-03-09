from socket import *

# client = socket(AF_INET, SOCK_STREAM)
#
# client.connect(('127.0.0.1', 1111))
#
# name = input("Enter your name: ")
#
# while True:
#     client.send(input(f"{name}: ").encode('utf-8'))
#     data = client.recv(1024).decode('utf-8')
#     if data == 'quit':
#         client.close()
#     else:
#         print(data)
#     client.send(input(" ").encode('utf-8'))

host = '127.0.0.1'
port = 3000
buffer_size = 1024
sockaddres = (host, port)
clientsock = socket(AF_INET, SOCK_STREAM)



name = input("Enter your name: ")
while True:
    data = name + ': ' + input('>')
    data = data.encode('utf-8')
    clientsock.sendto(data, sockaddres)
clientsock.close()
