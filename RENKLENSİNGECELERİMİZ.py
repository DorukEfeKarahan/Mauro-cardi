def Dörtkenar_tanımlama(kenar1, kenar2, kenar3, kenar4):
    if kenar1 == kenar2 == kenar3 == kenar4:
        return "Kare"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4 or kenar2 == kenar4 or kenar3 == kenar4:
         return "Dikgörtgen"
    else:
        return "Çeşitkenar Dörtgen"
    
kenar1 = float(input("1.kenar: "))
kenar2 = float(input("2.kenar: "))
kenar3 = float(input("3.kenar: "))
kenar4 = float(input("4.kenar: "))

Dörtkenar_yazdırma = Dörtkenar_tanımlama(kenar1, kenar2, kenar3, kenar4)
print(f"Dörtkenarın çeşidi: {Dörtkenar_yazdırma}")