import os
import time

os.system("clear")
satirlar = "abc"
sutunlar = "123"
koordinatlar = []
oynama_sirasi = 1

for x in satirlar:
    for b in sutunlar:
        koordinatlar.append(x+b)
tahta = dict(zip(koordinatlar,(len(koordinatlar)) * "*"))
def tahtayi_goster(tahta):
    print("1 2 3\n")
    for i,z in enumerate(tahta.values()):
        if (i + 1) % 3 == 0:
            print(z,end=" ")
            print(satirlar[int(str(i / 3)[0])])
            print("\n")
            
        else:
            print(z,end=" ")
def kontrol(tahta):
    durumlar = [list({tahta["a1"],tahta["a2"],tahta["a3"]}),
                list({tahta["b1"],tahta["b2"],tahta["b3"]}),
                list({tahta["c1"],tahta["c2"],tahta["c3"]}),
                list({tahta["a1"],tahta["b2"],tahta["c3"]}),
                list({tahta["c1"],tahta["b2"],tahta["a3"]}),
                list({tahta["a1"],tahta["b1"],tahta["c1"]}),
                list({tahta["a2"],tahta["b2"],tahta["c2"]}),
                list({tahta["a3"],tahta["b3"],tahta["c3"]})]
    for i in durumlar:
        if len(i) == 1:
            if i != ["*"]:
                print("{} oyuncusu oyunu kazandı.".format(i[0]))
                tahtayi_goster(tahta)
                return False
            else:
                return True
        else:
            return True

def beraberlik(tahta):
    bos_kare = 0
    for i in tahta.keys():
        if tahta[i] == "*":
            bos_kare += 1
    if bos_kare == 0:
        print("Beraberlik.")
        time.sleep(2)
        return True
    else:
        return False

def sira(oynama_sirasi):
    if oynama_sirasi % 2:
        return "O"
    else:
        return "X"

while kontrol(tahta) and not beraberlik(tahta):
    tahtayi_goster(tahta)
    girilen_koordinat = input("{} oyuncusu için koordinat: ".format(sira(oynama_sirasi))).lower()
    try:
        if tahta[girilen_koordinat] == "*":
            tahta[girilen_koordinat] = sira(oynama_sirasi)
            oynama_sirasi += 1
        else:
            print("Girdiğiniz koordinat dolu.")
            time.sleep(1)
    except KeyError:
        print("Girdiğiniz koordinat yanlış.")
        time.sleep(1)
    os.system("clear")
