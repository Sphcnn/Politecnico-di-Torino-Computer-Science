"""try: 
    words = []
    word_counts = []
    words_list = []
    infile = open("lorem.txt", "r") 
    for line in infile:
        line = line.rstrip()
        if line == "":
            pass
        else:
            splittedList = line.split()
            for element in splittedList:    
                words.append(element.rstrip(",.?!"))
            
except IOError:
    print("No infile named lorem.txt")
    exit()
finally:
    infile.close()

for i,element in enumerate(words):
    if element in words_list:
        word_counts[words_list.index(element)] += 1
    else:
        words_list.append(element)
        word_counts.append(1)

try:    
    output = open("output.txt", "w")
    for i,element in enumerate(words_list):
        output.write(f'{element} : {word_counts[i]}\n')

except IOError:
    print("No file named output")
    exit()
finally:
    output.close()
    print("Execution has been ended and file has been closed !")"""

def main():  
    try:
        infile = open("people.txt","r")
        database = []

        for i, line in enumerate(infile):
            line = line.rstrip()
            content = line.split()
            date = content[-1].split("/")
            database.append(content[:-1])
            database[i].append(date)
        print(database)
        infile.close()
    except IOError:
        print("File could not be opened")
    finally:
        print("Reading operation has been done")

    youngerElement = ["", "", ["1", "1", "0"]]     # en küçük yıl: en yaşlıyı engeller
    elderElement = ["", "", ["1", "1", "9999"]]    # en büyük yıl: en genci engeller

    for element in database:
        youngerElement = younger(element, youngerElement)
        elderElement = elder(element, elderElement)

    try:
        output = open("output2.txt", "w")
        output.write(f'The youngest person is {youngerElement[0]} {youngerElement[1]} who is {age(youngerElement[2])}\n')
        output.write(f'The oldest person is {elderElement[0]} {elderElement[1]} who is {age(elderElement[2])}')
        output.close()
    except IOError:
        print("File could not be opened")
    finally:
        print("Print out operation has been done")


def ageCalculator(element: list):
    return int(element[0]) * 1 + int(element[1]) * 30 + int(element[2]) * 365


def younger(element, referance): 
    # ageCalculator değeri büyükse kişi daha gençtir
    if ageCalculator(element[2]) > ageCalculator(referance[2]): 
        return element
    else: 
        return referance

def elder(element, referance):
    # ageCalculator değeri küçükse kişi daha yaşlıdır
    if ageCalculator(element[2]) < ageCalculator(referance[2]): 
        return element
    else: 
        return referance

def age(element):
    return 2025 - int(element[2])


main()










main()