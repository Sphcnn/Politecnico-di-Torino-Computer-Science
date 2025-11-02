#Exercises of Lab3
''' 1
VALID_CHARS = set('ACTG')

longSequence = input("Enter the chain of DNA as only A,C,T,G : ")
letter=""
if set(longSequence).issubset(VALID_CHARS):
    pass
else:
    print("Enter a valid DNA sequence.")
    longSequence=input("Try again use only (A,C,T,G) : ")
shortSequence = input("Enter a short part of DNA that you are looking for : ")

if set(shortSequence).issubset(VALID_CHARS):
    pass

else:
    print("Enter a valid DNA sequence.")
    shortSequence=input("Try again use only (A,C,T,G) : ")

isPart=shortSequence in longSequence

if isPart:
    
    print(f'Yes your piece of DNA {shortSequence} is part of {longSequence} for {longSequence.count(shortSequence)} starting from {longSequence.find(shortSequence)+1} ')
    #s.count(a) a snin içinde kaç tane var bakar
    #s.find() a sde var mı bakar varsa indexini yazdırır yoksa -1 çevirir
else:
    print(f'No your piece of DNA {shortSequence} is NOT  part of {longSequence}')
'''
''' 2
VALID_GRADES= set('ABCDF')
A = 4.0
B = 3.0
C = 2.0
D = 1.0
F = 0.0
avGrade = 0.0
grade = 0.0

numberLesson = int(input("How many courses did you get for this semester : "))
firstGrade = input("Enter your first exam grade (A=4.0 / B=3.0 / C=2.0 / D=1.0 / F=0.0) : ")

if not set(firstGrade).issubset(VALID_GRADES):
    firstGrade = input("Enter a valid grade :")
else:
    if firstGrade == "A":
       avGrade=4.0
    elif firstGrade == "B":
        avGrade = 3.0
    elif firstGrade == "C":
        avGrade = 2.0
    elif firstGrade == "D":
        avGrade = 1.0
    elif firstGrade == "F":
        avGrade = 0.0
for i in range(numberLesson-1):
    grade = input(f'Enter the grade of your {i+2}. lesson :')
    if grade == "A+":
        avGrade = avGrade + (A/10)
    elif grade == "A-":
        avGrade = avGrade - (A/10)
    elif grade == "B+":
        avGrade = avGrade + (B/10)
    elif grade == "B-":
        avGrade = avGrade - (B/10)
    elif grade == "C+":
        avGrade = avGrade + (C/10)
    elif grade == "C-":
        avGrade = avGrade - (C/10)
    elif grade == "D+":
        avGrade = avGrade + (D/10)
    elif grade == "D-":
        avGrade = avGrade - (D/10)
    i+=1
print(f'Your avarage is : {avGrade: .5f}')
'''    
''' 3
message = input("Enter the message that you want to check : ")

onlyLetters = message.isalpha()
onlyUpper = message.isupper()
onlyLower = message.islower()
onlyDigit = message.isdigit()
noSpecialchars = message.isalnum()
startLower = message[0:1].islower()
endPoint = message.endswith(".")

print("\n--- Mesaj Özellikleri Kontrol Sonucu ---")
print(f'1. Only Letters ?  (isalpha): {onlyLetters}')
print(f'2. All letters are Uppercase ? (isupper): {onlyUpper}')
print(f'3. All letters are Lowercase ? (islower): {onlyLower}')
print(f'4. Only Digits ? (isdigit): {onlyDigit}')
print(f'5. Any special characters ("/,*,-,!,?) ? (isalnum): {noSpecialchars}')
print(f'6. Starting with lowercase letter ?: {startLower}')
print(f'7. Ending with point(".") ?: {endPoint}')
'''
''' 4
numbers = [0,0,0]
for i in range(3):
    numbers[i] = int(input("Enter a list of numbers :"))
    i += 1

i=0

if numbers[i] < numbers[i+1] and numbers[i+1] < numbers[i+2]:
    print("Strictly Increasing")

elif numbers[i] <= numbers[i+1] and numbers[i+1] <= numbers[i+2]:
    print("Increasing")

elif numbers[i] > numbers[i+1] and numbers[i+1] > numbers[i+2]:
    print("Strictly Decreasing")

elif numbers[i] >= numbers[i+1] and numbers[i+1] >= numbers[i+2] :
    print("Decreasing")

else:
    print("Neither increasing nor decreasing")
'''
''' 5
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

month=input("Enter the month you are in : ")

if month == monthList[-1] or month == monthList[0] or month == monthList[1]:
    print("You are in winter")

elif month == monthList[2] or month == monthList[3] or month == monthList[4]:
    print("You are is spring")

elif month == monthList[5] or month == monthList[6] or month == monthList[7]:
    print("You are in summer")

else:
    print("You are in fall") 
'''
''' 6
year = int(input("What year are you in ? "))

if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    print(f'{year} is a leap year')

else:
    print(f'{year} is NOT a leap year')
'''
''' 7
grade = 0.0
credit = 0
totalCredit = 0
measure=0.0
avGrade=0.0

numberLesson = int(input("Enter the number of lessons you get : "))

for i in range(numberLesson):
    grade = float(input(f'Enter the grade of your {i+1}. lesson : '))
    credit = int(input(f'Enter the credit of your {i+1}. lesson :'))
    measure += grade*credit 
    totalCredit += credit


avGrade = measure/totalCredit

if avGrade == 4.0:
    print(f'Your avarage grade is {avGrade} and it is equal to A+')

elif avGrade < 4.0 and avGrade >= 3.5:
    print(f'Your avarage grade is {avGrade} and it is equal to A')

elif avGrade < 3.5 and avGrade > 3.00:
    print(f'Your avarage grade is {avGrade} and it is equal to A-')

elif avGrade <= 3.0 and avGrade > 2.5:
    print(f'Your avarage grade is {avGrade} and it is equal to B')

elif avGrade < 2.5 and avGrade > 2.0:
    print(f'Your avarage grade is {avGrade} and it is equal to B-')

elif avGrade <= 2.0 and avGrade > 1.5:
    print(f'Your avarage grade is {avGrade} and it is equal to C')

elif avGrade <= 1.5 and avGrade > 1.0:
    print(f'Your avarage grade is {avGrade} and it is equal to D')

elif avGrade <= 1.0 and avGrade > 0.5:
    print(f'Your avarage grade is {avGrade} and it is equal to D-')

elif avGrade <= 0.5 and avGrade >=0.0 :
    print(f'Your avarage grade is {avGrade} and it is equal to F')
'''
''' 8
marriage = input("Are you married (please answer with UPPERCASES : )")
income = float(input("Enter your salary per month : "))
annualIncome = income*12

if marriage == "NO":
    if annualIncome > 0 and annualIncome <= 8000:
        print(f"Your tax fee is : {annualIncome*0.1}")
    elif annualIncome > 8000 and annualIncome <= 32000:
        print(f"Your tax fee is : {(annualIncome*0.15) + 800 }")
    else:
        print(f"Your tax fee is : {(annualIncome*0.25) + 4400 }")

else:
    if annualIncome > 0 and annualIncome <= 16000:
        print(f"Your tax fee is : {annualIncome*0.1}")
    elif annualIncome > 16000 and annualIncome <= 64000:
        print(f"Your tax fee is : {(annualIncome*0.15) + 1600 }")
    else:
        print(f"Your tax fee is : {(annualIncome*0.25) + 8800 }")
'''

