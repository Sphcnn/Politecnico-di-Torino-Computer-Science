''' 1
def main():
    word = input("Enter your sentence : ")
    numVowel = count_vowels(word.lower())
    print(f'There are {numVowel} vowel in your word/{word}')
    

def count_vowels(string):
    VOWELS = ["a","e","i","o","u"]
    numVowel = 0
    for i in range(len(string)):
        if string[i] in VOWELS:
            numVowel += 1
        else: pass
    return numVowel

main()
'''

''' 2
def main():
    sentence = input("Enter your sentence : ")
    numWord = count_word(sentence)
    print(f'There are {numWord} word in your sentence/{sentence}')
    

def count_word(string):
    words = string.split(" ")
    return len(words)

main()
'''

''' 3
def main():
    studentName = []
    studentGrade = []
    statement = True
    while statement:
        print("\nChoose an operation:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Count Students")
        print("5. Search Student")
        print("6. Calculate Average Grade")
        print("7. Exit")
        
        chooseOperation(studentName, studentGrade)
        if input("Do you want to perform another operation? (yes/no): ").lower() == 'yes': pass
        else: statement = False


def addStudent(studentName, studentGrade):
    name = input("Enter student name : ")
    grade = float(input("Enter student grade : "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        return
    else: 
        if name in studentName:
            print("Student already exists.")
            return
        else: 
            studentName.append(name)
            studentGrade.append(grade)
            print(f'Student {name} with grade {grade} added.') 
            return

def removeStudent(studentName, studentGrade):
    name = input("Enter student name to remove : ")
    if name in studentName:
        index = studentName.index(name)
        studentName.pop(index)
        studentGrade.pop(index)
        print(f'Student {name} removed.')
    else:
        print(f'Student {name} not found.')

def displayStudents(studentName, studentGrade):
    if not studentName:
        print("No students to display.")
        return
    for i in range(len(studentName)):
        print(f'Student Name: {studentName[i]}, Grade: {studentGrade[i]}')
    return

def countStudents(studentName):
    return len(studentName)

def searchStudent(studentName, studentGrade):
    name = input("Enter student name to search : ")
    if name in studentName:
        index = studentName.index(name)
        print(f'Student Name: {studentName[index]}, Grade: {studentGrade[index]}')
    else:
        print(f'Student {name} not found.')

    return

def calculateAverageGrade(studentGrade):
    if not studentGrade:
        print("No grades available to calculate average.")
        return
    average = sum(studentGrade) / len(studentGrade)
    print(f'Average Grade: {average}')
    return


def chooseOperation(studentName, studentGrade):
    number = int(input("Enter the number of operation you want : "))

    if number == 1:
        addStudent(studentName, studentGrade)
    if number == 2:
        removeStudent(studentName, studentGrade)
    if number == 3:
        displayStudents(studentName, studentGrade)
    if number == 4:
        count = countStudents(studentName)
        print(f'There are {count} students.')
    if number == 5:
        searchStudent(studentName, studentGrade)
    if number == 6:
        calculateAverageGrade(studentGrade)
    if number == 7:
        exit()



main()
'''

''' 4
def main():
    statement = True
    while statement:
        try:
            print("Press Ctrl+C to exit")
            incomeMonthly = float(input("Enter your monthly income : "))
            numChildren = int(input("Enter number of your children : "))
            incomeYearly = incomeMonthly * 12
            benefit = financialBenefit(incomeYearly, numChildren)
            print(f'Your financial benefit is : {benefit} ')
        except KeyboardInterrupt:
            print("\nExiting the program.")
            statement = False


def financialBenefit(income, numChildren):
    if 30000 < income <= 40000 and numChildren >= 3:
        return 1000*numChildren 
    elif 20000 < income <= 30000 and numChildren >= 2:
        return 1500*numChildren
    elif income <= 20000:
        return 2000*numChildren
    else: 
        return 0

main()

'''