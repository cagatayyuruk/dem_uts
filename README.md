# dem_uts
My product seek project at Demirdokum internship.,
İnternet Tabanlı Saha Testi Ürün Takip Sisteminin Kullanılması
Geliştirdiğimiz sistemin kullanılması şu şekilde olmaktadır.
1. Raspberry Pi 3 Model B’nin yapılandırılması
1.1. Raspbian İşletim Sistemi Kurulması
1.1.1. https://www.raspberrypi.org/downloads/ adresinden Raspbian İşletim sisteminin .zip dosyası indirilir.
1.1.2. Kurulumun yapılacağı sd kart bilgisayara takılır. SD kart en az class 6 ve 8Gb kapasiteli olmalıdır.
1.1.3. https://sourceforge.net/projects/win32diskimager/ adresinden win32diskimager programı indirilir ve kurulumu yapılır.
1.1.4. Win32diskimager yazılımı yönetici olarak çalıştırılır.
1.1.5. İndirilen zip dosyası çıkartılır.
1.1.6. İşletim sistemi .image uzantılı dosya win32disk imager ile sd karta yazılır.
1.1.7. Sd kart Raspberry Pi sd kart yuvasına takılır.
1.2. Raspberry Pi üzerine sistem dosyalarının kurulumunun yapılması
1.2.1. Raspberry Pi’ye HDMI, fare ve klavye takılır.
1.2.2. Güç verilerek Raspberry Pi açılır.
1.2.3. Ctrl+Alt+T tuşlarına basılarak terminal açılır
1.2.4. Kullanacağımız modüller indirilir. pip install pyserial pip install --upgrade oauth2client pip install gspread
1.2.5. İnternet Tabanlı Saha Testi Ürün Takip Sistemi dosyaları GitHub Üzerinden indirilir.
2. Sistemin çalıştırılması
2.1. Bağlantıların yapılması
2.1.1. USB-TTL kablosu ürün kontrol kartı üzerinde D4 Portuna bağlanır.
2.1.2. USB-TTL kablosu Raspberry Pi’ye takılır.
2.1.3. Wİ-Fİ bağlantısı yapılır.
2.2. Sistemin Ayarlarının yapılmasuı
2.2.1. dem_uts_conf.py yazılımı ile test ayarları yapılır. python /<dosya_yolu>/dem_uts_conf.py
2.3. Google Drive paylaşım ayarlarının yapılması
2.3.1. Ürün testinin kaydının yapılacağı dosya oluşturulur.
2.3.2. Oluşturulan dosya "demirdokumuts@appspot.gserviceaccount.com" ile paylaşılır.
2.4. Sistemin çalıştırılması
2.4.1. Sistem ana dosyası çalıştırılır python /<dosya_yolu>/dem_uts.py
