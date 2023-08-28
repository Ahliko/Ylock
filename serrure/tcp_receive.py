import socket as skt


class TcpReceive:
    def __init__(self):
        self.PORT = 17267
        self.NAME = "ESP"
        self.IP_SERVER = "127.0.0.1"  # TODO: change this to the server's IP address

    def hear(self):
        while True:
            try:
                server = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
                server.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
                server.bind((self.IP_SERVER, self.PORT))
                server.listen(5)
                client, address = server.accept()
                data = client.recv(1000).decode()
                client.sendall("OK".encode())
                client.close()
                server.close()
                return data
            except OSError:
                raise ConnectionRefusedError("Impossible de se connecter")

    @staticmethod
    def action(data):
        if data == "lock":
            return 0
        elif data == "unlock":
            return 1
        else:
            return -1
