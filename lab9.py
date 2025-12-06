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

main()"""

""" 5
def main():
    lessons = []
    results = {}
    studentID = int(input("Enter the student ID: "))

    infile = None
    try:
        infile = open("classes.txt", "r")
        for i, line in enumerate(infile):
            line = line.strip()
            lessons.append(line)
    except IOError:
        print("Opening process has been canceled")
    finally:
        if infile is not None:
            infile.close()
        if lessons:
            print("Reading operation has been done succesfuly")
        else:
            print("File has not been opened succesfuly")

    results.update(gradeWriter(studentID, lessons))
    infoGiver(studentID, results)


def gradeWriter(studentID: int, lessons: list):
    grades = {}
    for lesson in lessons:
        lessonFile = None
        try:
            lessonFile = open(f"{lesson}.txt", "r")
            for line in lessonFile:
                line = line.strip()
                if not line:
                    continue
                content = line.split()  # StudentID Grade
                if int(content[0]) == studentID:
                    grades[lesson] = content[1]
        except IOError:
            print(f"{lesson}.txt could not be opened")
        finally:
            if lessonFile is not None:
                lessonFile.close()
    return grades


def infoGiver(studentID: int, results: dict):
    print(f"Student ID: {studentID}")
    for key, value in results.items():
        print(f"{key} {value}")


main()
"""

def main():
    bondData = {}
    bonds = []
    information = []
    try:
        infile = open("bond_data.txt")
        for line in infile:
            line = line.rstrip()
            temp = []
            temp.append(line.split(" "))
            bonds.append(temp[0][0])
            print(temp)
            information.append(temp[0][1:])
    except IOError: pass
    
    for i,element in enumerate(bonds):
        tempDict = {f"{element}":information[i]}
        bondData.update(tempDict)
    print(bondData)
    bond = input("Write the bonding chemicals as X|X or X||X or X|||X : ")
    converter(bond, bondData)

def converter(bond:str, bondData:dict):
    for key,value in bondData.items():
        if key.strip().lower() == bond.strip().lower():
            print(f'The bond\'s({bond}) length is {bondData[key][0]} and this bond\'s energy is {bondData[key][1]}')


main()