import serial                    # import pySerial module
import sys

ser = serial.Serial('COM3') # open the COM Port
ser.baudrate = 19200          # set Baud rate
ser.bytesize = 8             # Number of data bits = 8
ser.timeout = 1
ser.parity   = 'N'           # No parity
ser.stopbits = 1             # Number of Stop bits = 1


   
def readline(a_serial, eol=b'\r'):
    leneol = len(eol)
    line = bytearray()
    while True:
        c = a_serial.read(1)
        if c:
            print (type(c))
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return line


i=0
while i<10:
    data = readline(ser)
 
    print (data)
    i += 1
    print ("veri numarası " + str(i))
    
    
        
ser.close()      
