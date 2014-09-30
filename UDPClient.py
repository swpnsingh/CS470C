from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', 5432))
message=input('Input lowercase sentence:')
clientSocket.sendto(bytes(message.encode('utf-8')),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()