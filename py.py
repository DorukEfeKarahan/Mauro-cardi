from datetime import datetime

now = datetime.now()
year = now.strftime("%Y")
month = now. strftime("%m")
day = now. strftime("%d")
current_time = now. strftime("%H:%M:%S")
print(f"Anlık zaman:{current_time}")


byear = int(input("Doğum Yılınızı Yazınız: "))
bmonth = int(input("Doğum Ayınızı Yazınız: "))
bname = int(input("Adınızı Yazınız: "))
bday = int(input("Doğum  Gününüzü Yazınız"))
year = int(year)
month = int(month)
day = int(day)


if(byear < year):
    if(bmonth < month):
        if(bname < day):
         x = year - byear
         y = month - bmonth
         z = bname
         d = bday
        print(f"İsmin {z} ve Yaşın {x} ve{y} ve Aylıksın {d}Günsün")
    else:
         x = (year - byear)
         y = (12 -bmonth) + month
         z = bname
         d = bday
         
         print(f"İsmin {z} ve Yaşın {x} ve{y} Aylıksın {d} ve Günün")
else:
    print("Yanlış Bilgi Verdiniz")