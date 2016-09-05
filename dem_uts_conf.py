# -*- coding: utf-8 -*-
#"Demirdöküm İnternet Tabanlı Saha Testi Ürün Takip Sistemi" 
#test ayar yazılımı

import json

#New test configuration input function
def start_new():
    test_name="test1"
    device_name =raw_input('Test yapılan cihaz numarasını giriniz (örn: cihaz1) :')
    status= raw_input('Testi aktif etmek için "1" pasif etmek için "0" giriniz :')
    port=raw_input('Cihazın bağlandığını portu giriniz (portları görmek için \
    terminalden "dmesg | grep tty" komutu kullanınız (örn: /dev/ttyUSB0)) :')

    test_status = {}
    test_status[test_name] = {
        'device_name' : device_name,
        'status' : status,
        'port' : port
        }


    s=json.dumps(test_status)
    with open("test_stat.txt","w")as f:
        f.write(s)
        f.close()
    print('Ayarlar tamamlandı.')
#Current Test Status Change function
def change_status():
    with open("test_stat.txt","r")as f:
        d=f.read()
    test=json.loads(d)
    #test durumuna string atanması
    if test['test1']['status']== u'1':
        status_c = 'Test Aktif'
    else:
        status_c = 'Test Pasif'
    port_c = test['test1']["port"]
    name_c = test['test1']['device_name']
    print ("Şimdiki ayarlar:")  
    print port_c
    print name_c
    print status_c
    status_change = raw_input("Yeni test durumunu giriniz: (devam/bitir)")
    if status_change == "devam":
        test['test1']['status']= u'1'
    else:
        test['test1']['status']= u'0'
    s=json.dumps(test)
    with open("test_stat.txt","w")as f:
        f.write(s)
    f.close()
      
#Main Program   
print ("Demirdöküm İnternet Tabanlı Saha Testi Ürün Takip Sistemi v 0.05")
conf_stat = raw_input("Yeni test başlatmak istiyor musunuz? (E/H)")
if conf_stat=='E':
    start_new()
elif conf_stat =='H':
    change_status()
else:
    print ("Yanlış girdiniz!")
    

