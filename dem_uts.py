# -*- coding: utf-8 -*-
#"Demirdöküm İnternet Tabanlı Saha Testi Ürün Takip Sistemi" v. 0.06
#2016 Summer İntern Çağatay YÜRÜK

import data_reader
import data_logger
import time
import json
import gspread

#main test function
def start_test(device_name,sheet):
    ws_title=data_logger.conf_data_table(device_name,sheet)
    print (ws_title)
    while True:
        data= data_reader.getserialdata()       #Karttan datayı oku
        try:
            data_logger.log_data(ws_title,data)
            print (data)
            print ("bitti")
            time.sleep(5)
        except gspread.exceptions.HTTPError:
            print ("Bağlantı Hatası: 500")
            time.sleep(10)
            print ("bitti")            
            
#start
#Get settings from test_stat.txt file
with open("test_stat.txt","r")as f:
    d=f.read()
test=json.loads(d)
if test['test1']['status']== u'1':
    print ("Test başlıyor.")
    device_name = test['test1']['device_name']
    test_sheet = test['test1']['sheet']
    start_test(device_name,test_sheet)
else:
    print('Test pasif.')




    
    

