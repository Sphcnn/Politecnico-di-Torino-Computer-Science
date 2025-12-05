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
