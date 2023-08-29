import socket as skt
import json
from time import sleep


class TcpServer:
    def __init__(self):
        self.PORT = 17267
        self.NAME = "ESP"
        self.IP_SERVER = "127.0.0.1"
        # self.IP_ADDR = skt.gethostbyname(skt.gethostname())
        self.name_client = {}
        self.derniere_action = None
        self.sauvegarde = None
        self.vitesse = 0
        self.connect = False
        self.client = None

    def socket_to_server(self, message, method, error):
        lst = []
        while True:
            if not self.connect:
                try:
                    self.client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
                    self.client.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
                    self.client.connect((self.IP_SERVER, self.PORT))
                    self.connect = True
                except OSError:
                    raise ConnectionRefusedError("Impossible de se connecter")
            gotoserv = {
                "method": method,
                "message": message,
                "error": error
            }
            dumps = json.dumps(gotoserv)
            print("oui")
            print(lst)
            self.client.sendall(dumps.encode())
            data = self.client.recv(1000).decode()

            if data == "OK":
                self.client.close()
                self.connect = False
                print(len(lst))
                print(lst)
                if len(lst) == 1:
                    return json.loads(lst[0])
                return
            else:
                lst.append(data)



if __name__ == "__main__":
    tcp = TcpServer()
    print(tcp.socket_to_server("", "GET", "200"))
    sleep(1)
    print(tcp.socket_to_server("unlock", "POST", "200"))
    sleep(1)
    print(tcp.socket_to_server("", "GET", "200"))
