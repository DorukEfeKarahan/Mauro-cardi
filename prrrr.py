import random

Selam = ["Merhaba", "Selam", "Hoşbuldum", "Hoşgeldim", "Hello"]
Hyra_selam = ["Hoşgeldin", "Merhaba", "Selam", "Naber", "selam"]

Sorular = ["Kupa kasalım mı?", "Nasıl bu kadar geliştin?", "Gel vs atalım mı?", "Hesabım mük olmuş mu?", "Değişmiş mi oyun?"]
Hyra_sorular = ["Bu hesabı ne zaman kurdun?", "İyi oynuyormusun?", "Nerelisin?", "Kaç kupasın?", "Kaç karakterin var?"]

Cevap = ["2025", "Evet", "Türkiye", "6100", "42"]
Hyra_cevap = ["Olur!", "Uzun hikaye...", ":Hazırım ben!", "Olmuş","Evet"]

Market = ["Sandy çok pahalıymış", "XD katlayıcılarından nefret ediyorum!", "Bedava Ultra Sezon kutusu vaaaaaaaaaaaaaar!", "150 taş stın aldım", "Brawl pass plus satın aldım"]
Hyra_market = ["Bende var sandy", "Bende nefret ediyorum", "Yaşasın bee!", "Güzel", "Bende aldım"]

Veda = ["Görüşürüz Hyra", "Hoşçakaaal!", "Bay baaay!", "BAY!", "Bir daha gel!"]
Hyra_veda = ["Görüşürüz!", "Hoşçakal!", "Bay baaaaaaaaaaay!", "BAAAAAAAAAY", "Tamam"]

def chatbot(input_text):
    input_text = input_text.lower()

    for Selam in  Hyra_selam:
        if Selam in input_text:
            return random.choice(Hyra_selam)
        
    for Sorular in  Hyra_cevap:
        if Selam in input_text:
            return random.choice(Hyra_sorular)
        
    for Cevap in  Hyra_cevap:
        if Selam in input_text:
            return random.choice(Hyra_cevap)
        
    for Market in  Hyra_market:
        if Selam in input_text:
            return random.choice(Hyra_market)
    
    for Veda in  Hyra_veda:
        if Selam in input_text:
            return random.choice(Hyra_veda)
        
    return "Anlamadım"

print("Merhaba,  (Çıkış yapmak için 'q' yazın)")
while True:
    user_input = input("Kullanıcı:")
    if user_input.lower() == "q":
        print("Görüşmek üzere")
        chatbot(user_input)
        print("Chatbot:" , Cevap)