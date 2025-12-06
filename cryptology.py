import string

def main():
    keyFileName = input("Enter the name of the keyword file: ")
    keyword = ""

    keyfile = None
    try:
        keyfile = open(keyFileName, "r")
        keyword = keyfile.readline().strip()  
    except IOError:
        print("Keyword file could not be read")
        return
    finally:
        if keyfile is not None:
            keyfile.close()

 
    letterScript = build_letter_script(keyword)

    letters = []
    infile = None
    try:
        infile = open("input.txt", "r")
        char = infile.read(1)
        while char != "":
            letters.append(char)
            char = infile.read(1)
    except IOError:
        print("Reading process has been canceled")
    finally:
        if infile is not None:
            infile.close()
        if letters:
            print("Reading operation has been done succesfuly")
        else:
            print("Operation has not been successful")

    if not letters:
        return

    encryptedLetters = encrypted(letters[:], letterScript)
    sentence1 = "".join(encryptedLetters)

    decryptedLetters = decrpyted(encryptedLetters[:], letterScript)
    sentence2 = "".join(decryptedLetters)

    output = None
    try:
        output = open("output.txt", "w")
        output.write(sentence1 + "\n")
        output.write(sentence2 + "\n")
    except IOError:
        print("Writing process has been canceled")
    finally:
        if output is not None:
            output.close()
        if letters:
            print("Writing operation has been done succesfuly")
        else:
            print("Operation has not been successful")

def build_letter_script(keyword: str) -> dict:
    keyword = keyword.upper()
    unique_letters = []
    for ch in keyword:
        if ch.isalpha() and ch not in unique_letters:
            unique_letters.append(ch)

    for ch in reversed(string.ascii_uppercase):  #Add from Z to A
        if ch not in unique_letters:
            unique_letters.append(ch)

    letterScript = {}
    for i, ch in enumerate(string.ascii_uppercase):
        letterScript[ch] = unique_letters[i]

    return letterScript


def encrypted(letters: list, letterScript: dict):
    for i in range(len(letters)):
        letter = letters[i]
        if letter.isalpha():
            if letter.isupper():
                letters[i] = letterScript[letter]
            else:
                temp = letterScript[letter.upper()]
                letters[i] = temp.lower()
    return letters


def reverseDict(searched, letterScript):
    for key, value in letterScript.items():
        if value == searched:
            return key


def decrpyted(letters: list, letterScript: dict):
    for i in range(len(letters)):
        letter = letters[i]
        if letter.isalpha():
            upLetter = letter.upper()
            if letter.isupper():
                letters[i] = reverseDict(upLetter, letterScript)
            else:
                letters[i] = reverseDict(upLetter, letterScript).lower()
    return letters


main()
