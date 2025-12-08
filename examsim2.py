def main():
    infile = None
    content = []
    studentID = int(input("Enter student ID: "))
    try:
        infile = open("scores.txt", "r")
        for line in infile:
            line = line.rstrip()
            if line == "":
                continue
            content.append(line.split())
    except IOError:
        print("Reading operation has been failed")
    finally:
        if infile is not None:
            infile.close()
        if content:
            print("Reading operation has been done succesfuly")
        else:
            print("Reading operation has not been done succesfuly")

    summarize(studentID, content)


def summarize(id: int, data: list) -> None:
    returnDict = {}
    # ilgili öğrencinin derslerini topla
    for row in data:
        if int(row[0]) == id:
            course = row[1]
            score = int(row[2])
            returnDict[course] = score

    if not returnDict:
        print("No exam records found for this student.")
        return

    print(f"Student ID: {id}")
    print(f'{"Course :":<25} {"Score :":<25}')

    total = 0
    numLesson = 0
    highScore = -1
    highestLesson = ""

    for course, score in returnDict.items():
        print(f"{course + ':':<25} {score:<25}")
        total += score
        numLesson += 1

        if score > highScore:
            highScore = score
            highestLesson = course

    print(f'{"Average score :":<25} {total / numLesson:<25}')
    print(f'{"Highest scoring course:":<25} {highestLesson:<25}')


main()
