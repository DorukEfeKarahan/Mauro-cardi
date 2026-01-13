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
