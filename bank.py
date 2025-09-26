#Bankamatik
SerkayHesap = {
    "ad" : "Serkay Karakaya",
    "hesapNo" : "12345678",
    "bakiye" : 3000,
    "ekHesap" : 2000,
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap["bakiye"] >= miktar) :
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsinz")
    else :
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanımı = input("ek hesap kullanılsın mı (e/h): ")
            if ekHesapKullanımı == "e":
                ekHesapKullanılcakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanılcakMiktar
                print("paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} vardır.")  
        else :
            print("bakiye yetersiz")

paraCek(SerkayHesap,5000)
paraCek(SerkayHesap,5000)