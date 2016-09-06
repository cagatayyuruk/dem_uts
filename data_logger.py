# -*- coding: utf-8 -*-

#client e-mail: demirdokumuts@appspot.gserviceaccount.com
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

#gspread protokol tanımlamaları
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('demirdokumuts-5693c98232f3.json', scope)

gc = gspread.authorize(credentials)

#zaman bilgisi ayarlamaları
now = datetime.now()
time = '%s:%s:%s' % (now.hour, now.minute, now.second)
day = '%s/%s/%s' % (now.day, now.month, now.year)


#Tablo başlıkları
table_headers = [" ","E", "Working\nMode", "Heat Demand\nMode","Error Flags","DHW Curr\nTemp",\
                "Solar Curr\nTemp","Display Type","DHW Set\nTemp","Display Parameter\nAfter Change\Wait Cnt",\
                "I Error","\"H\"","D Error","Pout","I Out","D Out","M","PID Out","Curr Modulator\nCurrent",\
                "\"S\"","Heat Demand\nSource","Gas Valve\nModulation Type","Peripheral Out","Pot Position\nOffto On Cnt",\
                "dummy","Target Modulator\nCurrent","On Off Pot\nAdc Val","Prog Parameters","Antifreeze Timeout",\
                "DHW Pot Adc Val","Antifreeze F","Antifreeze Wait\nCnt","Flow Rate","Peripheralln","Dummy","SW_Version","ENTER"]



#cihaz adı ve saate göre yeni çalışma sayfası oluşturup tablo başlıklarını atma
#açılan sayfanın adını döner
def conf_data_table(device_name,sheet): #device_name: oluşturulacak yeni sayfa için cihaz adı
    header1 = "%s" % (device_name)   
    table_headers[0]=header1          #Takibi yapılan cihazın Adı nı başa ata    

    #Kayıt yapılacak çalışma sayfasını oluştur
    ws_title = "%s %s %s" % (device_name,day, time)    #açılacak yeni sayfanın adı 
    sh = gc.open(sheet)      #kayıt yapılacak dosyayı aç
    worksheet = sh.add_worksheet(title=ws_title, rows="1", cols="38")      #cihaz adı ve çalışma başlangıç saati isimli yeni sayfa aç

    #başlık hücrelerine başlık listesindeki verileri at
    #!!range içini düşünreke hücrelere veri yazmayı düşün
    cell_list = worksheet.range('A1:AK1')
    i = 0
    for cell in cell_list:      #Hücrelere ayarladığımız verileri yerleştir
        cell.value = table_headers[i]
        i +=1

        
    worksheet.update_cells(cell_list)       #yeni değerlerle sayfayı güncelle
    return ws_title     #açılan sayfanın adını dön



#karttan gelen veriyi calışma sayfası içine saat bilgisi ile birlikte yazma
def log_data(ws_title,data_list):        #ws_title: hangi sayfaya verinin giriliceğini                                                
                                                #data: yazılacak veri
    now = datetime.now()        #şimdiki zamanı al
    time_l = '%s:%s:%s' % (now.hour, now.minute, now.second)        #verinin yazıldığı saat
    day_l = '%s/%s/%s' % (now.day, now.month, now.year)     #verinin yazıldığı gün 
    date="%s %s" % (day_l, time_l)      # veri yazılma saat ve gün
    sh = gc.open("sheet1")      #kayıt yapılacak dosyayı aç
    worksheet = sh.worksheet(ws_title)  #kayıt yapılacak worksheet
    send_data = []
    send_data.append(date)
    i=1
    for data in data_list:
        send_data.append(data)
    worksheet.append_row(send_data)
    













