import socket
import time
import binascii
from config import switchIP

def sendCommand(s, content):
    content += '\r\n' #important for the parser on the switch side
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((switchIP, 6000))

print('Starting - this will take 1 minute')
time.sleep(1)
while True:
    sendCommand(s, "click A")
    print("Initialize conversation")
    time.sleep(4)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click DDOWN")
    time.sleep(0.5)
    sendCommand(s, "click A")
    print("I want visitors")
    time.sleep(4)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click DDOWN")
    time.sleep(0.5)
    sendCommand(s, "click A")
    print("Via online play")
    time.sleep(4)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click A")
    print("Connecting to the Internet")
    time.sleep(16)
    sendCommand(s, "click A")
    time.sleep(4)
    sendCommand(s, "click DDOWN")
    time.sleep(0.2)
    sendCommand(s, "click A")
    print("Invite via Dodo Code")
    time.sleep(4)
    sendCommand(s, "click A")
    time.sleep(4)
    sendCommand(s, "click DDOWN")
    time.sleep(0.5)
    sendCommand(s, "click A")
    print("The more the merrier")
    time.sleep(4)
    sendCommand(s, "click A")
    time.sleep(5)
    sendCommand(s, "click A")
    time.sleep(4)
    sendCommand(s, "click A")
    print("Invite anyone")
    time.sleep(5)
    sendCommand(s, "click A")
    print("Dodo Code recieved")
    time.sleep(60)
    break

    