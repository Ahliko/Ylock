import tcp_receive as tcp
from time import sleep
import lock_unlock as lu

lock = lu.Lock()
tcp = tcp.TcpReceive()

while True:
    data = tcp.hear()
    if data["method"] == "POST":
        action = tcp.action(data["message"])
        if action == 0:
            lock.lock()
        elif action == 1:
            lock.unlock()
    sleep(0.1)
