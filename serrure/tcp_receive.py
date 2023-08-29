import socket as skt
from json import loads, dumps


class TcpReceive:
    def __init__(self):
        self.PORT = 17267
        self.NAME = "ESP"
        self.IP_SERVER = "127.0.0.1"  # TODO: change this to the server's IP address
        self.client = None
        self.server = None

    def hear(self):
        while True:
            try:
                self.server = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
                self.server.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
                self.server.bind((self.IP_SERVER, self.PORT))
                self.server.listen(5)
                self.client, address = self.server.accept()
                data = self.client.recv(1000).decode()
                return loads(data)
            except OSError:
                raise ConnectionRefusedError("Impossible de se connecter")

    @staticmethod
    def action(data):
        print(data)
        if data == "lock":
            return 0
        elif data == "unlock":
            return 1
        else:
            return -1

    def close(self):
        self.client.sendall("OK".encode())
        self.client.close()
        self.server.close()


if __name__ == "__main__":
    tcp = TcpReceive()
    while True:
        data = tcp.hear()
        action = tcp.action(data["message"])
        print(action)
