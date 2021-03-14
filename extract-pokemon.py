import socket
import time
import binascii
from config import switchIP, pokemonFileLocation
exportFile = pokemonFileLocation, "lastReceived.ek8"

def sendCommand(s, content):
    content += '\r\n' #important for the parser on the switch side
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.0.243", 6000))

print('Starting')
time.sleep(2)
while True:
    sendCommand(s, "peek 0x45075880 344") #get pokemon from box1slot1
    time.sleep(0.5) #give time to answer
    pokemonBytes = s.recv(689)
    pokemonBytes = pokemonBytes[0:-1] #cut off \n at the end
    fileOut = open(importFile, "wb")
    fileOut.write(binascii.unhexlify(pokemonBytes))
    fileOut.close()
    print('Extracted Pokemon')
    break
    