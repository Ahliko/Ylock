import socket as skt


class TcpServer:
    def __init__(self):
        self.PORT = 17267
        self.NAME = "ESP"
        self.IP_SERVER = "172.20.10.11"
        # self.IP_ADDR = skt.gethostbyname(skt.gethostname())
        self.name_client = {}
        self.derniere_action = None
        self.sauvegarde = None
        self.vitesse = 0
        self.connect = False
        self.client = None

    def socket_to_server(self, message):
        if not self.connect:
            try:
                client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
                client.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
                client.connect((self.IP_SERVER, self.PORT))
                self.connect = True
            except OSError:
                raise ConnectionRefusedError("Impossible de se connecter")
        self.client.sendall(message.encode())
        data = self.client.recv(1000).decode()
        if data == "OK":
            self.client.close()
            self.connect = False
            return
        return data
