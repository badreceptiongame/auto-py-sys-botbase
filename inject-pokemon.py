import socket
import time
import binascii
from config import switchIP, pokemonFileLocation, pokemonFileName
importFile = pokemonFileLocation, pokemonFileName


def sendCommand(s, content):
    content += '\r\n' 
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((switchIP, 6000))

fileIn = open(importFile, "rb")
pokemonToInject = fileIn.read(344)
pokemonToInject = str(binascii.hexlify(pokemonToInject), "utf-8")

print('Starting')
time.sleep(2)
while True:
    sendCommand(s, f"poke 0x45075880 0x{pokemonToInject}")
    print("Pokemon injected")
    time.sleep(2)
    break