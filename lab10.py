""" 1 
def main():
    infile = None
    content = []
    total = 0
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            line1 = []
            for letter in line:
                if letter.isalpha():
                    line1.append(letter)
                    total += 1
                else:
                    line1.append(" ")
            content.append(line1)

    except IOError: print(f"File is not exist")
    finally:
        if infile is not None:
            infile.close()
            print("Reading operation has been done successfuly\n")
        else:
            print("Reading operation has been done successfuly")

    for line in content:
        sentence = "".join(line)
        print(sentence)
main()
"""

""" 2
def main():
    infile = None
    try:
        infile = open("input.txt", "r")
        content = infile.read().split("\n\n")   # boş satıra göre ayır
        content = [stanza.strip() for stanza in content if stanza.strip() != ""]  # boşları temizle
    except IOError:
        print("File does not exist")
        return
    finally:
        if infile is not None:
            infile.close()
            print("Reading operation has been done successfully\n")

    # ters sıraya al
    reversed_content = list(reversed(content))

    try:
        outfile = open("output.txt", "w")
        for stanza in reversed_content:
            outfile.write(stanza + "\n\n")   # kıtalar arasında boş satır bırak
        print("Writing operation has been done successfully\n")
    except IOError:
        print("Output file could not be created")
    finally:
        if outfile is not None:
            outfile.close()

main()
"""
""" 3
def main():
    infile = None
    content = []
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            content.append(line.split())        
    except IOError: print("File does not exist")
    finally:
        if infile is not None:
            infile.close()
            print("Reading operation has been done successfuly\n")
        else:
            print("Reading operation has been done successfuly")

    print(content)
    word = input("Enter the word you want to search : ")
    numWord = countWord(word, content)
    if numWord == 0: print(f'{word} does not exist in this song')
    else: print(f'{word} is found {numWord} times in this song')

    print("The vowel table : ")
    print("-"*15)
    countVowel(content)

def countWord(word:str,lyrics:list)->int:
    counter = 0
    for line in lyrics:
        for element in line:
            if word.lower() == element.lower(): counter += 1
    return counter

def countVowel(lyrics:list):
    VOWELS = {"a":0,
              "e":0,
              "i":0,
              "o":0,
              "u":0}
    
    for key, value in VOWELS.items():
        counter = 0
        for line in lyrics:
            for element in line:
                counter += element.lower().count(key)
        VOWELS[key] = counter
    
    for key, value in VOWELS.items():
        print(f' The vowel \"{key}\" has appeared {value} times')
main()

"""

""" 4
def main():
    infile = None
    content = []
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            content.append(line.split())        
    except IOError: print("File does not exist")
    finally:
        if infile is not None:
            infile.close()
            print("Reading operation has been done successfuly\n")
        else:
            print("Reading operation has been done successfuly")
    
    temp = replacer("jingle","Ring", content)
    outfile = None
    try:
        outfile = open("output.txt","w")
        for line in temp:
            sentence = " ".join(line)
            outfile.write(f'{sentence}\n')

    except IOError: print("File does not exist")
    finally:
        if outfile is not None:
            outfile.close()
            print("Writing operation has been done successfuly\n")
        else:
            print("Writing operation has been done successfuly")
    

def replacer(word1:str, word2:str , lyrics:list) -> list:
    for i,line in enumerate(lyrics):
        for j,element in enumerate(line):
            if element.lower() == word1.lower():
                lyrics[i][j] = word2
    return lyrics
main()
"""

def main():
    infile = None
    content = []
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            words = line.split()   

            cleanWords = []
            for word in words:
                word = word.strip(".,!?;:\"'()[]{}")
                cleanWords.append(word)

            content.append(cleanWords)
            
    except IOError:
        print("File does not exist")
    finally:
        if infile is not None:
            infile.close()
            print("Reading operation has been done successfuly\n")
        else:
            print("Reading operation has been done successfuly")

    # Uzun kelimeleri ayıklayıp yeni içerik üret
    filtered = controler(content)

    outfile = None
    try:
        outfile = open("output.txt","w")
        for line in filtered:
            sentence = " ".join(line)   # kelimeleri araya boşluk koyarak birleştir
            outfile.write(f'{sentence}\n')

    except IOError:
        print("File does not exist")
    finally:
        if outfile is not None:
            outfile.close()
            print("Writing operation has been done successfuly\n")
        else:
            print("Writing operation has been done successfuly")
    

def controler(lyrics:list):
    temp = []
    for line in lyrics:
        new_line = []
        for element in line:
            # 6 harften UZUN olanları çıkar (filter OUT)
            if len(element) <= 6:
                new_line.append(element)
        temp.append(new_line)
    return temp

main()
