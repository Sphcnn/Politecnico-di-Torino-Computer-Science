#Exercises of Lab2

'''  1
NUM1 = 15
NUM2 = 75

sumResult = NUM1+NUM2
difResult = NUM1-NUM2
proResult = NUM1*NUM2
avResult =(NUM1+NUM2)/2
distance = abs(NUM1-NUM2)
Max=max(NUM1,NUM2)
Min=min(NUM1,NUM2)


print(sumResult)
print(difResult)
print(proResult)
print(avResult)
print(distance)
print(Max)
print(Min)
'''

''' 2
time = input("Enter the time :")
hour=int(time[0:2])
minute=int(time[-2:])
print(hour)
totalSecond=(3600*hour)+(60*minute)

print(totalSecond)
'''

'''3
time = int(input("Enter the time as seconds:"))
day = 0
hour=int(time/3600)
second = int((time-(hour*3600))/60)

if time < 60 :
    print("Time is 00:00")
else:
    if hour < 24: 
        if hour < 10:
            if second < 10:
                print(f'Time is 0{hour}:0{second}')
            else:
                print(f'Time is 0{hour}:{second}')
        else:
            if second < 10:
                print(f'Time is {hour}:0{second}')
            else:
                print(f'Time is {hour}:{second}')
    else :
        day = int(hour / 24)
        hour = hour % 24
        if hour < 10:
            if second < 10:
                print(f'The time you said is equal to {day} day and 0{hour}:0{second}')
            else:
                print(f'The time you said is equal to {day} day and 0{hour}:{second}')
        else:
            if second < 10:
                print(f'The time you said is equal to {day} day and {hour}:0{second}')
            else:
                print(f'The time you said is equal to {day} day and {hour}:{second}')
'''



'''4
NUMBER = 12345
convNUMBER = str(NUMBER)
i=0
j=len(convNUMBER)

while i < j:
    print(f'{i}. digit is {convNUMBER[i]} ')
    i=i+1
'''

'''5
    carCost = float(input("Enter car cost:"))
    estimatedkmPerYear = float(input("Enter the value of km per year "))
    estimationOfFuelcost=50
    efficiency = 0
    valueOfAfter5year = float(input("Enter the sale price of car after 5 years"))
    carType = input("Enter your car type \(Dizel or Fuel): ")
    totalCostof5Year = 0

    if carType =="Dizel":
        efficiency = 12
    else :
        efficiency = 20

    totalCostof5Year = carCost + 5*((estimatedkmPerYear/efficiency)*estimationOfFuelcost) - valueOfAfter5year

    print(f'Your car costs {totalCostof5Year} enter the value of a car you want to buy : ')
    newCarsCost = float(input())
    if newCarsCost < totalCostof5Year:
        print("To buy a new car is logical")
    else:
        print("To buy a new car is unlogical")
'''


'''6
PI = 3.14
EPSILON = 8.854*(10**-12)
print("Enter the charges of particles:")
q1=float(input("q1:"))
q2=float(input("q2:"))

r=float(input("Enter the distance between charges:"))

force=float((q1*q2)/(4*(PI*EPSILON)*(r**2)))

print(force)
'''

''' 7
word=input("Enter a word:")
sizeOfWord=len(word)
if sizeOfWord < 6 :
    print("Too Short!")

elif 6 < sizeOfWord < 10:
    print(f'{word[0:3]}...{word[-3:]}')

else:
    print("Too Long!")
'''

'''8
number = input("Enter your phone number:")
print(f'({number[:3]}) {number[3:6]}-{number[6:]}')
'''

''' 9 
name = input("What is your name ? ")
surname = input("What is your surname ? ")
person = input("Who do you want to send message ? ")
message = input("Type your message : ")

nameinNickname = name[0:(len(name)-2)]
surnameinNickname = surname[0:(len(surname)-2)]

nikcname = nameinNickname + surnameinNickname

print(f'Your mail will be send as below: \n {nikcname} :  Hello {person}, \"{message}\"  \n Best Regards, \n {name} {surname}')

confirmation = input("Are you sure to send this mail ?  ")
if confirmation == "Yes":
    print("Your message have sent succesfuly")

else :
    conf=input("Do you want to cancel sending mail ?")
    
    if conf=="No":
        person = input("Who do you want to send message ? ")
        message = input("Type your message : ")
        print(f'Your mail will be send as below: \n {nikcname} :  Hello {person}, \"{message}\"  \n Best Regards, \n {name} {surname}')
        print("Your mail is being sent .............")

    else:
        print("Mail sending has been canceled ....... ")
'''


''' 10
NUM1 = 15
NUM2 = 75

Sum = NUM1+NUM2
Difference = NUM1-NUM2
Product = NUM1*NUM2
Avarage =(NUM1+NUM2)/2
Distance = abs(NUM1-NUM2)
Max=max(NUM1,NUM2)
Min=min(NUM1,NUM2)

message = "                    "#20 spaces
message[0:len("Sum")] = Sum
message[-len(str(Sum)):] = str(Sum)

print(message)
'''
print("Hello World")