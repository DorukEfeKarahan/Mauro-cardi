def üçgen_tanımlama(kenar1, kenar2, kenar3):
    if kenar1 == kenar2 == kenar3:
        return "Eşkenar üçgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        return "İkizkenar üçgen"
    else:
        return "Çeşitkenar üçgen"

kenar1 = float(input("1. kenar: "))
kenar2 = float(input("2. kenar: "))
kenar3 = float(input("3. kenar: "))

üçgen_yazdırma = üçgen_tanımlama(kenar1, kenar2, kenar3)
print(f"Üçgenin çeşidi: {üçgen_yazdırma}")