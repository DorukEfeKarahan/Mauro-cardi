def Password():
    Şifre = "Gumbal"
giriş_hakkı = 3
hak = 0 
while hak < giriş_hakkı:
    user_input = input ("Şifrenizi yazınız:")
    if user_input == Şifre:
        print("Dogrulandı!")
        break
    else:
        print("yanlış Şifre")
        hak += 1
    if hak == 2:
        print("Gum...")
""
if hak == giriş_hakkı:
    print("Erişim geçersiz.")

    print("Password'a hoşgeldiniz")
    Password()