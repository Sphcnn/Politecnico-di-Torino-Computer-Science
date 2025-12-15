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


