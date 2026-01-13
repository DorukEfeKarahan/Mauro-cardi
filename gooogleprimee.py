import webbroser


def search_Youtube():
    print("\n ------ Youtube anahtar kelimeyi aratma -----")
    keyword = input("Anahtar kelimeyi kullan. ").strip()

    invalid_chars = [',', '.', "'", '/', '[', ']', '{', '}',', ', ';']
    if any(char in keyword for char in invalid_chars):
        print("invalid karekter kullanildi, tekrar deneyin")
        return
    url = f"https://www.youtube.com/results?search_query={keyword}"
    print(f"aram yapiliyor youtubede: {keyword}")
    print(f"sayfa açılıyor: {url}\n")

    webbroser.open(url)
def main():
    while True:
        print("1 yutupta arama yap")
        print("2 exit")
        choice = input("birisini seçin")
        if choice == "1":
            search_Youtube()
        elif choice == "2":
            print("bay bay")
            break
        else:
            print("yanlış bir seç")
            enek seçtiniz.")
if __name__ == "__main__":
    main()