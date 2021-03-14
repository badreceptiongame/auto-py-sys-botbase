import socket
import time
import binascii
from config import switchIP, shinyFrame
import math

dSpeed = 0.01
shiny_frame = shinyFrame - 4
frame = 1
end_month = 1
month = 1
year = 0
estimate = math.floor(shiny_frame/26)

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((switchIP, 6000))

print("Starting - This will take about ", estimate, " minutes")

time.sleep(2)
while frame < shiny_frame:

    if year == 0 or 4:
        if month == 1:
            end_of_month = 31
        if month == 2:
            end_of_month = 29
        if month == 3:
            end_of_month = 31
        if month == 4:
            end_of_month = 30
        if month == 5:
            end_of_month = 31
        if month == 6:
            end_of_month = 30
        if month == 7:
            end_of_month = 31
        if month == 8:
            end_of_month = 31
        if month == 9:
            end_of_month = 30
        if month == 10:
            end_of_month = 31
        if month == 11:
            end_of_month = 30
        if month == 12:
            end_of_month = 31
    elif year != 0 or 4:
        if month == 1:
            end_of_month = 31
        if month == 2:
            end_of_month = 28
        if month == 3:
            end_of_month = 31
        if month == 4:
            end_of_month = 30
        if month == 5:
            end_of_month = 31
        if month == 6:
            end_of_month = 30
        if month == 7:
            end_of_month = 31
        if month == 8:
            end_of_month = 31
        if month == 9:
            end_of_month = 30
        if month == 10:
            end_of_month = 31
        if month == 11:
            end_of_month = 30
        if month == 12:
            end_of_month = 31
    
   
    if end_month < end_of_month:
        frame += 1
        end_month += 1
        sendCommand(s, "click A")
        time.sleep(0.2)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click A")
        time.sleep(1.7)


    if (end_month == end_of_month) and month == 12:
        frame += 1
        sendCommand(s, "click A")
        time.sleep(0.2)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click A")
        time.sleep(1.7)
        end_month = 1
        year += 1

    elif end_month == end_of_month:
        frame += 1
        sendCommand(s, "click A")
        time.sleep(0.2)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DLEFT")
        time.sleep(dSpeed)
        sendCommand(s, "click DUP")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(0.02)
        sendCommand(s, "click DRIGHT")
        time.sleep(0.02)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click DRIGHT")
        time.sleep(dSpeed)
        sendCommand(s, "click A")
        time.sleep(1.7)
        end_month = 1
        month += 1
    

                    