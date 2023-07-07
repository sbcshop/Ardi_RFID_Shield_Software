from machine import UART, Pin
import time

#Serial communication 
RFID = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

relay = machine.Pin(5, machine.Pin.OUT) #Define GPIO5 as output connected to relay
buzzer = machine.Pin(2, machine.Pin.OUT) #Define GPIO2 as output connected to buzzer

#initially switch off by setting LOW value
buzzer.value(0)
relay.value(0)

while 1:
    data_Read = RFID.readline(12) #read data bytes comming from RFID Module, 12 Bytes for our card (variable for different card)
    if data_Read is not None: # Enter when RFID card detected 
        print(data_Read)
        #data=data_Read.decode("utf-8") # convert raw data into utf-8 format
        #print(data)
        relay.value(1) # Switch ON Relay 
        buzzer.value(1) # Switch ON Buzzer 
        time.sleep(0.5)
    time.sleep(0.5)
    buzzer.value(0)
    relay.value(0)
