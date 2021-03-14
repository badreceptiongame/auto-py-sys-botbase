import socket
import time
import binascii
from config import switchIP

def sendCommand(s, content):
    content += '\r\n' #important for the parser on the switch side
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((switchIP, 6000))

print('Starting')
time.sleep(1)
while True:
    sendCommand(s, "click A")
    time.sleep(4)


    