print("Available metric units: ml, l, g, kg, mm, cm, m, km")
print("Available imperial units: fl, oz, gal, lb, in, ft, mi")


start_unit = input("Enter the starting unit: ").lower()
value = float(input("Enter the value: "))

result = None


if start_unit == "ml":
    print('You should choose "fl"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "fl":
        result = value * 0.033814
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (fl): ").lower()
        if target_unit == "fl":
            result = value * 0.033814

elif start_unit == "l":
    print('You should choose "gal"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "gal":
        result = value * 0.264172
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (gal): ").lower()
        if target_unit == "gal":
            result = value * 0.264172


elif start_unit == "g":
    print('You should choose "oz"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "oz":
        result = value * 0.035274
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (oz): ").lower()
        if target_unit == "oz":
            result = value * 0.035274

elif start_unit == "kg":
    print('You should choose "lb"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "lb":
        result = value * 2.20462
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (lb): ").lower()
        if target_unit == "lb":
            result = value * 2.20462


elif start_unit == "mm":
    print('You should choose "in"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "in":
        result = value * 0.03937
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (in): ").lower()
        if target_unit == "in":
            result = value * 0.03937

elif start_unit == "cm":
    print('You should choose "in"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "in":
        result = value * 0.3937
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (in): ").lower()
        if target_unit == "in":
            result = value * 0.3937

elif start_unit == "m":
    print('You should choose "ft"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "ft":
        result = value * 3.28084
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (ft): ").lower()
        if target_unit == "ft":
            result = value * 3.28084

elif start_unit == "km":
    print('You should choose "mi"')
    target_unit = input("Enter the unit to convert to: ").lower()
    if target_unit == "mi":
        result = value * 0.621371
    else:
        target_unit = input("Invalid unit. Choose correct one to convert (mi): ").lower()
        if target_unit == "mi":
            result = value * 0.621371


else:
    print("Invalid starting unit entered!")


if not result ==  None:
    print(f"\n{value} {start_unit} = {result:.4f} {target_unit}")

