#Exercises of Lab4
''' 1
numbers = []
sum_numbers = 0

while True:
    number = input("Enter a number (0 to quit): ")
    if number == "0":
        break   
    numbers.append(int(number))
    sum_numbers += int(number)

if numbers:  
    print(f"Sum of your numbers: {sum_numbers}")
    print(f"Max and min of your numbers: {max(numbers)}, {min(numbers)}")
else:
    print("You didn't enter any numbers.")
'''
''' 2
vowel=["a", "e", "i", "o", "u","A","E","I","O","U"]
outputCapital = []
outputEvenLetters = []
outputNoVowel = []
numberofDigits = 0
positionOfVowels = []

text = input("Enter a sentence : ")
textList = list(text)

for i,letter in enumerate(text):
    if letter.isupper():
        outputCapital.append(letter)
    else: pass     
    
    if i%2 == 0:
        if letter.isalpha():
            outputEvenLetters.append(letter)
    else: pass

    if letter in vowel:
        textList[i] = "_"
        outputNoVowel = "".join(textList)
        #stringler immutable olduğu için önce bir listeye atayıp sonrasında işlem yapmak gerkeiyor. İşlem bittikten sonra da join fonksiyonu ile tekrar stringe çevrilmeli.
    else: pass

    if letter.isdigit():
        numberofDigits +=1
    else: pass

    if letter in vowel:
        positionOfVowels.append(i)
    else: pass

print(outputCapital)
print(outputEvenLetters)
print(outputNoVowel)
print(numberofDigits)
print(positionOfVowels)
'''

''' 3
print("WELCOME TO THE CHATBOX (type Quit or quit to end chatting !)")
username1 = input("Enter the first username : ")
username2 = input("Enter the second username : ")
numMessage = 0
text = ""  

turn = 1 
current_user = username1


while text.lower() != "quit": 
    if turn == 1:
        current_user = username1
    else:
        current_user = username2
 
    text = input(f'{current_user} (Enter message): ')
    if text.lower() == "quit":
        print("Chat ended.")
        break
        
    if text.isdigit():
        print("Unvalid message: Message cannot contain only digits. Start chatting from zero.")
        break
        
    print(f'{current_user:<20}: {text}')
    
    numMessage += 1
    
    turn = 3 - turn 

print(f"Total messages sent: {numMessage}")
'''
''' 4
num = int(input("Enter number :"))

for i in range(num):
    print("*"*num)


for i in range(num):
    numStar = (2*(i+1))-1
    numSpace = num - (i+1)
    print(f'{" "*numSpace}{"*"*numStar}')

for i in range(num-1):
    j = num - i
    numStar = (2*(j-1))-1
    numSpace = num - (j-1)
    print(f'{" "*numSpace}{"*"*numStar}')
'''
''' 5
text = input("Enter a word : ")

textList = list(text)

reversedList = []
reversedUpperList = []

for i in range(len(text)):
    reversedList.append(textList[len(text)-i-1])
    if reversedList[i].isupper():
        reversedUpperList.append(reversedList[i]) 
print(f'{"".join(reversedList)}')
print(f'{"".join(reversedUpperList)}')
'''
''' 6
number = int(input("Enter a number: "))
primeList = []

for i in range(2, number + 1):  
    divisor = 2
    is_prime = True             

    while divisor < i:         
        if i % divisor == 0:
            is_prime = False    
            break
        divisor += 1

    if is_prime:
        primeList.append(i)

for num in primeList:
    print(num)
''' 

''' 7
text = input("Enter a word: ")

for i in range(1, len(text) + 1):     
    for j in range(0, len(text) - i + 1):  
        print(text[j:j + i])
'''

''' 8
numList = []
a = input("Deneme : ")
check = True

while check:
    number = input("Enter number (quit = q): ")
    if number.lower() == "q":
        check = False
    else:
        numList.append(number)

previous = numList[0]
counter = 1
lastList = []

for i in range(1, len(numList)):
    if numList[i] == previous:
        counter += 1
    else:
        if counter >= 2:
            lastList.append(previous)
        previous = numList[i]
        counter = 1

if counter >= 2:
    lastList.append(previous)
else: pass

if not lastList:
    print("There is no duplicated number.")
else:
    print("Duplicated numbers:", lastList)
'''

