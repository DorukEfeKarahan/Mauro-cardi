import random
import string

def Şifre_oluşturucu():
    print("!Şifre Oluşturucuya Hoşgeldiniz!")

    while True:
       try:
           lenght = int(input("Şifrenizin Uzunluğunu Giriniz: (8 - 200): "))
           if lenght < 8 or lenght > 200:
               print("Hata Yaptınız, Bir Daha Yazın. ")
               continue
           
           include_digits = input("Rakamlar dahil edilsinmi? (e/h)").lower() == 'e'
           include_symbols = input("Semboller dahil edilsin mi? (e/h)").lower == 'e'

           characters = string.ascii_letters
           if include_digits:
               characters += string.digits
           if include_symbols:
               characters += string.punctuation

           password = ''.join(random.choice(characters))
           for _ş in range (lenght):
            print(f"Oluşturulan yeni şifreniz {password}")

       except ValueError:
          print("Lütfen gerçek bir sayı giriniz. ")

          play_again = input("Başka bir şifre olşturmak istermisiniz. (e/h)").lower()
          if play_again != 'e':
             print("Şifre oluşturu sonlandırıldı")
             break
          
if __name__ == "__main__":
   Şifre_oluşturucu()






























