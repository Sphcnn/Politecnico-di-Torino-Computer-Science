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