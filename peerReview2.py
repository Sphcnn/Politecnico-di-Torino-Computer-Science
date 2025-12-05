def main():
    informations = []
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            informations.append(line.split(";"))

        
        for element in informations:
            print(element)
            print()
        serviceName = []
        
        for i in range(len(informations)):
            serviceName.append(informations[i][1])

        for name in set(serviceName):
            serviceList = []
            serviceList.extend(serviceFinder(name,informations))
            writer(f"output_{name}",serviceList)

    except IOError: print("Openning process has been canceled")
    finally:
        infile.close()
        if informations : print("File operation has been done succesfuly !")
        else: print("File operation has not been done succesfuly !")

def serviceFinder(name:str, records:list):
    elements = []
    for i,element in enumerate(records):
            if records[i][i].lower() == name.lower():
                elements.append(element)
            else: continue
    return elements

def writer(fileName:str , el:list):
    total = 0
    initials = ["Index ","Name ", "Payment ", "Date "]
    try:
        output = open(f"{fileName}.txt","w")
        for word in initials:
            output.write(f'{word:<15} \t')
        output.write(f'\n')    

        for i,element in enumerate(el):
            total += float(el[i][2])
            output.write(f'\n {i}--> \t\t\t\t')
            for j in range(len(el[i])):
                if j == 1: continue
                else: output.write(f'{el[i][j]:<15} \t')

        output.write(f'\n The total income is {total}')
    except IOError: print("Openning process has been canceled")
    finally:
        output.close()
        if total != 0 : print(f"File operation has been done succesfuly for {fileName} !")
        else: print("File operation has not been done succesfuly !")

main()