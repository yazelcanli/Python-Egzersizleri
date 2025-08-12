#Temel Python Eğitimi Başlıyorr

#Birinci Kodumuzu Çalıştıralım

print("Merhaba kod dünyası artık ben de varım!")

#Python'da yorum yapmak ve açıklama yazmak için # işareti kullanılır.

# değişken atama işlemi 

x = 8
ülke = "Türkiye Cumhuriyeti"


bir, iki, üç = 1, 2, 3            #birden fazla değişkene farklı değerler atamak

mavi = yeşil = kırmızı = "renk"   #birden fazla değiişkene aynı değeri atamak 

# Aritmetik Operastörler

8 * 4                             #çarpma operatörü
8 / 4                             #bölme operatörü
8 + 4                             #toplama
8 - 4                             #çıkarma
2 ** 3                            #üs alma
9 % 2                             #mod(bölmede kalan)
9 // 2                            #tam sayılı bölme operatörü

# değişken değiştirme operatörleri 

x += 3                            #kayıtlı olan değişkene değer eklemek
x -= 3 
x /= 2 
x *=2
print(x)

#mantıksal sorgulamalar

x > 5                              # değişken değerden büyük mü 
x < 5
x >= 5                             #değişken değerden büyük ya da eşit mi
x <=5
x == 5                              #eşit
x != 5                              #eşit değil
5  is 5                             # eşit
5 is not 6
"T" in ülke                         #değişken içerisinde değer varlığını sorgulamak 
"k" not in ülke

#Phyton'da kullanılan veri türleri

yazı = "harflerden oluşur"          #str (karakterler)
tam_sayı = 23                         #int (tam sayılar)
ondalık_sayı = 3.14                   #float(ondalıklı sayılar)
kompleks_sayı = 1j                    #complex (kompeks sayılar)
liste = ["kırmızı","sarı", "mavi", "turuncu"] #list(liste)
demet = ("gül",  "karanfil", "papatya")        #tuple(demet,değişken grubu)
sözlük = {"ülke" : "türkiye" , "başkent" : "ankara"}    #dic(sözlük)
grup = {"elma" , "karpuz" , "muz"}                     #set(grup)
mantıksal = True                                      #bool(mantıksal)
bayt = b"merhaba"                                     #byte(bayt)
bayt_dize = bytearray(5)                              #byterray(byte dize)
type(bayt_dize)                                  #memoryview(hafıza görünümü, ver,mli kullanım)


 # değişkenin elemanlarına erişmek ( phyton'da indiksleme SIFIRDAN başlar)

 # değişkenin tümünü çağırmak
yazı                                             #değişkenin adı ile tamamı çağrılır                                        
tam_sayı
ondalık_sayı
kompleks_sayı

 # değişken içerisinden eleman çağırmak 

liste[0]                                       #liste elemanına köşeli parantez ile erişilir
liste[1]
liste[2]
liste[3]
demet[0]                                       #demet elemanına köşeli parantez ile erişilir
demet[1]
demet[2]
sözlük                                          #sözlükte değişkenin ismi ile hem anahtar hem ifade gelir
sözlük["ülke"]                                  #sözlükte köşeli parantez içerisine "anahtar" değer yazılır
sözlük["başkent"]
liste
yeni_liste = ["ilk", "ikinci", "üçüncü" , liste] # iç içe listeler ve demetler oluşturulabilir
yeni_liste[0]
yeni_liste[1]
yeni_liste[2]
yeni_liste[3]
yeni_liste[3][0]                                # liste içeirisindeki listelelerin  elemana çift köşeli parantez ile erişir

# slice işlemleri ile elemanlara erişmek 

liste[0:2]                                      # lite elemanlarına aralık olarak erişmek ('e kadar)
liste[:2]
liste[1:]                                      # lite elemanlarına aralık olarak erişmek (elemandan başlamak üzere)                                      
liste[1:3]

 # karakter işlevleri
 
ülke = "turkiye Cumhuriyeti"                   #ilk harfi küçük olan bir metin değişkeni oluşturduk
print(ülke)                                    #ülke değişkeninin çıktısını alma
print(ülke.capitalize())                        # ilk harfi büyütme işlevi ikinci kelime tamamen küçük oldu 
print(ülke.casefold())                          # Tamamı küçük harfe dönüştürme
print(ülke.center(40, "."))                     #metni ilgili karakter sayısına arttırma ve ortalama 

metin = """Python derslerine başladım
Python aslında öğrenmesi zor bir dil değil 
Python öğrenmesi çok keyifli."""                # üç tırnak arasına irden fazla satır yazılabilir

print(metin)                                    # çıktıyı kodlar olmaksızın almak ( kodlar arasındaki değişkenler /n gini gözükmeden)
print(metin.count("python"))                    # metin içerisinde geçen kelimeyi saydırma 
print(metin.endswith("."))                      # metin bu ifade ile bitiyor mu
print(metin.find("dil"))                        # metin içerisinde geçen ifadenin konumunu bulmak.
ekmek = "ekmek sadece {fiyat:.2f} Türk Lirası!"
print(ekmek.format(fiyat = 4.5))                # değiştirilebilir öğe için format işlevi kullanılır

# örnekler 
ad = "benim adım {kişi_adı}, {kişinin_yaşı} yaşındayım.".format(kişi_adı = "kuzey" , kişinin_yaşı = "11")
print(ad)


YER = "benim memleketim {kişinin_memleketi} ve ben orayı çok seviyorum herkes bunu bilsin".format(kişinin_memleketi = "ALANYA")
print(YER)

yer = "benim doğum yerim {0}, doğum yılım ise {1}".format("ankara", 1980)
print(yer)

benim_denemem_yer = "benim doğum yerim {0} , doğum yılım ise {1}".format("ALANYA", 2002)
print(benim_denemem_yer)

benim_denemem_2 = "benim ingilizce seviyem {0} amacım yaz sonuna kadar ingilizce seviyemi {1}  yapmak".format("B1", "B2")
print(benim_denemem_2)

ısı = "saat {} ve hava {} santigrat derece".format("14.33" , 23 )
print(ısı)
print(metin.index("derslerine"))

