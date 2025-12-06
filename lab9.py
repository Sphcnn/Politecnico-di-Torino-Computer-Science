''' 1
def main():
    content =[]
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip() 
            content.append(line) 
        try:
            output = open("outputt.txt","w")
            for i,element in enumerate(content):
                output.write(f'/*{i}*/{element} \n')
        except IOError: print("File writing operation has been cancelled.")
        finally: output.close() ; print("File writing operation has been done.")
    except IOError: print("File openning operation has been cancelled.")
    finally: infile.close() ; print("File openning operation has been done.")
    
        
main()
'''

''' 2
def main():
    try:
        content = []
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            content.append(line)
        try:
            output = open("output.txt","w")
            for i in range(len(content)):
                output.write(f'{content[len(content)-i-1]} \n')

        except IOError: print("File writing operation has been cancelled.")
        finally: output.close() ; print("File writing operation has been done.")
        
    except IOError: print("File writing operation has been cancelled.")
    finally: infile.close() ; print("File writing operation has been done.")

main()
'''

''' 3
def main():
    try:
        content = []
        length = 0
        infile = open("input.txt","r",encoding="utf-8")
        for line in infile:
            line = line.rstrip()
            content.append(line)
            length += 1
        try:
            output = open("output.txt","w",encoding="utf-8")
            for i in range(length):
                output.write(f"{content[length-1-i]} \n")
        except IOError: print("Writing file has not been opened")
        finally: output.close() ; print("Writing process has been done")
    except IOError: print("Opening process has been failed")
    finally: infile.close() ; print("Reading process has been done")


main()
'''

"""4
def main():
    fileNames = ["address.txt", "book.txt"]
    addressWords = []
    addressRow = []
    try:
        addressFile = open("address.txt","r")
        for line in addressFile:
            line = line.rstrip()
            addressRow.append(line)
            addressWords.append(line.split())   # << BURAYI DÜZELTTİK
        print(addressRow)
        print("-"*15)
        print(addressWords)
        print("-"*15)
    except IOError:
        print("Address file has not been opened")
    finally:
        addressFile.close()
        print("Operation has done")

    bookWords = []
    bookRows = []
    try:
        bookFile = open("book.txt","r")
        for line in bookFile:
            line = line.rstrip()
            bookRows.append(line)
            bookWords.append(line.split())      # << BURAYI DA DÜZELTTİK
        print(bookRows)
        print("-"*15)
        print(bookWords)
        print("-"*15)
    except IOError:
        print("book file has not been opened")
    finally:
        bookFile.close()
        print("Operation has done")

    word = input("Enter the word you want the search : ").lower()
    fileName = input(f'You should choose a file to search your word in : ({fileNames} : )')

    if fileName == "address.txt":
        index_list = search(word, addressWords)
    elif fileName == "book.txt":
        index_list = search(word, bookWords)
    else:
        print("Invalid file name")
        return

    try:
        output = open("output.txt","w")
        if not index_list:
            output.write(f'"{word}" not found in {fileName}\n')
        else:
            output.write(f'The lines that include \"{word}\" are shown below :\n')
            for i, number in enumerate(index_list):
                if fileName == "address.txt":
                    output.write(f'{i+1}--) {addressRow[number]}\n')
                else:
                    output.write(f'{i+1}--) {bookRows[number]}\n')
    except (IOError, ValueError):
        print("Process has been canceled")
    finally:
        output.close()
        print("Operation has been done succesfuly")  

def search(word: str, element: list):
    index = []
    for i in range(len(element)):
        for token in element[i]:
            clean = token.strip(".,;:!?()[]\"'")
            if clean.lower() == word:
                index.append(i)
                break
    return index

main()
"""

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
