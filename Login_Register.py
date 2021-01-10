print("Kodlama.io'ya hoşgeldiniz!")

Kullanici_adi= ["BariscanKurtkaya","EnginDemirog","MichealJordan1"] #Databaseden çekilen kullanıcı adı (List)
sifre= ["123456789", "Engin1", "1998Bulls"] #Database'den çekilen şifre (List)

k_adi= "" #Kullanıcının gireceği kullanıcı adı (string)
k_sifre= str(0) #Kullanıcının gireceği şifre (string)

def menu(Kullanici_adi,sifre,k_adi,k_sifre): #Kullanıcı için giriş menüsü
  giris=input("Çıkış için 0, Kayit olmak icin 1, Giriş yapmak için 2 yazınız ")

  if(giris=="1"):
    Kayit(Kullanici_adi,sifre,k_adi,k_sifre)
  elif(giris=="2"):
    Kontrol(Kullanici_adi,sifre,k_adi,k_sifre)
  elif(giris=="0"):
    print("Görüşmek Üzere")
  else:
    print("Hatalı sayı girdiniz! Tekrar deneyin")
    menu(Kullanici_adi,sifre,k_adi,k_sifre)
  return

def Kayit(Kullanici_adi,sifre,k_adi,k_sifre): #Kullanıcı kayıt kısmı
  k_adi_new=input("Kullanıcı adınızı giriniz: ")
  k_sifre_new=input("Şifre giriniz: ")
  Kullanici_adi.append(k_adi_new)
  sifre.append(k_sifre_new)
  print("Başarılı şekilde kayıt oldunuz.")
  print("Kullanıcı adınız: " + k_adi_new)
  print("Şifreniz: " + k_sifre_new )
  menu(Kullanici_adi,sifre,k_adi,k_sifre)
  return 


def Kontrol(Kullanici_adi,sifre,k_adi,k_sifre): #Kullanıcı bilgilerini kontrol eden fonksiyon

  dongu_sayisi=0 #For döngüsünün kaç defa döndüğünü bulmak için
  while(k_adi!=Kullanici_adi[dongu_sayisi] or k_sifre != sifre[dongu_sayisi]): #Şifre ve Kullanıcı adı doğru olana kadar dönüyor

    k_adi=input("Kullanıcı adınızı giriniz: ") #Kullanıcı adı girişi
    
    for kullanici in Kullanici_adi:
      if(kullanici==k_adi):
        print("Kullanıcı adınız doğru!")
        for hak in range(3):
          k_sifre=input("Lütfen şifrenizi giriniz: ") #Şifre girişi
          if(k_sifre==sifre[dongu_sayisi]):
            print("Sisteme hoşgeldiniz")
            break
          elif(k_sifre!=sifre[dongu_sayisi] and 2>hak):
            print("Şifreniz yanlış! Kalan Şifre deneme hakkınız: " + str(2-hak))
          else:
            print("Deneme hakkınız bitmiş bulunmakta!")
            menu(Kullanici_adi,sifre,k_adi,k_sifre)
            return

      elif(((len(Kullanici_adi))-1)==dongu_sayisi and kullanici!=k_adi):
        print("Böyle bir kullanıcı bulunmamaktadır. Lütfen kayıt olunuz.")
        menu(Kullanici_adi,sifre,k_adi,k_sifre)
        return

      else:
        dongu_sayisi=dongu_sayisi+1 
    return    
        
    
menu(Kullanici_adi,sifre,k_adi,k_sifre)
