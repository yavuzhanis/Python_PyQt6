import sqlite3

# camelCase kullandık,dosya varsa bağlandı yoksa yeni dosya oluşturdu connect()
baglanti = sqlite3.connect("ilkVeriTabanım.db")
# tabloya ekleme çıkarma ve üzerinde oynama işlemleri burda yapılır.Cursor()
cursor = baglanti.cursor()


#!TABLO OLUŞTURMA FONKSİYONU :
def tabloOlustur():
    # ? execute ise ne değişiklik yapacağını yaparsın
    # tablo oluşturma cümlesi
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ogrenci(isim TEXT , sehir TEXT ,no INTEGER)")
    baglanti.commit()
    print("Tablo Oluşturuldu")
    #! yukarıda öğrenci içerisinde ise başlıkları girdik
# tabloOlustur()


def veriEkle():
    # tek tırnak içinde eklenen veriler vardır.insert into ise ekleme syntax ı
    cursor.execute("insert into ogrenci values('Fırat' , 'İzmir' , '35')")
    baglanti.commit()
    print("Veri Eklendi")
# veriEkle()
# ? VERİ EKLEME 2.YÖNTEM:


def veriEkle2(isim, sehir, no):
    cursor.execute("insert into ogrenci values(?,?,?)", (isim, sehir, no))
    baglanti.commit()
    print("veri eklendi")
# veriEkle2("Yavuzhan","İzmit","41")


def veriEkle3():
    isim = input("bir isim giriniz: ")
    sehir = input("Bir sehir ismi giriniz: ")
    no = int(input("Plaka giriniz:"))
    cursor.execute("insert into ogrenci values(?,?,?)", (isim, sehir, no))
    baglanti.commit()
    print("Eklendi bea")
# veriEkle3()


def veriEkleListe():
    veri = []
    for i in range(3):
        if i != 2:
            deger = input("Degerleri giriniz: ")
        else:
            deger = int(input("Deger giriniz: "))
        veri.append(deger)
    print(veri)
    cursor.execute("insert into ogrenci values (?,?,?)",
                   (veri[0], veri[1], veri[2]))
    baglanti.commit()
    print("Veri eklendi")
# veriEkleListe()


def veriCek():
    cursor.execute("select * from ogrenci")
    liste = cursor.fetchall()  # veri çekmek için kullanılan fonks.
    for i in liste:
        print(i)
# veriCek()


def veriCek2():
    cursor.execute("select isim , sehir from ogrenci")
    liste = cursor.fetchall()  # veri çekmek için kullanılan fonks.
    for i in liste:
        print(i)
# veriCek2()
def veriCekOzel():
    cursor.execute("select * from ogrenci where sehir = 'İzmir'")
    liste = cursor.fetchall()  # veri çekmek için kullanılan fonks.
    for i in liste:
        print(i)
# veriCekOzel()
def veriGuncelle(isim, sehir):
    cursor.execute(
        "update ogrenci set sehir = ? where isim = ?", (sehir, isim))
    baglanti.commit()
    print("Veri Güncellendi")
#veriGuncelle("Fırat", "Manisa")

def veriSil(isim):
    cursor.execute("delete from ogrenci where isim = ?",(isim,))
    baglanti.commit()
    print("Veri Güncellendi")
#veriSil("Fırat") Veri silme işlemi..

"""
#TODO tablo silme işlemi...
def tabloSil():
    cursor.execute("drop table ogrenci")
    print("Tablo silindi)
tabloSil()
"""