def not_getir(score):
    if score >= 90:
        return "Baklava ve lahmacun kazandınız"
    elif score >= 80:
        return "Pide ve Kadayıf kazandınız"
    elif score >= 70:
        return "Hindistan cevizi ve Hindistan sokak lezzeti kazandınız"
    elif score >= 60:
        return "Nükleerli İsrail Yemeği kazandınız"
    else:
        return "Kaldı"
    
kullanıcı_not = int(input("notunuzu giriniz"))

if kullanıcı_not >= 101: 
    print("notunuz 100'den büyük olamaz")

else:
    notlar = not_getir(kullanıcı_not)
    print(f"notonuz: {notlar}")