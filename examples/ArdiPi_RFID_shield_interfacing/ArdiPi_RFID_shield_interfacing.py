from machine import UART, Pin      #import serial and pin access library
import time    

#Serial communication 
RFID = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

relay = machine.Pin(5, machine.Pin.OUT) #Define GPIO5 as output connected to relay
buzzer = machine.Pin(2, machine.Pin.OUT) #Define GPIO2 as output connected to buzzer

#initially switch off by setting LOW value
buzzer.value(0)
relay.value(0)
toggleVal = True

while 1:
    data_Read = RFID.readline(12)    #read RFID data byte
    if data_Read is not None: # enter when RFID card detected
        toggleVal = not toggleVal
        print(data_Read)
        data=data_Read.decode("utf-8") # convert raw data into utf-8 format
        print(data)
        relay.value(toggleVal) # Toggle Relay 
        buzzer.value(1) # Switch ON Buzzer 
    time.sleep(0.2)    # wait 0.2 second
    buzzer.value(0)

