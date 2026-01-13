def Herşeyi_tanımlama(kenar1, kenar2, kenar3, kenar4, kenar5, kenar6):
    if kenar1 == kenar2 == kenar3 == kenar4 == kenar5 == kenar6:
        return "Eşkenar Altıgen"
    elif  kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4 or kenar1 == kenar5 or kenar2 == kenar5 or kenar3 == kenar5 or kenar4 == kenar6 or kenar1 == kenar6 or kenar2 == kenar6 or kenar3 == kenar6 or kenar4 == kenar6 or kenar5 == kenar6:
          return "İkizkenar altıgen"
    elif  kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4 or kenar1 == kenar5 or kenar2 == kenar5 or kenar3 == kenar5 or kenar4:
         return "Çeşitkenar altıgen"
    if  kenar1 == kenar2 == kenar3 == kenar4 == kenar5:
       return "Eşkenar beşken"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4 or kenar1 == kenar5 or kenar2 == kenar5 or kenar3 == kenar5 or kenar4:
         return "İkizkenar beşken"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4:
        return "Kare"
    if  kenar1 == kenar2 == kenar3 ==kenar4:
        return "eşkenar dörtgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4:
         return "Dikgörtgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:

   

        return "Eşkenar üçgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        return "İkizkenar üçgen"
    else:
        return "Çeşitkenar üçgen"
kenar1 = float(input("1.kenar: "))
kenar2 = float(input("2.kenar: "))
kenar3 = float(input("3.kenar: "))
kenar4 = float(input("4.kenar: "))
kenar5 = float(input("5.kenar: "))
kenar6 = float(input("6.kenar: "))

Herşeyi_yazdırma = Herşeyi_tanımlama(kenar1, kenar2, kenar3, kenar4, kenar5, kenar6)
print(f"Şeklin çeşidi: {Herşeyi_yazdırma}")