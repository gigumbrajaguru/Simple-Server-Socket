import socket

print("Please, Enter Server:")
SERVER = input()
if(SERVER==""):
    SERVER = "127.0.0.1"
print("Please, Enter Port")
PORT = input()
if(PORT==""):
    PORT = 6789
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

def sentMessage() :
    in_data = client.recv(1024).decode()
    print("From Server :" , in_data)

client.connect((SERVER , PORT))
client.sendall(bytes("ClientData: /HelloWorld.html", 'UTF-8'))
sentMessage()

while True :
    client.close()
    print("Please, Enter File path( starting from '/' or Enter 'q' to exit):")
    out_data = input()
    if out_data == 'q':
        break
    else:
        client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client.connect((SERVER , PORT))
        client.sendall(bytes("ClientData: "+ out_data, 'UTF-8'))
        sentMessage()

    
