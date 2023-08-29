import socket
import network
from time import sleep
import esp

esp.osdebug(None)

import gc


def main() -> None:
    gc.collect()
    # Entrer les paramètres du point d'accès
    ssid = 'AZERTY'
    password = 'lollollol'
    # Connexion au point d'accès
    station = network.WLAN(network.STA_IF)
    # station.ifconfig(('192.168.1.35', '255.255.255.0', '192.168.1.1', '192.168.1.1'))  # IP fixe sinon supprimer la ligne
    station.active(True)
    station.connect(ssid, password)
    # Attendre que l'ESP soit connecté avant de poursuivre
    print("Connexion ESP32 au point d'acces ", ssid)
    while not station.isconnected():
        print('.', end=" ")
        sleep(1)
    print("Connexion réussie")
    print("ESP32 : Adresse IP, masque, passerelle et DNS", station.ifconfig())
    return True
