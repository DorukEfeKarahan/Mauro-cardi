def Sınav(Bs):
    if Bs >= 100:
       return "Kara Melek Edgar Kazandınız"
    elif Bs >= 50:
      return "Fedai Meg kazandınız"
    elif Bs >= 40:
      return "500 Altın kazandınız"
    elif Bs >= 0:
      return "Bir şey kazanmadınız"

Babapro = int(input("cuguli"))

if Babapro >= 101:
   print("değerin 100'den büyük olamaz")

else:
   ohhhhhh = Sınav(Babapro)
   print (f"notunuz: {ohhhhhh}")