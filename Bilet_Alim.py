import os
import time
import datetime

print("""
      #######################################
      BİLET REZERVASYON SİSTEMİNE HOŞGELDİNİZ
      #######################################
      """)

def firmalar():
    
    print("1- METRO TURİZM")
    print("2- KAMİL KOÇ")
    print("3- PAMUKKALE")
    print("4- ULUSOY")
    print("5- SİNOP BİRLİK")
   
def databasebilgialma():

    firmalar()

    f = input(" Hangi Firma için rezervasyon yapılacak? : ")
    if f == "1":
        f = "METRO TURİZM\\"
        print("""
        Seferler:
        İstanbul-Ankara: 20:00 - 21:00 - 22:00 - 23:00 
        Ankara-İstanbul: 20:30 - 21:30 - 22:30 - 23:30
              """)
        return f
    else:
        pass

    if f == "2":
        f = "KAMİL KOÇ\\"
        print("""
        Seferler:
        İstanbul-Ankara: 20:00 - 21:00 - 22:00 - 23:00 
        Ankara-İstanbul: 20:30 - 21:30 - 22:30 - 23:30
              """)
        return f
    else:
        pass

    if f == "3":
        f = "PAMUKKALE\\"
        print("""
        Seferler:
        İstanbul-Ankara: 20:00 - 21:00 - 22:00 - 23:00 
        Ankara-İstanbul: 20:30 - 21:30 - 22:30 - 23:30
              """)
        return f
    else:
        pass

    if f == "4":
        f = "ULUSOY\\"
        print("""
        Seferler:
        İstanbul-Ankara: 20:00 - 21:00 - 22:00 - 23:00 
        Ankara-İstanbul: 20:30 - 21:30 - 22:30 - 23:30
              """)
        return f
    else:
        pass

    if f == "5":
        f = "SİNOP BİRLİK\\"
        print("""
        Seferler:
        İstanbul-Ankara: 20:00 - 21:00 - 22:00 - 23:00 
        Ankara-İstanbul: 20:30 - 21:30 - 22:30 - 23:30
              """)
        return f
    else:
        pass

    

def tarihklasör():

    b = "A:\\python projeler\\Bilet_Alım_Sistemi\\Bilet_Alim_Text\\"

    tarih = time.strftime('%d-%m-%Y/')

    yol = b + f + tarih + "database.log"

    kontrolyol = os.path.dirname(yol)
    if not os.path.exists(kontrolyol):
        os.makedirs(kontrolyol)

    return yol

def yolcubilgilerivelog():

    an = datetime.datetime.now()
    ansaat = an.hour
    andakika = an.minute


    isim = input("Yolcu İsmi: ")
    soyisim = input("Yolcu Soyismi: ")
    doğumtrh = input("Yolcu Doğum Tarihi: ")
    neredennereye = input("İstikamet Nereden - Nereye: ")
    sefersaati = input("Sefer Saati: ")
    koltukno = input("Koltuk No: ")
    
    if len(doğumtrh) != 10:
        os.system("cls")
        print("Doğum Tarihi Hatalı")
        doğumtrh = input("Yolcu Doğum Tarihi: ")

    else:
        pass

    TC = input("Yolcu TC Kimlik Numarası: ")

    if len(TC) != 11:
        os.system("cls")
        print("TC Kimlik Numarası Hatalı")
        

    else:
        pass

    dosya =open(yol,"a",encoding="utf8")
    dosya.write("\n----------------------------\n")
    dosya.write("Yolcu Kayıt Saati : ")
    dosya.write(str(ansaat))
    dosya.write(":")
    dosya.write(str(andakika))
                
    dosya.write("\n")
    dosya.write("Yolcu İsmi : ")
    dosya.write(isim + '\n')
    dosya.write("Yolcu Soyismi : ")
    dosya.write(soyisim + '\n')
    dosya.write("Yolcu Doğum Tarihi : ")
    dosya.write(doğumtrh + '\n')
    dosya.write("Yolcu TC Numarası : ")
    dosya.write(TC + '\n')
    dosya.write("İstikamet Nereden - Nereye : ")
    dosya.write(neredennereye + '\n')
    dosya.write("Sefer Saati : ")
    dosya.write(sefersaati + '\n')
    dosya.write("Koltuk No : ")
    dosya.write(koltukno + '\n')
    dosya.write("----------------------------")
    dosya.close()



while True:
    os.system("cls")
    f = databasebilgialma()
    yol = tarihklasör()
    yolcubilgilerivelog()
