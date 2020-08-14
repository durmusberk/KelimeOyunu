import time
import random

kullanılan_kelimeler = []
pcsonharfler = []
pckullanılankelimeler = []

# DOSYADAKİ KELİMELERİ LİSTE YAPMA KODU
with open('sozluk.txt' , encoding="utf8") as f:
    sozluk1 = f.readlines()
sozluk1 = [x.strip() for x in sozluk1]
    
#  KARAKTERLERİ DEĞİŞTİRME KODLARI
sozluk = []

for string in sozluk1:  
    new_string = string.replace("Ä±", "ı")
    new_string = string.replace("ÅŸ", "ş")
    new_string = string.replace("Ã¼", "ü")  
    new_string = string.replace("Ã§", "ç") 
    new_string = string.replace("Ã¶", "ö")
    new_string = string.replace("ÄŸ", "ğ")
    new_string = string.replace("Ã®", "i")
    new_string = string.replace("Ã¢", "â")
    sozluk.append(new_string)    
    
#OYUNUN BAŞLANGICI   
print("Kelime Türetme Oyunumuza Hoşgeldiniz... Çıkış yapmak için : !çıkış "  )

baslangic = random.choice(sozluk)
sozluk.remove(baslangic)
kullanılan_kelimeler.append(baslangic)
cumle = "Bilgisayarın Seçimi==> {baslangic}".format(baslangic=baslangic)
print(cumle)

pcsonharfler.append(baslangic[-1])
pcsonharf = pcsonharfler[-1]

while True :
    ilkgirdi = input("Oyuncunun Seçimi=====> ")
            
    girdi = ilkgirdi.lower()
    
    if girdi == "" :
        print("Bu olmaz bir daha dene!")
        continue
    
    oyuncusonharf = girdi[-1]
         
    if girdi == "!çıkış" :
        for x in range(0,5):
            b = "Çıkış Yapılıyor" + "." * x
            print (b, end = "\r")
            time.sleep(0.5)
        quit()
     
    elif girdi[0] != pcsonharf :
        print("Bilgisayarın yazdığı kelimenin son harfine dikkat et! ")
        continue
    
    elif girdi in pckullanılankelimeler :
        print("Çakaal bunu bilgisayar yazmıştı... Tekrar dene...")
        continue
    
    elif girdi not in sozluk :
        print("Böyle bir kelime icat edilmedi...")
        continue
            
    elif girdi in kullanılan_kelimeler :
        print("Bunu daha önce yazdın ama yine de sen bilirsin...")
        continue
                                
    kullanılan_kelimeler.append(girdi)
                                                             
    while True :
        randomkelimeilk = random.choice(sozluk)
        randomkelime = randomkelimeilk.lower()
        sozluk.remove(randomkelimeilk)
        kullanılan_kelimeler.append(randomkelime)   
        if randomkelime[0] == oyuncusonharf :
            break    
    cumle = "Bilgisayarın Seçimi==> {randomkelime}".format(randomkelime=randomkelime)
    pcsonharfler.append(randomkelime[-1])
    print(cumle)
    
    pcsonharf = pcsonharfler[-1]
    pckullanılankelimeler.append(randomkelime)
