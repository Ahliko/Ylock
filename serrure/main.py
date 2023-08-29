import tcp_receive as tcp
from time import sleep
# import lock_unlock as lu
from json import loads, dumps

# lock = lu.Lock()
tcp = tcp.TcpReceive()
status = "lock"

while True:
    data = tcp.hear()
    if data["method"] == "POST":
        action = tcp.action(data["message"])
        if action == 0:
            # lock.lock()
            status = "lock"
        elif action == 1:
            # lock.unlock()
            status = "unlock"
    elif data["method"] == "GET":
        gotoserv = {
            "method": "GET",
            "message": "lock" if status == "lock" else "unlock",
            "error": "200"
        }
        tcp.client.sendall(dumps(gotoserv).encode())
    sleep(1)
    tcp.close()
    sleep(0.1)
