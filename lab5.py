#Exercises of Lab5
''' 1
PIN=1234

for i in range(2):
    password = int(input("Enter your password : "))
    if password == PIN:
        print("You have entered successfuly !")
        break
    else:
        if not i >= 2:
            print("Try Again")
        else:
            print("Your card is blocked")

'''
''' 2
number = int(input("Enter a number : "))
i=2
while(number!=0):
    if number % i == 0:
        print(i)
        number = number / i
        if number == 1:
            break
    else:
        i+=1
'''  
''' 3
TICKET = 100
buyers = 0

while(TICKET != 0):
    ticket = int(input("How many tickets do you want to buy ? "))
    while(ticket > 4 ):
        ticket = int(input("You can buy 4 ticket at most. Try again : "))
    buyers += 1
    TICKET = TICKET - ticket
    print(f'{TICKET} tickets left')

print(f'The number of buyers : {buyers}')
'''
''' 4
a = 32310901
b = 1729
m = 224
r1=int(input("Enter a inital value : "))

for i in range(100):
    r2 = ((a*r1) + b) % m
    print(r2)
    r1=r2
'''
''' 5
import math
location_x = 0
location_y = 0
DIRECTIONS = ["N","S","E","W"]

for i in range(10):
    direction = input("Select your way (N,S,E,W) : ")
    while (not direction in DIRECTIONS):
        direction = input("Select valid way (N,S,E,W) : ")

    if direction == "N":
        location_y += 1
    elif direction == "S":
        location_y -= 1
    elif direction == "E":
        location_x += 1
    elif direction == "W":
        location_x += 1
    i+=1

print(f'You were at (0,0) and came to ({location_x},{location_y}) so you walked {math.sqrt((location_x**2)+(location_y**2)): .2f}')
'''

'''6
growthPredators = float(input("Enter rate of growth of predators : "))
destructionRate = float(input("Enter rate of destruction by predators : "))
deathPredators = float(input("Enter rate of death of predators : "))
increasePredators = float(input("Enter rate of increase of predators : "))
populationPredators = float(input("Enter the population population of predators : "))
populationPrey = float(input("Enter the population population of prey : "))
period = int(input("Enter the period of simulation : "))



for i in range(period):
    populationPrey = populationPrey * (1 + growthPredators - (destructionRate*populationPredators))
    populationPredators = populationPredators * (1- deathPredators + (increasePredators*populationPrey))

    if populationPrey <= 0:
        print(f"There is not anymore prey {populationPrey} number of predators : {populationPredators}")
        break
    elif populationPredators <= 0:
        if populationPrey <= 0:
            print(f"There is not anymore predator {populationPredators} number of preys : {populationPrey}")
            break
    else:
        print(f'The population of preys : {populationPrey : .2f} and predators {populationPredators : .2f} in {i+1}')
    i += 1
'''
SPEAKER_RESISTANCE = 8
VOLTAGE_SOURCE = 40
AMPLIFIER_RESISTANCE = 20

n = float(input("Enter your turns ratio: "))
speakerPower = 0

while n <= 2:
    speakerPower = ((n * VOLTAGE_SOURCE) ** 2) * SPEAKER_RESISTANCE / ((n**2 * SPEAKER_RESISTANCE + AMPLIFIER_RESISTANCE) ** 2)
    print(f"Transformer turned values from {AMPLIFIER_RESISTANCE}Ω and {VOLTAGE_SOURCE}V "
          f"to {SPEAKER_RESISTANCE}Ω and {speakerPower:.4f} W with {n:.2f} turns ratio")
    n += 0.01
