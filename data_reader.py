# -*- coding: utf-8 -*-
"""
This file make serial connection from product to 'Demirdöküm İnternet Tabanlı
    Ürün Takip Sistemi' 
pyserial module has used

written by: Çağatay YÜRÜK Demirdöküm 2016 summer intern
"""
# -*- coding: utf-8 -*-

import serial  #import Pyserial module
import io
import time

ser = serial.Serial("/dev/ttyUSB0", baudrate=19200,
                    bytesize=8, parity='N', stopbits=1
                    , rtscts=1)


sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii')
def getserialdata():
    ser.flushInput()
    print sio.readline()
    hard_data = sio.readline()
    data_list = hard_data.split(',')
    return data_list
    
    



"""
#data uygunluğunu kontrol et, ayır ve gönder
def getserialdata():
    hard_data = readline()
    data_list = hard_data.split(',')
    while data_list[0] != ('E'):
        hard_data = readline()
        data_list = hard_data.split(',')
    ser.flush()
    return data_list

"""

