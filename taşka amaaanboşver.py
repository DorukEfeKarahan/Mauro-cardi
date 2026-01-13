import random
def Taş_Kağıt_Makas():
    choices = ["taş", "kağıt", "makas", "çay", "kuşkonmaz", "pankek"]
    user_choice = input("Taş, Kağıt, Makas, Çay, Kuşkonmaz, Seçeneklerinden birisini seçin").lower()

    if user_choice not in choices:
       print("Hatalı bir seçim yatınız.Tekrar deneyiniz")
       return

    computer_choice = random.choice(choices)
    print(f"Bilgisayarın seçimi: {computer_choice}")

    if user_choice == computer_choice:
        print("berabere")
    elif user_choice == "taş":
        if computer_choice == "kağıt":
            print("ChatGPT kazandı")
        else:
            print("sen kazandın")
    elif user_choice == "kağıt":
        if computer_choice == "makas":
            print("ChatGPT kazandı")
        else:
            print("Sen kazandın")
    elif user_choice == "kağıt":
        if computer_choice == "makas":
            print("ChatGPT kazandı")   
        else: 
         print("Sen kazandın")
    elif user_choice == "makas":
        if  computer_choice == "taş":
               print("ChatGPT kazandı")
        else:
         print("Sen kazandın")
    elif user_choice == "çay":
        if computer_choice == "pankek":
              print("Sen kazandın")
        else:
    elif user_choice == "kuşkonmaz":
        if computer_choice =="taş":
              print("ChatGPT kazandı")
        else:
    elif user_choice == "kuşkonmaz":
        if computer_choice == "makas":
              print("Sen kazandın")
        else:
    elif user_choice == "kağıt":
        if computer_choice == "çay":
              print("ChatGPT kazandın")
        else:
    elif user_choice == "pankek":
        if computer_choice == "taş":
              print("Sen kazandın")
        else:
    elif user_choice == "kuşkonmaz":
        if computer_choice == "pankek":
              print("ChatGPT kazandın")
        else:
    elif user_choice == "pankek":
        if computer_choice == "makas":
              print("Sen kazandın")
              

              print("Taş,kağıt,makasa hoşgeldin")
              Taş_Kağıt_Makas()

