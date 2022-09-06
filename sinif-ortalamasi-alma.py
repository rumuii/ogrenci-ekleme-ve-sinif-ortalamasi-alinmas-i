notlar = []
kisi = 0
Ntoplam = 0
ort = 0
while True:
    ogrenci_adi  =str(input("Öğrencinin adiniz giriniz:"))
    ogrenci_adi_soyadi = str(input("Öğrencinin soyadini giriniz:"))
    ogrenci_notu = str(input("Ögrencinin notunu giriniz:"))
    notlar.append(ogrenci_notu)
    print("Öğrencinin Adı Soyadı: {}  {}  Notu: {}".format(ogrenci_adi.title(),ogrenci_adi_soyadi.title(),ogrenci_notu))
    devam = str(input("Eklemeye devam etmek istiyorsanız 'E' ye , ortalama almak istiyorsanız 'H' yaziniz. ").upper())
    devam.upper()
    kisi += 1
    if devam=="H":
        for i in notlar:
            Ntoplam +=int(i)
        print("Sınıf not ortalaması : {}".format(Ntoplam / kisi))
        quit()
    elif devam=="E":
        print("Notu girilen öğrenci sayısı {}".format(kisi))
    else:
        print("Ne yapmak istediğinize karar verin.")