''' 9
import random

numberMarble = random.randint(10, 100)
player = random.randint(0, 1)  
smartMode = random.randint(0, 1)  

print(f"\nInitial marbles: {numberMarble}")
print("First player:", "Computer" if player == 0 else "User")
print("Computer mode:", "SMART" if smartMode == 1 else "DUMB")

targetValues = [3, 7, 15, 31, 63]

while numberMarble > 0:

    if numberMarble == 1:
        if player == 0:
            print("\nYou WON! Computer took the last marble.")
        else:
            print("\nYou LOST! You took the last marble.")
        break

    maxTake = numberMarble // 2

    if player == 0:

        if smartMode == 0:
            taken = random.randint(1, maxTake)

        else:
            target = None
            for t in targetValues:
                if t < numberMarble:
                    target = t

            if target is None:
                taken = random.randint(1, maxTake)

            else:
                desired = numberMarble - target
                if 1 <= desired <= maxTake:
                    taken = desired
                else:
                    taken = random.randint(1, maxTake)

        print(f"\nComputer takes {taken} marbles.")
        numberMarble -= taken
        print(f"Marbles left: {numberMarble}")

    else:
        print(f"\nYour turn! Marbles left: {numberMarble}")
        taken = int(input(f"How many marbles will you take? (1–{maxTake}): "))

        if taken < 1 or taken > maxTake:
            print("Invalid move — You lose for cheating!")
            break

        numberMarble -= taken
        print(f"You took {taken}. Marbles left: {numberMarble}")

    player = 1 - player
'''
''' 10
import math 

Azero = int(input("Enter the beginning value : "))
Thalf = 6
landa = (math.log(2))/Thalf
t  = 1
e = math.e

for t in range(0,25):
    A = Azero*( e **(-landa*t))
    print(f'{t:>5} hours later : {A: <10.4f} percentage : %{((A/Azero)*100):<10.4f}')
'''

'''11
G = 9.81
DELTA_T = 0.01


v0 = float(input("Enter the initial velocity (m/s): "))
v = v0
s = 0.0
t = 0.0

print("Time (s) | Simulated pos (m) | Exact pos (m) | Velocity (m/s)")
print("-------------------------------------------------------------")


while s >= 0:
    pos_exact = (-0.5) * G * (t**2) + v0 * t

    s = s + v * DELTA_T
    v = v - G * DELTA_T
    t += DELTA_T

    if abs(t - round(t)) < DELTA_T/2:
        print(f"{t:6.1f} | {s:17.2f} | {pos_exact:13.2f} | {v:10.2f}")
'''
print("Welcome to the messaging application. You can text your friend here. The message turn will be first user's until he or she will type \"Pass or pass\" \n To quit application you should type \"Quit or quit\" ")
print("-"*20)
username1 = input("Enter the first username : ")
username2 = input("Enter the first username : ")
turn = 1
statement = True
numberMessage = 0
lengthList1 = []
lengthList2 = []
while statement:
    if turn == 1:
        text = input(f'{username1} Enter your message : ')
        if text.lower() == "quit":
            break
        elif text.lower() == "pass":
            turn = 1-turn
        else:
            print(f'{username1:.15s} :  {text:<.50s}')
            numberMessage += 1
            lengthList1.append(len(text))
    else:
        text = input(f'{username2} Enter your message : ')
        if text.lower() == "quit":
            break
        elif text.lower() == "pass":
            turn = 1-turn
        else:
            print(f'{username2:.15s} :  {text:<.50s}')
            numberMessage += 1
            lengthList2.append(len(text))
if not lengthList1:
    print(f'The shortest text of the chat longs {sorted(lengthList2)[0]} and this message is written by {username2}')
    print(f'The longest text of the chat longs {sorted(lengthList2)[-1]} and this message is written by {username2}')
elif not lengthList2:
    print(f'The shortest text of the chat longs {sorted(lengthList1)[0]} and this message is written by {username2}')
    print(f'The longest text of the chat longs {sorted(lengthList1)[-1]} and this message is written by {username2}')
else:
    if sorted(lengthList1)[0] < sorted(lengthList2)[0]:
        print(f'The shortest text of the chat longs {sorted(lengthList1)[0]} and this message is written by {username2}')

    elif sorted(lengthList1)[0] > sorted(lengthList2)[0]:
        print(f'The shortest text of the chat longs {sorted(lengthList2)[0]} and this message is written by {username1}')

    else:
        print(f'The shortest text of the chat longs {sorted(lengthList2)[0]} and this message is written by both {username1} and {username2}')


    if sorted(lengthList1)[-1] < sorted(lengthList2)[-1]:
        print(f'The longest text of the chat longs {sorted(lengthList2)[-1]} and this message is written by {username2}')

    elif sorted(lengthList1)[-1] > sorted(lengthList2)[-1]:
        print(f'The longest text of the chat longs {sorted(lengthList1)[-1]} and this message is written by {username1}')

    else:
        print(f'The longest text of the chat longs {sorted(lengthList2)[-1]} and this message is written by both {username1} and {username2}')

totalLen = 0
for num in lengthList1:
    totalLen += num
for num in lengthList2:
    totalLen += num    

print(f'The total lenght of speech is {totalLen} !')