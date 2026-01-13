def remove_punctuation(text:str, remove_space: bool = False) -> str:
    import string
    punctuation = string.punctuation

    result = "" 
    for char in text:
        if char not in punctuation:
            result += char
    if remove_space:
        result = result.replace(" ","")

    if remove_space:
        result = result.replace("Q","q")

    if remove_space:
        result = result.replace("W","w")

    if remove_space:
        result = result.replace("E","e")

    if remove_space:
        result = result.replace("R","r")

    if remove_space:
        result = result.replace("T","t")

    if remove_space:
        result = result.replace("Y","y")

    if remove_space:
        result = result.replace("U","u")

    if remove_space:
        result = result.replace("I","ı")

    if remove_space:
        result = result.replace("O","o")

    if remove_space:
        result = result.replace("P","p")

    if remove_space:
        result = result.replace("Ğ","ğ")

    if remove_space:
        result = result.replace("Ü","ü")

    if remove_space:
        result = result.replace("A","a")

    if remove_space:
      result = result.replace("D","d")

    if remove_space:
        result = result.replace("F","f")

    if remove_space:
        result = result.replace("G","g")

    if remove_space:
        result = result.replace("H","h")

    if remove_space:
        result = result.replace("J","j")

    if remove_space:
        result = result.replace("K","k")
    if remove_space:
        result = result.replace("L","l")

    if remove_space:
        result = result.replace("Ş","ş")

    if remove_space:
        result = result.replace("İ","i")

    if remove_space:
        result = result.replace("Z","z")

    if remove_space:
        result = result.replace("X","x")

    if remove_space:
        result = result.replace("C","c")

    if remove_space:
        result = result.replace("V","v")

    if remove_space:
        result = result.replace("B","b")

    if remove_space:
        result = result.replace("N","n")

    if remove_space:
        result = result.replace("M","m")

    if remove_space:
        result = result.replace("Ö","ö")

    if remove_space:
        result = result.replace("Ç","ç")