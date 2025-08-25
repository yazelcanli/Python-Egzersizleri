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
print(metin.index("derslerine"))                 # find fonksiyonundaki gii indeksleme işlevi yapar
print("bu metinin tamamı rakamlardan oluşmuyor".isalnum())  #yazı içerisindeki elemanların tümmü rakam mı sorgulamasını gerçekleştirdik 
print("070707".isalnum())
print("burasıtamamenharfler".isalpha())                     # yazı içerisindeki tüm elemanlar harfler mi
kırtasiye = ("kalem" , "kağıt", "defter", "silgi")
print(kırtasiye)
print(" & ".join(kırtasiye))                    # elemanların arasına bir eleman(lar) eklemek 
print(ülke.lower())                             # metni küçük harfe dönüştürme
araç = "  otomobil  "                           # boşluklar ile bir değişken oluşturma
print(araç.lstrip())                            # boşlukları kırpma işlevi


yanlış_yazı = """aslında mu yazıda yazarken men yanlışlık oldu,
nedense mir kere de değil."""
print(yanlış_yazı)
doğru_yazı = yanlış_yazı.maketrans("m","b")
print(yanlış_yazı.translate(doğru_yazı))
bölme = "elma çok lezzetli"
print(bölme.partition("çok"))                    # metni ilgili ifadeden itibaren bölme yapar
ifade = "İstanbul TÜRKİYE'nin başkentidir."      # yanlış bir ifade girdik 
print(ifade.replace("İstanbul", "Ankara"))       # bir ifadenin değiştirilmesinde kullanılır
tekrar = "su sıcaktı. su içmek istedim. su içemedim" # tekrar eden öğeler yer alan metin girdik
print(tekrar.rfind("su"))                           # aranan ifadenin son geçtiği konumu söyler
print(tekrar.rindex("su"))                           # aranan ifadenin son geçtiği indeksi söyler
satır_bölme = """birici satır
ikinci satır 
üçüncü satır."""                                    # üç satırdan oluşan bir değişken oluşturma
print(satır_bölme)                                  # bu ifadenin çıktısının alınması
print(satır_bölme.splitlines())                     # birden fazla satırı tek bir değişken elemanları yapma


yaren = "benim adım {0} ve benim yaşım {1}".format("yazel", 22)
print(yaren)

harf_değiştirme = "mERHABA bEN aLANYA'DA dOĞDUM"    # büyük ve küçük harflerin ters olduğu bir ifade girdik
print(harf_değiştirme.swapcase())                   # harflerin küçük büyük durumunu tersine çevirdi
başlık = "pyhton derslerine giriş - 1"              # başlık olarak metin girme
print(başlık.title())                               # ilk harflerini büyütme
büyütme = "alanya"                                  # küçük harflerden oluşan bir ifade
print(büyütme.upper())                              # tüm harfleri büyütme
doldur = "50"                                       # sıradan bir değişken ataması
print(doldur.zfill(10))                             # ifadenin başına girilen değere tamamlamak için sıfır ekler

dir(metin)                                          # o değişkene ilişkin işlevleri listeler

print("benim adım yazel" + " ben Alanya doğumluyum")
print("Antalya'nın plaka kodu:" + str(7))          # Sayıyı stringe çevirip birleştir
print("Antalya'nın plaka kodu:" + "07")            #İki stringi birleştir


# Fonksiyonlar

## Tek Argümanlı Fonksiyonlar

def kare_alma(x):                                  # fonklarda çıktının ekrana gelmesi için print kullanılır
    x ** 2

kare_alma(4)                                       # print kullanılmadı ve çıktı ekrana gelmedi 

def kare_alma(x):
    print(x**2)

kare_alma(4)

def kare_alma(x):
    print(str(x) + " karesi alınınca " + str(x**2) + " eder ")   # tümü string ifade ise birleşik çıktı alınabilir
kare_alma(4)
    
## Birden Fazla Argümanlı Fonksiyonlar

def mutlak_fark(x, y):
    print(abs(x - y))
mutlak_fark(8 , 4)

mutlak_fark(  y = 4 , x = 9)                                     # istendiğinde argümanlar belirtilerek yer değişebilir
mutlak_fark(5)                                                  # tek argümanda hata ile karşılaşılır

# Neden Fonksiyonlara İhtiyaç Duyulur
#577/100 = 5
#577/100 = 5.77


