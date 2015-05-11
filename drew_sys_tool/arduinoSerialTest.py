from time import sleep
import serial
import re
#ser = serial.Serial('/dev/tty.usbmodem1d11', 9600) # Establish the connection on a specific port
ser = serial.Serial('COM8', 9600) # Establish the connection on a specific port
counter = 0 # Below 32 everything in ASCII is gibberish
state = 0
while True:
    data = ser.readline().decode()
    data = data.replace('\r\n', '')
    splitData = re.split('\,', data)
    type = splitData[0]
    if (type == '0'):          
        wearableId = splitData[1]
        zoneId = splitData[2]
        signalStrength = splitData[3]
        print('Wearable ID=', wearableId)
        print('Zone ID=', zoneId)
        print('Signal Strength=', signalStrength)
        print()
    elif (type == '1'):
        wearableId = splitData[1]
        print('Found wearable with id=', wearableId)
        print()
    if (counter % 3) == 0:
        state = 1-state
        if (state == 0):
            ser.write('0'.encode())
        elif (state == 1):
            ser.write('1'.encode())
    
    counter += 1