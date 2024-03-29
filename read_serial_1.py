import serial                    # import pySerial module
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#gspread protokol tanımlamaları
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('demirdokumuts-5693c98232f3.json', scope)

gc = gspread.authorize(credentials)

#seri haberleşme tanımlamaları
ser = serial.Serial('/dev/ttyUSB0') # open the COM Port
ser.baudrate = 19200          # set Baud rate
ser.bytesize = 8             # Number of data bits = 8
ser.timeout = 1
ser.parity   = 'N'           # No parity
ser.stopbits = 1             # Number of Stop bits = 1


#seri haberleşmeden gelen veriyi okuyan fonksiyon
def readline(a_serial, eol=b'\r'):
    leneol = len(eol)
    line = bytearray()
    while True:
        c = a_serial.read(1)
        if c:
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return line

# Open a worksheet from spreadsheet with one shot
wks = gc.open("sheet1").sheet1


i=0
while i<10:
    data = readline(ser)        #veriyi oku
    print (data)                #shell e veriyi yaz
    print ("veri numarası " + str(i))       
    wks.update_cell(1+i,2, data)        #drive'daki dosyanın 1. sütun i+1. satırını değiştir
    time.sleep(10)
    i += 1
    


        
ser.close()      