# örnek: hız(ortalama), mesafe ve mola değerleri girildiğinde bana varış süresinini saat ve dakika cinsinden verecek bir fonk tasarlayınız
def varış_süresi(hız, mola, mesafe):
    print(str(int((mesafe / hız * 60 + mola) // 60)) +
          " saat " +
         str(round((mesafe/ hız * 60 + mola) % 60)) + 
         " dakika sürer yolculuğunuz.")
    
varış_süresi(90, 75, 420)
varış_süresi(120,30,380)

# Fonksiyonun çıktılarını girdi olarak kullanmak 

def kare_alma(x):                                                 # Bir fonksiyon yazıldı 
    print(x**2)

kare_alma(4)                                                       #Fonksiyon test edildi


# Fonksiyonun çıktısını kullanabilmek için ( GİRDİ OLARAK) RETURN kullanmak gerekir 

def kare_alma(x):
    return(x**2)                                                  # return ile fonksiyon yazıldı

kare_alma(5)*2                                                    # fonksiyon çıktısını girdi olarak kullandık 
    
sonuç = kare_alma(10) * 2                                         # çıktıyı girdi olarak kullanıp bir değişkene kaydetmek
print(sonuç)                                                      # oluşturduğumuz çıktı değişkenini ekrana getirme
sonuç

# Python'da Local ve Global Değişkenler

a = 10
b = 20

# Local Değişkenler İçin Bİr Fonksiyon Tanımlama

def üs_alma(a,b):
    return(a**b)
üs_alma(2,3)
üs_alma( b=2, a=5)                                               # program bizim variable explorer içerisinde yer alan(global değişkenler)
                                                                 # a ve b değerleri olan 10 ve 20 yi kullanmak yerine benim girdiğim değerleri kullandı o değerler Local Değişkenlerdir
                                                                  

# Fonksiyonda kullanılan girdilerin etkiledikleri bölge yalnızca fonksiyonun kendisi ile sınırlıdır
# Görüldüğü üzere variable explorer' dan bağımsız olarak çalıştı 

# Local den Global etki alanına geçiş mümkün müdür

liste = []                                                      # boş bir liste oluşturmak
liste                                                           # listeyi ekrana getirmek 
liste.append(10)                                                # listeye 10 öğesini eklemek
liste.append(25)                                                # listeyi ekrana getirmek
liste

def öğe_eklemek(b):
    liste.append(b)
    print( " liste isimli değişkene "+ str(b) + " öğesi eklendi")

öğe_eklemek(45)

öğe_eklemek(12)
# Append ile bir öğe eklemek istediğimde o öğenin daha önce mutlaka oluşturulmuş olması gerekir.

# Programcılığa girişte koşulların ve kontrollerin kullanılması 

# gerçek hayatımızda her anımızda yaptığımız işi bilgisayarlarla yaptırmaktır

# alçak bir tavan gördüğümüzde eğilmemiz 
# hava soğuksa kalın kıyafet almak 

# Boolean (doğru& yanlış [true 6 false])

sınav_notu= 50
sınav_notu == 50
sınav_notu<50
sınav_notu>50
sınav_notu <=50

# İF 

sınav_notu = 60                                                  # öncelikle belirli bir koşul için sayısal değerli değişken oluşturduk                                                                                                                                                
geçme_notu = 70

if sınav_notu >=  geçme_notu:
    print(" tebrikler sınavı geçtiniz")
    print(str( sınav_notu ) + ">= " + str( geçme_notu ) + "olduğu için geçtiniz")

else:
     print( " dersten maalesef kaldınız ")
     print(" başarılı olmak için daha fazla çalışmanız gerekmektedir ")

    
# Elif birden fazla koşul durumunda elif kullanılır.

# Diyelim ki birden fazla koşul gerektiren bir durumla karşılaştım
# örneğin
# kişinin geliri 0 ile 4250tl arasında ise düşük gelirli 
# kişinin geliri 4251 ile 8500tl arasında ise orta gelirli 
# kişinin geliri 8501tl ve üzeri ise yüksek gelirli olarak belirlensin

gelir = 3600 
if gelir < 4250:
    print( " Düşük gelir düzeyine sahipsiniz")
elif gelir > 4250  and  gelir < 8501:
    print(" Orta gelir düzeyine sahipsiniz ")
else:
    print(" yüksek gelir düzeyine sahipsiniz ")


# Modüllerin kullanılması 

import random 
print(random.randrange( 0, 10))                                 # tek bir rastgele sayı üretimi için kullanılır
print(random.sample(range(0, 10),8))                            # yerine koymadan bir aralıktan veri üretme
print(random.choices(range(0, 10), k = 20))                     # yerine koyarak bir aralıktan veri üretme
print(random.randrange(2,20,2))                                 # belirli bir aralıktan belirli bir artışla tek veri üretmek
print(random.randrange(100, 1000, 3))                           # belirli bir aralıktan belirli basamakta sayı üretme 
print(random.randrange(-50,-5))                                 # negatif aralıktan da veri üretebiliriz
print(random.randint(0 , 100))                                  # tam sayılardan veri üretmek için kullanılır.

# dongüler for döngüsü 

şehirler = ["Ankara", "İstanbul", "İzmir", "Antalya"]

for i in şehirler:
    print(i)


notlar = random.choices(range( 0 , 101), k = 60)
notlar
import statistics
dir(statistics)
for k in notlar:
    print(k-statistics.mean(notlar))
    
notlar[0]-statistics.mean(notlar)


for i in range( 0 , 60):
    print( notlar[i] - statistics.mean(notlar))
    
sapma = []
sapma

for i in range( 0, 60):
  sapma.append(notlar[i] - statistics.mean(notlar))
sapma

# Append kullmak istemiyorsak mutlaka çıktıların aynı boyunca bir boş değişkene ihtiyacım var

import itertools
boş_değişken = list(itertools.repeat( 0, 60))
boş_değişken

for i in range(0 ,60):
    boş_değişken[i] = notlar[i] - statistics.mean(notlar)
    print( " tur sayısı:" + str(i +1))
    
boş_değişken == sapma




# for döngüleri ile birlikte fonksiyonların kullanımı 

# Sorun: Verilen sıcaklık değerlerini çevirmek 
# çözüm : Buna uygun bir fonksiyon tanımı 

def fahrenayt(x):
    return(round((x-32)/(9/5),2))



def santigrat(x):
    return(round((9/5 *  x) + 32,2))

santigrat(21.11)
fahrenayt(70)

ankara = random.choices(range(-10, 10), k=90)   # 90 günlük veri
donusum = []                                     # ortalamadan sapma listesi

for i in range(0, 90):                           # 0..89 (90 eleman)
    donusum.append(ankara[i] - statistics.mean(ankara))

print("İlk 5 sapma:", donusum[:5])





