def main():
    infile = None
    content = []
    studentID = int(input("Enter student ID :"))
    try: 
        infile = open("scores.txt","r")
        for line in infile:
            line = line.rstrip()
            content.append(line.split())
    except IOError: print("Reading operation has been failed")
    finally:
        if infile is not None: infile.close()
        if content: print("Reading operation has been done succesfuly ")
        else: print("Reading operation has not been done succesfuly ")
    summarize(studentID,content)

def summarize(id:int, data:list) -> dict:
    total = 0
    numLesson = 0
    checker = 0
    returnDict = {}
    tempDict = {}
    highScore = 0
    for i in range(len(data)):
            if int(data[i][0]) == id:
                tempDict = {f'{data[i][1]}': int(data[i][2])}
                returnDict.update(tempDict)
                checker += 1
                highScore = int(data[i][2])
    if checker == 0: print("No exam records found for this student.")
    else:
        print(f'Student ID : {id}')
        print(f'{"Course :":<25} {"Score :":<25}')
        for key, value in returnDict.items():
            if value > highScore: highScore = value; highestLesson = key
            else: continue
            print(f'{key+":":<25} {value:<25}')
            numLesson += 1
            total = total + value
        print(f'{"Avarage Score :":<25} {total/numLesson:<25}')
        print(f'{"Highest scoring lesson:":<25} {highestLesson:<25}')
        

main()