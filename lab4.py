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

previous = None
count = 0

while True:
    line = input("Enter number (empty to finish): ")

    if line == "":   # boş satır bitirir
        break

    current = int(line)

    # İlk sayı ise
    if previous is None:
        previous = current
        count = 1
        continue

    # Aynı sayı ise -> duplicate devam ediyor
    if current == previous:
        count += 1
    else:
        # Farklı sayı gelince seri bitmiş olur
        if count >= 2:
            print(previous)

        # Yeni sayıya başla
        previous = current
        count = 1

# Döngü bittiğinde son seriyi kontrol et
if count >= 2:
    print(previous)

