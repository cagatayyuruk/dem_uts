# -*- coding: utf-8 -*-
import data_reader
import data_logger
import time






data_number=1
ws_title=data_logger.conf_data_table("Cihaz 1")
print (ws_title)
while True:
    data= data_reader.getserialdata()
    print (data)
    data_logger.log_data(ws_title,data_number,data)
    data_number +=1
    print ("bitti")
    time.sleep(1)
    
    

