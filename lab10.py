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

""" 5
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
"""

def main():
    infile = None
    content = []

    try:
        infile = open("cs1.6.csv","r")
        infile.readline()
        for line in infile:
            line = line.rstrip()
            content.append(line.split(","))

    except IOError: print("File does not exist")
    finally:
        if infile is not None: infile.close(); print("Reading operation has been done successfuly")
        else: print("Reading operation has been canceled")
        if not content: print("File is empty")

    pistolDict = classification("Pistol",content)
    shotgunDict = classification("Shotgun",content)
    machinegunDict = classification("Machinegun",content)
    smgDict = classification("SMG",content)
    rifleDict = classification("Rifle",content)
    sniperifleDict = classification("SniperRifle",content)
    semiautosniperDict = classification("Semi-autoSniper",content)
    
    print(pistolDict)
    print(pistolDict)
    cost(3500, content)

    print(f'The avarage cost of Pistols : {avarage(pistolDict)}')
    print(f'The avarage cost of Shotguns : {avarage(shotgunDict)}')
    print(f'The avarage cost of Machineguns : {avarage(machinegunDict)}')
    print(f'The avarage cost of SMGs : {avarage(smgDict )}')
    print(f'The avarage cost of Rifles : {avarage(rifleDict )}')
    print(f'The avarage cost of Sniper Rifles : {avarage(sniperifleDict )}')
    print(f'The avarage cost of Semi-auto Snipers : {avarage(semiautosniperDict )}')


    game(pistolDict , shotgunDict, machinegunDict,smgDict,rifleDict,
         sniperifleDict,semiautosniperDict,800)
    

def classification(name:str, menu:list) -> dict:

    returnDict = {}
    for i in range(len(menu)):
        tempDict = {}
        tempList = []
        if menu[i][0].lower() == name.lower():
            tempList.append(menu[i][2])
            tempList.append(menu[i][3])  
            tempDict = {f'{menu[i][1]}' : tempList}
            returnDict.update(tempDict)

    return returnDict


def cost(threshold:int, menu:list):
    returnList = []
    for i in range(len(menu)):
        tempList = []
        if int(menu[i][2]) >= 3500:
            tempList.append(menu[i][1])
            tempList.append(menu[i][2])
            returnList.append(tempList)
    
    print("Guns which are expensive than 3500")
    print("-"*15)
    print(f'{"Gun :":<15}\t {"Price:":<15}')
    for i in range(len(returnList)):
            print(f'{returnList[i][0]:<15}\t {returnList[i][1]}')

def avarage(menu:dict) -> float:
    total = 0
    for key, value in menu.items():
        total += int(value[0])
    average = total / len(menu)
    return average


def game(pistolDict:dict , shotgunDict:dict, machinegunDict:dict,
         smgDict:dict,rifleDict:dict,sniperifleDict:dict,semiautosniperDict:dict, money:int):
    gunMenuDict = {1:pistolDict,    
                   2:shotgunDict,
                   3:machinegunDict,
                   4:smgDict,
                   5:rifleDict,
                   6:sniperifleDict,
                   7:semiautosniperDict}
    money = 800
    round = 1
    while round < 16:
        menuSelect = int(input(f'ROUND {round}. Select gun menu (1-Pistol, 2-Shotgun, 3-Machinegun, 4-SMG, 5-Rifle, 6-SniperRifle, 7-Semi-autoSniper): '))
        if menuSelect in gunMenuDict:
            print(f'{"Gun":<20} {"Price":<10} {"Damage":<10}')
            print("-"*40)
            for key, value in gunMenuDict[menuSelect].items():
                print(f'{key:<20} {value[0]:<10} {value[1]:<10}')
            print(f'You have {money} money')
        else: print("Invalid menu selection")
        
        gunSelect = input("Select the gun you want to buy (Press q to return previous menu): ")
        while gunSelect == "q":
            menuSelect = int(input(f'ROUND {round}. Select gun menu (1-Pistol, 2-Shotgun, 3-Machinegun, 4-SMG, 5-Rifle, 6-SniperRifle, 7-Semi-autoSniper): '))
            if menuSelect in gunMenuDict:
                print(f'{"Gun":<20} {"Price":<10} {"Damage":<10}')
                print("-"*40)
                for key, value in gunMenuDict[menuSelect].items():
                    print(f'{key:<20} {value[0]:<10} {value[1]:<10}')
                print(f'You have {money} money')
            else: print("Invalid menu selection")
            gunSelect = input("Select the gun you want to buy (Press q to return previous menu): ")
        if gunSelect not in gunMenuDict[menuSelect]:
            print("Invalid gun selection")
        elif int(gunMenuDict[menuSelect][gunSelect][0]) > money:
            print("You don't have enough money to buy this gun")
        else:
            money -= int(gunMenuDict[menuSelect][gunSelect][0])
            print(f'You bought {gunSelect} which costs {gunMenuDict[menuSelect][gunSelect][0]} damages {gunMenuDict[menuSelect][gunSelect][1]} and you have {money} left')
        kills = int(input("Enter the number of kills you made this round : "))
        money += kills * 300
        if input("Did you die this round? (y/n): ").lower() == 'y':death = True 
        else: death = False
        if death:
            money -= 500
            print(f'You died this round and lost 500. You have {money} left')

        round += 1


main()

