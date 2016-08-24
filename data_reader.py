# -*- coding: utf-8 -*-
"""
This file make serial connection from product to 'Demirdöküm İnternet Tabanlı
    Ürün Takip Sistemi' 
pyserial module has used

written by: Çağatay YÜRÜK Demirdöküm 2016 summer intern
"""
# -*- coding: utf-8 -*-

import serial  #import Pyserial module

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
    return bytes(line)  #line bytearrayden ','le ayrılmış veri paketine dönüştürülüyor

#data uygunluğunu kontrol et, ayır ve gönder
def getserialdata():
    hard_data = readline(ser)
    data_list = hard_data.split(',')
    while data_list[0] != ('E'):
        hard_data = readline(ser)
        data_list = hard_data.split(',')
    return data_list





