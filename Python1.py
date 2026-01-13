from gtts import gTTs
import pygame
import os

TEXT = """
Askerler ilk hedefiniz AKDENİZ İLERİ
"""

OUTPUT_FILE = "Python1.py"

def text_to_voice(text, filename):
    tts =gTTs(text=text, lang="tr")
    tts.save(filename)
    print(f"Ses dosyası oluşturuldu: {filename}")

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

if __name__ == "__main__":
    if TEXT.strip():
        text_to_voice(TEXT , OUTPUT_FILE)
    else:
        print("Metin boş, ses oluşturulamadı.")