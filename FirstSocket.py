from socket import *
import threading
import sys

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print('Ready to serve...')
        request = connectionSocket.recv(1024).decode('utf-8')
        try :
            message = request.split(' ')
            print(message)
            filename = message[1]
            if(filename=="terninate"):processKill()
            f = open(filename[1 :])
            outputdata = f.read().encode()
            f.close()
            header = 'HTTP/1.1 200 OK\n'
            header += 'Content-Type: ' + 'text/html' + '\n\n'
    
    
        except :
            header = 'HTTP/1.1 404 Not Found\n\n'
            outputdata = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP ' \
                         'Server</p></center></body></html>'.encode('utf-8')
        final_response = header.encode('utf-8')
        final_response += outputdata
        connectionSocket.send(final_response)
        connectionSocket.close()


HOST = '127.0.0.1'
PORT = 6789
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
while True: #Establish the connection
    connectionSocket , addr = serverSocket.accept()
    newthread = ClientThread(addr , connectionSocket)
    newthread.start()
    
#Terminate the server
def processKill():
    serverSocket.close()
    sys.exit()


