# -*- coding: utf-8 -*-
#"Demirdöküm İnternet Tabanlı Saha Testi Ürün Takip Sistemi" v. 0.06
#2016 Summer İntern Çağatay YÜRÜK

import data_reader
import data_logger
import time
import json

#main test function
def start_test(device_name):
    ws_title=data_logger.conf_data_table(device_name)
    print (ws_title)
    while True:
        data= data_reader.getserialdata()       #Karttan datayı oku
        try:
            data_logger.log_data(ws_title,data)
            print (data)
            print ("bitti")
            time.sleep(5)
        except gspread.exceptions.HTTPError:
            time.sleep(10)
            data.append("Bağlantı Hatası: 500")
            data_logger.log_data(ws_title,data)
            print ("bitti")            
            

#Get settings from test_stat.txt file
with open("test_stat.txt","r")as f:
    d=f.read()
test=json.loads(d)
if test['test1']['status']== u'1':
    print ("Test başlıyor.")
    device_name = test['test1']['device_name']
    start_test(device_name)
else:
    print('Test pasif.')




    
    

